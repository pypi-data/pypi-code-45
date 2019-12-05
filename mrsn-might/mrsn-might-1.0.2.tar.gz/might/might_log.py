"""
Copyright 2017 Ryan Wick (rrwick@gmail.com)
https://github.com/rrwick/Unicycler
This module contains a Unicycler class for writing output to both stdout and a log file.
This file is part of Unicycler. Unicycler is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. Unicycler is distributed in
the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details. You should have received a copy of the GNU General Public License along with Unicycler. If
not, see <http://www.gnu.org/licenses/>.
"""

import sys
import datetime
import re
import shutil
import textwrap
import subprocess
from pathlib import Path


def initialize_logger_attributes(sample, log_filename=None, stdout_verbosity_level=1, log_file_verbosity_level=None):
    sample.log_filename = log_filename

    # initialize the log file
    if not Path(str(sample.log_filename)).expanduser().resolve().exists():
        subprocess.run(['touch', str(sample.log_filename)])

    # Determine if the terminal supports colours or not.
    try:
        sample.colors = int(subprocess.check_output(['tput', 'colors']).decode().strip())
    except (ValueError, subprocess.CalledProcessError, FileNotFoundError, AttributeError):
        sample.colors = 1

    # There are two verbosity levels: one for stdout and one for the log file. They are the
    # same, except that the log file verbosity level is never 0.
    sample.stdout_verbosity_level = stdout_verbosity_level
    if not log_file_verbosity_level:
        sample.log_file_verbosity_level = stdout_verbosity_level
    else:
        sample.log_file_verbosity_level = log_file_verbosity_level
    sample.log_file_verbosity_level = max(1, sample.log_file_verbosity_level)


def open_log_file(log_file=None):
    if log_file:
        log_file_exists = Path(str(log_file)).expanduser().resolve()
        return open(str(log_file_exists), 'at', 1, encoding='utf8')  # line buffering


def close_log_file(log_file_handle):
    if log_file_handle and not log_file_handle.closed:
        log_file_handle.close()


def log(text, colors=1, verbosity=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None, stderr=False,
        end='\n', print_to_screen=True, write_to_log_file=True):

    text_no_formatting = remove_formatting(text)

    # The text is printed to the screen with ANSI formatting, if supported. If there are only 8
    # colours available, then remove the 'dim' format which doesn't work.
    if stderr or (verbosity <= stdout_verbosity_level and print_to_screen):
        if colors <= 1:
            text = text_no_formatting
        elif colors <= 8:
            text = remove_dim_formatting(text)
        if stderr:
            print(text, file=sys.stderr, end=end, flush=True)
        else:
            print(text, end=end, flush=True)

    # The text is written to file without ANSI formatting.
    if log_file and verbosity <= log_file_verbosity_level and write_to_log_file:

        # open the log file for writing
        log_file_handle = open_log_file(log_file=log_file)

        log_file_handle.write(text_no_formatting)
        log_file_handle.write('\n')

        # close the log file
        close_log_file(log_file_handle)


def log_section_header(message, colors=1, verbosity=1, stdout_verbosity_level=1, log_file_verbosity_level=1,
                       log_file=None, single_newline=False):
    """
    Logs a section header. Also underlines the header using a row of dashes to the log file
    (because log files don't have ANSI formatting).
    """
    if single_newline:
        log('',
            colors=colors,
            verbosity=verbosity,
            stdout_verbosity_level=stdout_verbosity_level,
            log_file_verbosity_level=log_file_verbosity_level,
            log_file=log_file)
    else:
        log('\n',
            colors=colors,
            verbosity=verbosity,
            stdout_verbosity_level=stdout_verbosity_level,
            log_file_verbosity_level=log_file_verbosity_level,
            log_file=log_file)

    time = get_timestamp()
    time_str = '(' + time + ')'
    if colors > 8:
        time_str = dim(time_str)
    log(bold_yellow_underline(message) + ' ' + time_str,
        colors=colors,
        verbosity=verbosity,
        stdout_verbosity_level=stdout_verbosity_level,
        log_file_verbosity_level=log_file_verbosity_level,
        log_file=log_file)
    log('-' * (len(message) + 3 + len(time)),
        colors=colors,
        verbosity=verbosity,
        stdout_verbosity_level=stdout_verbosity_level,
        log_file_verbosity_level=log_file_verbosity_level,
        log_file=log_file,
        print_to_screen=False)


