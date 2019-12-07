
import argparse
import re
import pathlib

consumer_key_re = re.compile(r'([a-zA-Z1-9]+)')
consumer_secret_re = re.compile(r'([a-zA-Z1-9]+)')
access_token_key_re = re.compile(r'([0-9]+-[a-zA-Z1-9]+)')
access_token_secret_re = re.compile(r'([a-zA-Z1-9]+)')

protection_tag_re = re.compile(r'(\[[\w]+\])')


def validate_unsigned_int_non_zero(value):
    if isinstance(value, int) and value > 0:
        return value
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid alue. Must be int and bigger than 0 (current value {value})"
        )


def validate_consumer_key(token):
    if consumer_key_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer key token -> {token}"
        )


def validate_consumer_secret(token):
    if consumer_secret_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token}"
        )


def validate_access_token_key(token):
    if access_token_key_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token}"
        )


def validate_access_token_secret(token):
    if access_token_secret_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token}"
        )


def validate_protection_tag(protection_tag):
    if protection_tag_re.match(protection_tag):
        return protection_tag
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid protection tag -> {protection_tag} - Can only contain alphabetic or numeric values and have the format [customTag]."
        )


def validate_directory_attribute(directory_location):
    if type(directory_location) is str:
        directory_location = pathlib.Path(directory_location)
        if directory_location.exists():
            if directory_location.is_dir():
                return directory_location
            else:
                raise argparse.ArgumentTypeError(
                    "Directory location must point to a directory"
                )
        else:
            raise argparse.ArgumentTypeError(
                "Directory location must exist."
            )

    raise argparse.ArgumentTypeError(
        f"Invalid directory attribute -> {directory_location}. Must be a valid directory location."
    )


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--logLevel",
        help="Logging Level (default: %(default)s)",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO"
    )

    parser.add_argument(
        "-d", "--days",
        help="Tweets older than %(default)d days (default value)",
        type=validate_unsigned_int_non_zero,
        default=0
    )

    parser.add_argument(
        "-m", "--months",
        help="Tweets older than %(default)d months (default value)",
        type=validate_unsigned_int_non_zero,
        default=1
    )

    parser.add_argument(
        "-y", "--years",
        help="Tweets older than %(default)d years (default value)",
        type=validate_unsigned_int_non_zero,
        default=0
    )

    parser.add_argument(
        "-t", "--protection_tag",
        help="Protection Tag (default: %(default)s)",
        type=validate_protection_tag,
        default="[P]"
    )

    parser.add_argument(
        "-f", "--saving_directory",
        help="Directory location to where deleted tweets are exported (default: %(default)s)",
        type=validate_directory_attribute,
        default=None
    )

    parser.add_argument(
        "-ck", "--consumer_key",
        help="Consumer Key",
        required=True,
        type=validate_consumer_key
    )

    parser.add_argument(
        "-cs", "--consumer_secret",
        help="Consumer Secret",
        required=True,
        type=validate_consumer_secret
    )

    parser.add_argument(
        "-tk", "--token_key",
        help="Access Token Key",
        required=True,
        type=validate_access_token_key
    )

    parser.add_argument(
        "-ts", "--token_secret",
        help="Access Token Secret",
        required=True,
        type=validate_access_token_secret
    )

    return parser.parse_args()
