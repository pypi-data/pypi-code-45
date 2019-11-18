'''
Stopped training alerting script.
'''
__author__ = 'Jakub Langr'
import subprocess
import sentry_sdk
import datetime
import os
from sentry_sdk import capture_exception, capture_message
from argparse import ArgumentParser
import sys
import subprocess as sp
import traceback

def initialize(overwrite=False):
    global config
    script_location = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(script_location)
    try:
        import perses_config as config
    except ModuleNotFoundError:
        if not os.path.exists(f"{script_location}/perses_config.py") or overwrite:
            print('Config does not exist. Please enter the commands.')
            exec_file = input('Enter the file to run: ')
            defaults = input("Please set default flags: ")
            sentry_sdn = input("Enter the Sentry SDN: ")
            with open(f"{script_location}/perses_config.py","w+") as f:
                f.write(f"exec_file = \'{exec_file}\' \n")
                f.write(f"defaults = \'{defaults}\' \n")
                f.write(f"sentry_sdn = \'{sentry_sdn}\' \n")

            import perses_config as config
        else:
            raise Exception('Missing config & cannot create one.')


    # variables to set
    now_str = str(datetime.datetime.now())[:-7].replace(' ','_')
    log_file = f'cli_output/{config.exec_file}_{now_str}.txt'

    # uses the current python env
    os.environ['BETTER_EXCEPTIONS'] = "1"

    # makes sure the file above exists
    # open(log_file, 'a').close()

    # This should be eventually grabbed from ENV or something.
    sentry_sdk.init(config.sentry_sdn)


def tracking(flags: str, testing: bool, no_shutdown: bool, base_py: str):
    start_time = datetime.datetime.now()
    initialize()
    FLAGS = config.defaults + flags

    shutdown_hours = [22, 23] + list(range(0,8))

    if not base_py:
        py_path = sp.run(['which','python3'], stdout=sp.PIPE)
        base_py = py_path.stdout.decode()[:-1]
        
    # e.g. command = f'{base_py} train.py {FLAGS} 2>> {log_file}'
    # alt command = f'{base_py} train.py {FLAGS} 2>&1 | tee {log_file}'
    command = f'{base_py} {config.exec_file} {FLAGS}'

    try:
        print(f'Starting tracking, running command: \n {command}')
        output = subprocess.run(
            command, shell=True, check=True) 
        # print(output.stderr)
    # except subprocess.CalledProcessError as exc:
    #     print("Status : FAIL", exc.returncode, exc.output)
    #     capture_exception(exc)
    except Exception as e:
        # TODO: actually check if this works.
        capture_message('Program exited, Output: \n{}'.format(e))
        traceback.print_exc(e)
        # TODO: don't shut down if Keyboard interrupt
        print("Program exited.")
        run_time = datetime.datetime.now() - start_time 
        time_checks = run_time.total_seconds() < 60 and datetime.datetime.now().hour in shutdown_hours
        if not no_shutdown and time_checks:
            capture_message('It is also late. Shutting down the instance.')
            os.system('sudo shutdown now')

def test_sentry():
    initialize()
    inst_private_ip = os.environ["SSH_CONNECTION"].split()[2]
    capture_message(f"A test if sentry can work from private IP: \
        {inst_private_ip}")

