from prefect.utilities.tasks import defaults_from_attrs
from .query import Query


class QueryTimeseries(Query):
    def __init__(self, key, timeseries=None, url=None):
        super().__init__(key, url)
        self.name = "Timeseries"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.timeseries = timeseries
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, ca_id: str, timeseries: str):
        if "error" in ca_id:
            return ca_id
        return "{url}/timeseries/{timeseries}/{ca_id}".format(url=url, ca_id=ca_id, timeseries=timeseries)

    @defaults_from_attrs('url', 'timeseries')
    def run(self, data, timeseries=None, url=None):
        full_url = self.prep(url, data, timeseries)
        response = self.query(full_url)
        result = self.process(response)
        return result


class GetAllTimeseries(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "TimeseriesAllSignals"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str):
        return "{url}/timeseries".format(url=url)

    def post_process(self, result):
        if "data" in result:
            return result["data"]
        return []

    @defaults_from_attrs('url')
    def run(self, url=None):
        full_url = self.prep(url)
        response = self.query(full_url)
        result = self.process(response)
        timeseries = self.post_process(result)
        return timeseries


class SearchCompany(Query):
    def __init__(self, key, url=None):
        super().__init__(key, url)
        self.name = "TimeseriesCompany"
        self.url = url
        self.key = "apiKey {}".format(key)
        self.log_prefix = self.build_log_prefix()

    def prep(self, url: str, timeseries_id: str):
        if "error" in timeseries_id:
            return timeseries_id
        return "{url}/companies?name={timeseries_id}".format(url=url, timeseries_id=timeseries_id)

    @defaults_from_attrs('url')
    def run(self, data, url=None):
        full_url = self.prep(url, data)
        response = self.query(full_url)
        result = self.process(response)
        return result
