install = []
import os
import sys
import time

try: from colorama import Fore, init
except: install.append("colorama")

# Trying to install the needed modules if there not already
if install:
    to_install = " ".join(install)
    os.system(sys.executable + " -m pip install " + to_install)
    print("[STARTUP] INSTALLED MODULES: "+str(install))
    quit()

# colors!
init()

################## Functions ######################################
def warn(text: str):
    print("["+Fore.YELLOW+"WARN"+Fore.RESET+"] "+str(text))

def error(text: str):
    print("["+Fore.RED+"ERROR"+Fore.RESET+"] "+str(text))
    
def done_task(text: str):
    print("["+Fore.GREEN+"DONE"+Fore.RESET+"] "+str(text))

def info(text: str):
    print("["+Fore.WHITE+"INFO"+Fore.RESET+"] "+str(text))

def critical(text: str):
    print("["+Fore.RED+"CRITICAL"+Fore.RESET+"] "+str(text))
    quit()

def logo(lines: list, Fore_Color = Fore.WHITE):
    for line in lines:
        print(Fore_Color+line)
        time.sleep(0.1)
    print(Fore.RESET)
################## END LOGGING ###################################
