#!/usr/bin/env python3

import signal
import subprocess
import sys
import time

from utils import bruno, signal_handler


class Stan:

    def __init__(self, time, command):
        self.time = time
        self.command = command

    def broken_alarm(self):
        time.sleep(self.time)

    def register_signals(self):
        signal.signal(signal.SIGINT, signal_handler)

    def answer(self):
        if self.command == ['']:
            print("[STAN] Attends, j'appelle Bruno !")
            print('[BRUNO] ', end='')
            bruno()
        else:
            subprocess.run(self.command)

    def run(self):
        self.register_signals()
        self.broken_alarm()
        self.answer()


if __name__ == '__main__':
    Stan(5, sys.argv[1:] if len(sys.argv) > 1 else ['']).run()
