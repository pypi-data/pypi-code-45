import os
import time
from argparse import ArgumentParser

from django.conf import settings
from django.core.management import call_command

from rest_base.commands import BaseCommand
from rest_base.settings import base_settings


class Command(BaseCommand):
    help = (
        'Dump model instances as predefined for future deployment'
    )

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('model', type=str, help='Specifies the model to dump in the format of app_label.ModelName')
        parser.add_argument(
            '-f', '--filename', nargs='?', type=str, help='Specifies the file name of dumps (default: ModelName.json)')

    def handle(self, *args, **options):
        model: str = options['model']
        filename: str = options['filename']
        if filename is None:
            filename = f"{model.split('.')[-1]}.json"

        try:
            base_dir = settings.BASE_DIR
        except AttributeError as e:
            raise AttributeError('BASE_DIR must be defined in Django settings') from e
        path = os.path.join(base_dir, base_settings.PREDEFINED_ROOT, filename)

        t = time.time()
        self.log(f'dump {model} instances to:')
        self.log(path)

        with open(path, 'w', encoding='utf-8') as f:
            call_command('dumpdata', model, format='json', indent=2, stdout=f)

        self.log(f'done ({time.time() - t:.2f} s)')
