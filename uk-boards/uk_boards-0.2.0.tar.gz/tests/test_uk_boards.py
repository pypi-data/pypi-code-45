#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `uk_boards` package."""

import pytest

from click.testing import CliRunner

# from uk_boards import uk_boards
from uk_boards import cli

CORRECT_HELP = """\
Options:
  -i, --indent INTEGER  How many spaces to indent printing json queries.
                        [default: 2]
  --help                Show this message and exit.

Commands:
  company            Query Companies House by company number.
  csv-organisations  Path to csv with company and charity numbers."""


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert CORRECT_HELP in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert CORRECT_HELP in help_result.output
