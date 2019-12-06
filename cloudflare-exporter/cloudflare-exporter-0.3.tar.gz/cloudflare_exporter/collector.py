import time
from collections import Counter, defaultdict
from statistics import mean

import CloudFlare
from prometheus_client.core import GaugeMetricFamily

from cloudflare_exporter.config import (LOGS_EXTENDED_METRIC,
                                        LOGS_EXTENDED_METRIC_COUNT,
                                        LOGS_EXTENDED_METRIC_SAMPLE,
                                        LOGS_EXTENDED_METRIC_RANGE)
from cloudflare_exporter.lib.statistics import quantiles


class CloudflareCollector:
    def __init__(self, cloudflare_token):
        self.cloudflare_token = cloudflare_token

    def logs_collect(self, families):
        if LOGS_EXTENDED_METRIC:
            families['received_requests_pop_origin'] = GaugeMetricFamily(
                'cloudflare_by_origin_received_requests',
                'Requests received at this PoP location.',
                labels=['zone', 'colo_id', 'origin_ip', 'client_country'])

            for tile in ['avg', '50tile', '90tile']:
                families[f'origin_response_time_{tile}'] = GaugeMetricFamily(
                    f'cloudflare_origin_response_time_{tile}',
                    f'Response Time:{tile}',
                    labels=['zone', 'colo_id', 'origin_ip', 'client_country'])

            for metric in _get_cloudflare_metrics_from_logs(self.cloudflare_token):
                for keys, value in metric.received_requests_pop_origin.items():
                    families['received_requests_pop_origin'].add_metric(keys, value)
                for keys, values in metric.origin_response_times.items():
                    families['origin_response_time_avg'].add_metric(keys, mean(values))

                    try:
                        decile = quantiles(values, n=10)
                    except ValueError:
                        # Not enough Data.
                        continue
                    families['origin_response_time_50tile'].add_metric(keys, decile[5 - 1])
                    families['origin_response_time_90tile'].add_metric(keys, decile[9 - 1])

    def collect(self):
        families = {
            'received_requests': GaugeMetricFamily(
                'cloudflare_pop_received_requests',
                'Requests received at this PoP location.',
                labels=['zone', 'type', 'colo_id'],
            ),
            'bandwidth_bytes': GaugeMetricFamily(
                'cloudflare_pop_bandwidth_bytes',
                'Bandwidth used from this PoP location.',
                labels=['zone', 'type', 'colo_id'],
            ),
            'http_responses_sent': GaugeMetricFamily(
                'cloudflare_pop_http_responses_sent',
                'Breakdown per HTTP response code.',
                labels=['zone', 'colo_id', 'http_status'],
            ),
            'threats_seen': GaugeMetricFamily(
                'cloudflare_pop_threats_seen',
                'Threats identified.',
                labels=['zone', 'colo_id', 'threats'],
            ),
            'threat_types': GaugeMetricFamily(
                'cloudflare_pop_threat_types',
                'Threat breakdown per threat type.',
                labels=['zone', 'colo_id', 'threat_type'],
            ),
            'threat_countries': GaugeMetricFamily(
                'cloudflare_pop_threat_countries',
                'Threat breakdown per country.',
                labels=['zone', 'colo_id', 'threat_country'],
            ),
        }
        if LOGS_EXTENDED_METRIC:
            self.logs_collect(families)

        for zone, raw_data in _get_cloudflare_analytics(self.cloudflare_token):
            # We're interested in the latest metrics, however
            # the Cloudflare API doesn't guarantee non-zero values.
            # Index -2 was chosen empirically and is usually non-zero.
            for pop_data in raw_data:
                serie = pop_data['timeseries'][-2]

                families['received_requests'].add_metric(
                    [zone, 'cached', pop_data['colo_id']], serie['requests']['cached']
                )
                families['received_requests'].add_metric(
                    [zone, "uncached", pop_data["colo_id"]], serie["requests"]["uncached"]
                )

                families["bandwidth_bytes"].add_metric(
                    [zone, "cached", pop_data['colo_id']], serie['bandwidth']['cached']
                )
                families['bandwidth_bytes'].add_metric(
                    [zone, 'uncached', pop_data['colo_id']], serie['bandwidth']['uncached']
                )

                for http_status, count in serie["requests"]["http_status"].items():
                    families['http_responses_sent'].add_metric(
                        [zone, pop_data["colo_id"], http_status], count
                    )

                families['threats_seen'].add_metric(
                    [zone, pop_data['colo_id']], serie['threats']['all']
                )

                for threat, count in serie['threats']['type'].items():
                    families['threat_types'].add_metric(
                        [zone, pop_data['colo_id'], threat], count
                    )

                for country, count in serie['threats']['country'].items():
                    families['threat_countries'].add_metric(
                        [zone, pop_data['colo_id'], country], count
                    )

        for metric in families.values():
            yield metric


def _get_cloudflare_analytics(token):
    cloudflare = CloudFlare.CloudFlare(debug=False, token=token)
    for zone in cloudflare.zones.get():
        # get the last 30 minutes (the very last 5 minutes are usually not correct)
        try:
            series = cloudflare.zones.analytics.colos(zone['id'], params={'since': -35, 'until': -5})
        except CloudFlare.exceptions.CloudFlareAPIError as exception:
            if int(exception) == 10_000:
                # Authentication error on this zone. We continue for others zones
                continue
            raise exception
        yield zone['name'], series


def nanos2s(nanos):
    """Transform nanoseconds to seconds

    :param time: Time in Nanoseconds
    :return: Time in seconds
    """
    return nanos / 1_000_000


class LogMetrics:
    def __init__(self):
        self.received_requests_pop_origin = Counter()
        self.origin_response_times = defaultdict(list)

    def add(self, zone, serie):
        # Log by originIP are useless in Cache Mode
        if not serie['CacheTieredFill']:
            key = (zone, serie['EdgeColoCode'], serie['OriginIP'], serie['ClientCountry'])
            self.received_requests_pop_origin[key] += 1
            self.origin_response_times[key].append(nanos2s(serie['OriginResponseTime']))


def _get_cloudflare_metrics_from_logs(token):
    cloudflare = CloudFlare.CloudFlare(debug=False, token=token)
    # from cf docs: Must be at least 1 minute earlier than now and later than start
    # Sometime 1 minutes is not enough...
    end = int(time.time() - 60 * 1)
    start = end - 60 * LOGS_EXTENDED_METRIC_RANGE
    for zone in cloudflare.zones.get():
        series = cloudflare.zones.logs.received(zone['id'],
                                                params={'end': end,
                                                        'start': start,
                                                        'fields': 'CacheTieredFill,ClientCountry,'
                                                                  'EdgeColoCode,ConnectTimestamp,'
                                                                  'OriginIP,'
                                                                  'OriginResponseTime',
                                                        'count': LOGS_EXTENDED_METRIC_COUNT,
                                                        'sample': LOGS_EXTENDED_METRIC_SAMPLE
                                                        })
        if not isinstance(series, list):
            # cloudflare.zones.logs.received don't raise any error on authentification failure
            # but answer {'success': False, 'errors': [{'code': 10000, 'message': 'Authentication error'}]}
            if not series.get('errors') or series.get('errors')[0].get('code') != 10_000:
                raise Exception(f'/zones.logs.received {series} - api call failed')
            continue

        metrics = LogMetrics()
        for serie in series:
            metrics.add(zone['name'], serie)
    yield metrics
