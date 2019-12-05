import os
import re
import click


def email(ctx, param, value):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
        raise click.UsageError('Incorrect email address given')
    else:
        return value


def _to_email(value):
    if os.path.isfile(value):
        return value
    return email(None, None, value)


def emails(ctx, param, value):
    return map(_to_email, value)


def content(ctx, param, value):
    if os.path.isfile(value):
        return value
    return value
