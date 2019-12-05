from abc import ABC, abstractmethod
import logging
import os
import sys

from prometheus_client import CollectorRegistry

from nubium_utils.monitoring import MetricsPusher, Monitor
from .instrumented_app import InstrumentedApp

LOGGER = logging.getLogger()


class FaustAppWrapper(ABC):
    """
    A wrapper around the Faust app so that it may be more easily unit tested.
    """

    def __init__(self, faust_config, avro_client, hostname, metrics_service_name, metrics_service_port, metrics_pod_port):
        self.faust_config = faust_config
        self.avro_client = avro_client

        self.app = InstrumentedApp(**self.faust_config)
        self.app.wrapper = self

        self.monitor = Monitor(job=hostname, app=self.faust_config['id'], registry=CollectorRegistry())
        self.metrics_pusher = MetricsPusher(
            job=self.monitor.job,
            registry=self.monitor.registry,
            metrics_service_name=metrics_service_name,
            metrics_service_port=metrics_service_port,
            metrics_pod_port=metrics_pod_port
        )

        self._init_serializers()
        self._init_records()
        self._init_topics()
        self._init_tables()
        self._init_agents()
        self._init_monitoring()

    def get_schema_path(self, file, schema_path_from_src_root='./schemas'):
        """
        Ensures that the Faust app's schema files are always correctly referenced/loaded regardless of your init path.
        :param file: name of the schema file
        :param schema_path_from_src_root: based on the root of the app, where the schemas folder is located.
        :return: relative path to load the schema at runtime
        """
        runtime_path = os.getcwd()
        app_file_path = os.path.abspath(sys.modules[self.__module__].__file__)
        common_path = os.path.commonpath([runtime_path, app_file_path])
        rel_path = os.path.relpath(common_path, runtime_path)
        return os.path.join(runtime_path, rel_path, schema_path_from_src_root, file)

    @abstractmethod
    def _init_serializers(self):
        pass

    @abstractmethod
    def _init_records(self):
        pass

    @abstractmethod
    def _init_topics(self):
        pass

    @abstractmethod
    def _init_tables(self):
        pass

    @abstractmethod
    def _init_agents(self):
        pass

    def agent_exception(self, exc):
        """
        Increments the message errors metric by one
        :param exc:
        :return:
        """
        self.monitor.message_errors.inc(1)

    def _init_monitoring(self):
        """
        Defines method for updating metrics from Faust sensor and pushing data
        :return: None
        """

        @self.app.timer(2)
        async def push_metrics():
            """
            Updates gauges from Faust and pushes data to prometheus pushgateways
            :return: None
            """
            self.set_gauges()
            self.metrics_pusher.set_gateways()
            self.metrics_pusher.push_metrics()

    def set_gauges(self):

        self.monitor.messages_consumed.labels(
            job=self.monitor.job,
            app=self.monitor.app
        ).set(self.app.monitor.messages_received_total)
        self.monitor.messages_produced.labels(
            job=self.monitor.job,
            app=self.monitor.app
        ).set(self.app.monitor.messages_sent)
