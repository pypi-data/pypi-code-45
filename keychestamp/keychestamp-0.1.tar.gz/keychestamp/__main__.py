#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module:
***

 Copyright (C) KeyChest Ltd, registered in the United Kingdom.
 This file is owned exclusively by KeyChest Ltd.
 Unauthorized copying of this file, via any medium is strictly prohibited
 Proprietary and confidential
 Written by Dan Cvrcek <support@keychest.net>, 2019
"""
import getopt
import logging
import multiprocessing
import signal
import sys
import time

from keychestamp.queue_handler import QueueHandler
from keychestamp.version import proxy_version

__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'


logger = logging.getLogger()
# logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.INFO)
# ch = logging.StreamHandler()
ch = QueueHandler()
fmt = logging.Formatter('%(asctime)s - %(name)s(Q) - %(levelname)s - %(message)s')
ch.setFormatter(fmt)
ch.setLevel(logging.INFO)
logger.addHandler(ch)


main_stop = multiprocessing.Event()
parent_group_pid = None


def print_help():
    """
    A simple help printing
    """
    print("keychestamp, version %s. (c) KeyChest Ltd. Visit https://gitlab.com/keychest .\n\n"
          "The proxy accepts the following parameters:" % proxy_version)
    print("  -h, --help - this help, if present it will stop the process\n")
    print("  -l  <DEBUG|ERROR|WARNING|INFO> - minimum level to log, default is INFO")
    print("  -r, --register - will attempt to create certification request(s)\n")
    print("  -p <port>, --port <port> - port where the proxy listens, 4001 if not set\n")
    print("  -p2 <port>, --port2 <port> - port where proxy's RESTful and WS server listens, 4443 if not set\n")
    print("  -k <path>, --keys <path> - location of keys for downstream RESTfull HTTPS (folder must contain files ")
    print("        'privkey.pem' and 'fullchain.pem' files in LetsEncrypt format; if not present, HTTP only\n")
    print("  -s http(s)://<url:port>|file://<path>|python://dummy> - address of the upstream server, e.g., ")
    print("        FoxyRest - http://upstream.cloudfoxy.com:8081 ; 'python://' will use an internal simulator\n")
    print("  -c <signer>, --signer <signer> - identification of the signature provider; currently supported are "
          "\"ICA\", \"PGP\"\n")
    print("  -t <token>, --token <token> - authorization token / API key for the signing API")


# noinspection PyUnusedLocal
def signal_handler(sig, frame):
    """
    Signal handler
    :param sig:
    :param frame:
    :return:
    """
    global beacon_thread
    global logger
    global ch
    global main_stop  # type: multiprocessing.Event()

    main_stop.set()
    beacon_thread.stopnow()
    ch.close()
    sys.stderr.write("Waiting 1 second to exit\n")
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    time.sleep(1)

    raise SystemExit('Terminating FoxyProxy')  # this is supposed to kill main()


def process_watch():
    """
    A simple process watch function that will try to close worker processes that died
    :return:
    """

    re_raise = False
    while True:
        time.sleep(10)
        logging.debug("watcher run started at %d" % int(time.time()))
        # noinspection PyBroadException
        try:
            pass
        except Exception:
            pass
        finally:
            logging.debug("watch run finished at %d" % int(time.time()))
            if re_raise:
                raise Exception("terminating process_watch")


def main():
    """
    Main entry function
    """

    # noinspection PyBroadException
    try:
        signal.signal(signal.SIGINT, signal_handler)
    except Exception:
        pass
    # noinspection PyBroadException
    try:
        signal.signal(signal.SIGTERM, signal_handler)
    except Exception:
        pass

    log_level = logging.INFO

    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hrp:s:t:c:l:',
                                       ['help', 'register', 'port=', 'server=', 'signer=', 'token=', 'level='])
        except getopt.GetoptError:
            # print help information and exit:
            print_help()
            print("You provided %s" % ' '.join(sys.argv[1:]))
            ch.close()
            sys.exit(2)

        for o, a in opts:
            if o in ('-h', '--help'):
                print_help()
                ch.close()
                sys.exit(0)
            else:
                if o in ('-r', '--register'):
                    register = True
                if o in ('-p', '--port'):
                    if a.isdigit():
                        foxyproxy_port = int(a)
                    else:
                        print("Invalid value of the port, it has to be a number")
                if o in ('-l', '--level'):
                    _a = ("%s" % a).lower()
                    if _a == 'debug':
                        log_level = logging.DEBUG
                    elif _a == 'info':
                        log_level = logging.INFO
                    elif _a == 'error':
                        log_level = logging.ERROR
                    elif _a == 'warning':
                        log_level = logging.WARNING

                if o in ('-p2', '--port2'):
                    if a.isdigit():
                        pass
                    else:
                        print("Invalid value of the port2, it has to be a number")
                if o in ('-s', '--server'):
                    upstream_server = a.strip()
                if o in ('-c', '--signer'):
                    signer_name = a.strip().lower()
                if o in ('-t', '--token'):
                    token = a.strip()
                if o in ('-k', '-keys'):
                    key_folder = a.strip()

    # alternative logbook logging
    # log_dispatcher_thread = LogDispatcher(logger_stop_event, ip="127.0.0.1")
    # log_dispatcher_thread.name = "LogDispatcher"
    # log_dispatcher_thread.start()

    # setup_logging(log_level, true_socket=True)  # alternative logbook logging
    logger.setLevel(log_level)


if __name__ == '__main__':
    try:
        main()
        sys.stderr.write("KeyChestAmp terminated\n")
        sys.stderr.flush()
    finally:
        pass
