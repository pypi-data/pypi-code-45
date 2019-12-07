import signal
import subprocess
import time

from utils import utils


class Stan:

    def __init__(self, time, command):
        self.time = time
        self.command = command

    def broken_alarm(self):
        time.sleep(self.time)

    def register_signals(self):
        signal.signal(signal.SIGINT, utils.signal_handler)

    def answer(self):
        if self.command == ['']:
            print("[STAN] Attends, j'appelle Bruno !")
            print('[BRUNO] ', end='')
            utils.bruno()
        else:
            subprocess.run(self.command)

    def run(self):
        self.register_signals()
        self.broken_alarm()
        self.answer()
