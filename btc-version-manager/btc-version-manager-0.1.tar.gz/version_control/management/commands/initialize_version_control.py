from django.core.management import BaseCommand
from django.utils import timezone

from version_control.service import VersionControlManager
from version_control.utils import make_date_for_arg_parse, make_time_for_arg_parse


class Command(BaseCommand):
    """
    A command for populate the version pool

    For objects that are tracked by the version manager but do not have initial states
    """

    def add_arguments(self, parser):
        parser.add_argument('date', type=make_date_for_arg_parse)
        parser.add_argument('time', type=make_time_for_arg_parse)

    def handle(self, *args, **options):
        datetime = timezone.datetime.combine(options.get('date').date(), options.get('time').time())
        version_control_manager = VersionControlManager()
        version_control_manager.initialize_version_control(datetime)