def log_progress_line(sample, completed, total, base_pairs=None, end_newline=False):
    """
    Logs a progress line using a carriage return to overwrite the previous progress line. Only the
    final progress line will be written to the log file.
    """
    progress_str = int_to_str(completed) + ' / ' + int_to_str(total)
    if total > 0:
        percent = 100.0 * completed / total
    else:
        percent = 0.0
    progress_str += ' (' + '%.1f' % percent + '%)'
    if base_pairs is not None:
        progress_str += ' - ' + int_to_str(base_pairs) + ' bp'

    end_char = '\n' if end_newline else ''
    sample.log('\r' + progress_str, end=end_char, write_to_log_file=False)
    if end_newline:
        log(progress_str, print_to_screen=False)


def log_explanation(text, colors=1, verbosity=1, stdout_verbosity_level=1, log_file_verbosity_level=1, log_file=None,
                    print_to_screen=True, write_to_log_file=True, extra_empty_lines_after=1, indent_size=4):
    """
    This function writes explanatory text to the screen. It is wrapped to the terminal width for
    stdout but not wrapped for the log file.
    """
    text = ' ' * indent_size + text
    if print_to_screen:
        terminal_width = shutil.get_terminal_size().columns
        for line in textwrap.wrap(text, width=terminal_width - 1):
            if colors > 8:
                formatted_text = dim(line)
            else:
                formatted_text = line
            log(formatted_text,
                colors=colors,
                verbosity=verbosity,
                stdout_verbosity_level=stdout_verbosity_level,
                log_file_verbosity_level=log_file_verbosity_level,
                log_file=log_file,
                print_to_screen=True,
                write_to_log_file=False)
    if write_to_log_file:
        log(text,
            colors=colors,
            verbosity=verbosity,
            stdout_verbosity_level=stdout_verbosity_level,
            log_file_verbosity_level=log_file_verbosity_level,
            log_file=log_file,
            print_to_screen=False,
            write_to_log_file=True)

    for _ in range(extra_empty_lines_after):
        log('',
            colors=colors,
            verbosity=verbosity,
            stdout_verbosity_level=stdout_verbosity_level,
            log_file_verbosity_level=log_file_verbosity_level,
            log_file=log_file,
            print_to_screen=print_to_screen,
            write_to_log_file=write_to_log_file)


def log_number_list(sample, numbers, verbosity=1, print_to_screen=True, write_to_log_file=True,
                    indent_size=4):
    """
    Some lists of numbers are long, so this function makes them wrap nicely when displayed on
    stdout.
    """
    text = ' ' * indent_size + ', '.join(str(x) for x in numbers)
    if print_to_screen:
        terminal_width = shutil.get_terminal_size().columns
        for line in textwrap.wrap(text, width=terminal_width - 1):
            sample.log(line, verbosity=verbosity, print_to_screen=True, write_to_log_file=False)
    if write_to_log_file:
        sample.log(text, verbosity=verbosity, print_to_screen=False, write_to_log_file=True)


def int_to_str(num, max_num=0):
    if num is None:
        num_str = 'n/a'
    else:
        num_str = '{:,}'.format(num)
    max_str = '{:,}'.format(int(max_num))
    return num_str.rjust(len(max_str))


def get_timestamp():
    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())


END_FORMATTING = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
YELLOW = '\033[93m'
DIM = '\033[2m'
RED = '\033[31m'
GREEN = '\033[32m'


def green(text):
    return GREEN + text + END_FORMATTING


def bold_green(text):
    return GREEN + BOLD + text + END_FORMATTING


def bold_red(text):
    return RED + BOLD + text + END_FORMATTING


def bold(text):
    return BOLD + text + END_FORMATTING


def bold_yellow_underline(text):
    return YELLOW + BOLD + UNDERLINE + text + END_FORMATTING


def dim(text):
    return DIM + text + END_FORMATTING


def remove_formatting(text):
    return re.sub('\033.*?m', '', text)


def remove_dim_formatting(text):
    return re.sub('\033\[2m', '', text)