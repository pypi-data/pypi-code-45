import sys
from argparse import ArgumentParser
from getpass import getpass
from os import name as os_name

from progressbar import ProgressBar

from manga_py.fs import check_free_space, get_temp_path
from manga_py.parser import Parser


class Cli:  # pragma: no cover
    args = None
    parser = None
    _info = None
    __progress_bar = None

    def __init__(self, args: ArgumentParser, info=None):
        self.args = args.parse_args()
        self.parser = Parser(args)
        self._info = info

        space = self.args.min_free_space
        if not check_free_space(get_temp_path(), space) or not check_free_space(self.args.destination, space):
            raise OSError('No space left on device')

    def start(self):
        try:
            self.parser.init_provider(
                progress=self.progress,
                log=self.print,
                quest=self.quest,
                quest_password=self.quest_password,
                info=self._info,
            )
        except AttributeError as e:
            print(e, file=sys.stderr)
            print('Please check if your inputed domain is supported by manga-py: ', file=sys.stderr)
            print('- https://manga-py.com/manga-py/#resources-list', file=sys.stderr)
            print('- https://manga-py.github.io/manga-py/#resources-list (alternative)', file=sys.stderr)
            print('- https://yuru-yuri.github.io/manga-py/ (deprecated)', file=sys.stderr)
            print('Make sure that your inputed URL is correct\n\nTrace:', file=sys.stderr)
            raise e
        self.parser.start()
        self.__progress_bar and self.__progress_bar.value > 0 and self.__progress_bar.finish()
        self.args.quiet or self.print(' ')

    def __init_progress(self, items_count: int, re_init: bool):
        if re_init or not self.__progress_bar:
            if re_init:
                self.__progress_bar.finish()
            bar = ProgressBar()
            self.__progress_bar = bar(range(items_count))
            self.__progress_bar.init()

    def progress(self, items_count: int, current_item: int, re_init: bool = False):
        if not items_count:
            return
        if not self.args.no_progress and not self.args.print_json:
            current_val = 0
            if self.__progress_bar:
                current_val = self.__progress_bar.value
            self.__init_progress(items_count, re_init and current_val > 0)
            self.__progress_bar.update(current_item)

    def print(self, text, **kwargs):
        if os_name == 'nt':
            text = str(text).encode().decode(sys.stdout.encoding, 'ignore')
        self.args.quiet or print(text, **kwargs)

    def _single_quest(self, variants, title):
        self.print(title)
        for v in variants:
            self.print(v)
        return input()

    def _multiple_quest(self, variants, title):
        self.print('Accept - blank line + enter')
        self.print(title)
        for v in variants:
            self.print(v)
        result = []
        while True:
            _ = input().strip()
            if not len(_):
                return result
            result.append(_)

    def quest(self, variants: enumerate, title: str, select_type=0):  # 0 = single, 1 = multiple
        if select_type:
            return self._multiple_quest(variants, title)
        return self._single_quest(variants, title)

    def quest_password(self, title):
        return getpass(title)
