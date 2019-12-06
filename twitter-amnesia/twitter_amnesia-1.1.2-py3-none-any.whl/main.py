"""
Twitter Amnesia

A service which can be deployed to erase tweets older than a specific date and not marked with a custom tag
"""

import logging
import sys
import datetime
from datetime import *
import pickle

import twitter
from dateutil.relativedelta import *
from dateutil import parser

from twitter_amnesia.helpers import custom_logging_callback, logger_module_name
from twitter_amnesia.arg_parsing import parse_arguments

# Initialize Exception Hook
sys.excepthook = (lambda tp, val, tb: custom_logging_callback(logging.getLogger(), logging.ERROR, tp, val, tb))


# Initialize logger for this module
__log_format = '[{asctime:^s}][{levelname:^8s}]: {message:s}'
__log_format_debug = '[{asctime:^s}][{levelname:^8s}][{name:s}|{funcName:s}|{lineno:d}]: {message:s}'
__log_datefmt = '%Y/%m/%d|%H:%M:%S (%Z)'
__log = logging.getLogger(logger_module_name(__file__))


def main():
    try:
        parsed_args = parse_arguments()
        if sys.flags.debug:
            logging.basicConfig(format=__log_format_debug, datefmt=__log_datefmt, style='{', level=logging.DEBUG)
        else:
            logging.basicConfig(format=__log_format, datefmt=__log_datefmt, style='{', level=parsed_args.logLevel)

        if sys.flags.debug:
            __log.debug(
                ''.join(['CLI arguments: ']+list(
                                ('  {:s}: {:s}'.format(
                                    str(key), str(data)
                                ) for (key, data) in vars(parsed_args).items())
                            )
                        )
            )

        date_until = datetime.now() - relativedelta(
            days=parsed_args.days,
            months=parsed_args.months,
            years=parsed_args.years
        )

        __log.warning(
            "Tweets created before {:s} will be deleted.".format(date_until.strftime("%Y-%m-%d"))
        )

        api = twitter.Api(
            consumer_key=parsed_args.consumer_key,
            consumer_secret=parsed_args.consumer_secret,
            access_token_key=parsed_args.token_key,
            access_token_secret=parsed_args.token_secret,
            sleep_on_rate_limit=False
        )
        this_user_credentials = api.VerifyCredentials()
        __log.info(
            f"Name: {this_user_credentials.name:s}; Screen Name: {this_user_credentials.screen_name:s}"
        )
        removed_tweets_counter = 0

        statuses = api.GetUserTimeline(trim_user=True, count=1)
        if len(statuses):
            __log.info("Retrieving first status in timeline")
        while len(statuses):
            max_id = statuses[-1].id
            for status in statuses:
                if parsed_args.protection_tag in status.text[0:len(parsed_args.protection_tag)]:
                    __log.info(f"Tweet with ID {status.id:d} skipped. Protection tag present.")
                    continue
                elif date_until.astimezone() <= parser.parse(status.created_at).astimezone():
                    __log.info(f"Tweet with ID {status.id:d} skipped. Not old enough to be removed.")
                    continue
                else:
                    if parsed_args.saving_directory:
                        __log.info(f"Saving tweet with ID {status.id:d}.")
                        with open(f"{parsed_args.saving_directory}/{status.id:d}", "wb") as file:
                            pickle.dump(status.AsDict(), file)

                    api.DestroyStatus(status.id)
                    removed_tweets_counter += 1
                    __log.warning(f"Tweet {status.id:d} deleted.")
            statuses = api.GetUserTimeline(trim_user=True, max_id=max_id-1, count=200)
        __log.info(f"Total number of deleted tweets: {removed_tweets_counter:d}.")

    except Exception:
        custom_logging_callback(__log, logging.ERROR, *sys.exc_info())
        exit(-1)

    __log.info("It's done!")
    exit(0)


if __name__ == '__main__':
    main()
