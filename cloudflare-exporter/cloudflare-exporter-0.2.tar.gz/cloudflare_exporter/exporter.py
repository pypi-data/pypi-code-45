import argparse
import logging

from aiohttp import web
from prometheus_client.core import REGISTRY

from cloudflare_exporter.collector import CloudflareCollector
from cloudflare_exporter.config import DEFAULT_HOST, DEFAULT_PORT, LOG_FORMAT
from cloudflare_exporter.handlers import handle_health, handle_metrics


def parse_args():
    parser = argparse.ArgumentParser(description='Cloudfalre prometheus exporter')
    parser.add_argument('-t', '--token', type=str, required=True,
                        help='Cloudflare API Token')
    parser.add_argument('--host', type=str,
                        help='TCP/IP host for HTTP server',
                        default=DEFAULT_HOST)
    parser.add_argument('--port', type=int,
                        help="Port used to expose metrics for Prometheus",
                        default=DEFAULT_PORT)
    return parser.parse_args()


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    args = parse_args()
    REGISTRY.register(CloudflareCollector(cloudflare_token=args.token))
    app = web.Application()
    app.router.add_get('/metrics', handle_metrics)
    app.router.add_get('/health', handle_health)
    print(f'======== Running on http://{args.host}:{args.port}/metrics ========')
    web.run_app(app, host=args.host, port=args.port, access_log=None,
                print=False)


if __name__ == '__main__':
    main()
