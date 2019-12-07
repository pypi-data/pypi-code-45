#!/usr/bin/env python3

import signal
import subprocess
import sys
import time


def bruno():
    print('Va voir ce que dit le standard CPP17 : http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/n4713.pdf')


def signal_handler(signum, frame):
    print(f'[STAN] Désolé mon réveil était cassé...')
    return


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


def main():
    Stan(4 * 60 * 60, sys.argv[1:] if len(sys.argv) > 1 else ['']).run()


if __name__ == '__main__':
    main()
