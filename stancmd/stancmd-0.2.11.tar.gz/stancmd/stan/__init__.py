import signal
import subprocess
import time


class Stan:

    def __init__(self, time, command):
        self.time = time
        self.command = command

    def broken_alarm(self):
        time.sleep(self.time)

    def register_signals(self, sig_handler):
        signal.signal(signal.SIGINT, sig_handler)

    def answer(self, answer):
        if self.command == ['']:
            print("[STAN] Attends, j'appelle Bruno !")
            print('[BRUNO] ', end='')
            answer()
        else:
            subprocess.run(self.command)

    def run(self, sig_handler, answer):
        self.register_signals(sig_handler)
        self.broken_alarm()
        self.answer(answer)
