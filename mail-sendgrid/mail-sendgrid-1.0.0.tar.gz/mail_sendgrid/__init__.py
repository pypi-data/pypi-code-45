#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import click_log
import logging
import sys
import os
import base64
import jinja2
import yaml
import sendgrid
from sendgrid.helpers.mail import *
from . import validate


__version__ = '1.0.0'


def _update(label, emails, fce):
    for email in emails:
        if os.path.isfile(email):
            with open(email, 'r') as fd:
                for line in fd:
                    line = line.strip()
                    if not line:
                        continue
                    logging.debug('%s: %s', label, line)
                    fce(Email(line))
        else:
            logging.debug('%s: %s', label, email)
            fce(Email(email))


@click.command()
@click.option('-f', '--from', "from_email", metavar="EMAIL",
              help='Email address to send from.',
              callback=validate.email,
              required=True)
@click.option('-t', '--to', "to_emails", metavar="EMAIL/FILE",
              help='Email address or file with address, recipient to receive of this email.  [multiple]',
              callback=validate.emails,
              multiple=True,
              required=True)
@click.option('--cc', "cc_emails", metavar="EMAIL/FILE",
              help='Email address or file with address, recipient to receive a copy of this email.  [multiple]',
              callback=validate.emails,
              multiple=True)
@click.option('--bcc', "bcc_emails", metavar="EMAIL/FILE",
              help='Email address or file with address, recipient to receive a blind carbon copy of this email.  [multiple]',
              callback=validate.emails,
              multiple=True)
@click.option('-s', '--subject', metavar="SUBJECT",
              help='Email subject.',
              required=True)
@click.option('-c', '--content', metavar="TEXT/FILE",
              help='Email content, support jinja2 template.',
              callback=validate.content,
              required=True)
@click.option('-a', '--attachment', 'attachment_files', metavar="FILE",
              type=click.Path(exists=True, dir_okay=False),
              help='Email attachment.  [multiple]', multiple=True)
@click.option('--var', 'variable', metavar="KEY VALUE",
              type=(str, str),
              help='Jinja2 template variable.  [multiple]', multiple=True)
@click.option('--variable-yaml', 'variables_files', metavar="FILE",
              type=click.Path(exists=True, dir_okay=False),
              help='Jinja2 template variables in YAML format. [multiple]', multiple=True)
@click.option('--nl2br', is_flag=True, help='Replace all new line with br tag.')
@click.option('--no-send', is_flag=True, help='Skip send, print rendered content.')
@click.option('--apikey', envvar="SENDGRID_API_KEY", metavar="APIKEY",
              help='Sendgrid api key or use env: SENDGRID_API_KEY.',
              required=True)
@click.version_option(version=__version__)
@click_log.simple_verbosity_option(default='INFO')
def cli(from_email, to_emails, cc_emails, bcc_emails, subject, content, attachment_files, variable, variables_files, nl2br, no_send, apikey):
    '''Cli tool for send mail over sendgrid.'''

    mail = Mail()
    mail.from_email = from_email

    personalization = Personalization()

    _update('Email to', to_emails, personalization.add_to)
    _update('Email cc', cc_emails, personalization.add_cc)
    _update('Email bcc', bcc_emails, personalization.add_bcc)

    mail.add_personalization(personalization)

    logging.debug('Subject: %s', subject)
    mail.subject = subject

    for filename in attachment_files:
        logging.debug('Attachment: %s', filename)
        attachment = Attachment()
        attachment.content = base64.b64encode(open(filename, 'rb').read()).decode()
        attachment.filename = filename
        attachment.disposition = "attachment"
        attachment.content_id = os.path.basename(filename)
        mail.add_attachment(attachment)

    if os.path.isfile(content):
        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template(content)
    else:
        template = jinja2.Template(content)

    variables = {}

    for filename in variables_files:
        with open(filename, 'r') as fd:
            variables.update(yaml.safe_load(fd))

    for k, v in variable:
        variables[k] = v

    content = template.render(**variables)

    if nl2br:
        content = content.replace('\n', '<br />\n')

    logging.debug('Content: %s', content)

    mail.add_content(Content("text/html", content))

    if no_send:
        print(content)
    else:
        sg = sendgrid.SendGridAPIClient(apikey=apikey)
        sg.client.mail.send.post(request_body=mail.get())
        click.echo('Email was send')


def main():
    try:
        logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s')
        cli()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
        click.echo('Email not send')
        sys.exit(1)


if __name__ == '__main__':
    main()
