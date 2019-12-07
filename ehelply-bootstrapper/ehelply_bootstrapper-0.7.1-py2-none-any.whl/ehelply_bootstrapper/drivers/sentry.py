from ehelply_bootstrapper.drivers.driver import Driver
from ehelply_bootstrapper.utils.state import State
from ehelply_bootstrapper.utils.service import ServiceMeta
from ehelply_bootstrapper.utils.environment import Environment
import sentry_sdk


class Sentry(Driver):
    def __init__(self, service_meta: ServiceMeta, service_process: str):
        self.service_meta: ServiceMeta = service_meta
        self.service_process: str = service_process
        super().__init__()

    def setup(self):
        sentry_sdk.init(
            State.config.bootstrap.sentry.dsn,
            environment=Environment.stage(),
            release=self.service_meta.version,
            server_name=self.service_process,
            debug=Environment.is_dev()
        )


