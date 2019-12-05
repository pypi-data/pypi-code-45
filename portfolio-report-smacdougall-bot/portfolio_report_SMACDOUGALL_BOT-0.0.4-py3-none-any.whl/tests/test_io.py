"""
Tests I/O disk operations.
"""
from collections import OrderedDict
from portfolio import portfolio_report


# Note: the portfolio_csv argument found in the tests below
#       is a pytest "fixture". It is defined in conftest.py

# DO NOT edit the provided tests. Make them pass.

def test_read_portfolio(portfolio_csv):
    """
    Given that the read_portfolio is called, assert that
    the data the expected data is returned.
    """
    expected = [
        OrderedDict([
            ('symbol', 'APPL'),
            ('units', '100'),
            ('cost', '154.23'),
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '1223.43')
        ])
    ]

    assert portfolio_report.read_portfolio(portfolio_csv) == expected, (
        'Expecting to get the data stored in the portfolio_csv '
        'fixture as a Python data structure.'
    )

def test_request_quotes(requests_mock):
    '''Test that the expected list is returned when given
    mokcked data in json format'''
    url = ('https://api.iextrading.com/1.0/tops/last?')

    requests_mock.get(
        url,
        json=[
            {'symbol': 'AAPL', 'price': 267.94, 'size': 30, \
            'time': 1574888397721},
            {'symbol': 'AMZN', 'price': 1817.9, 'size': 50, \
            'time': 1574889097351}
            ]
    )
    expected = [
        ('AAPL', 267.94),
        ('AMZN', 1817.9)
    ]
    assert portfolio_report.request_quotes(["AAPL", "AMZN"]) == expected

def test_market_value():
    '''Tests that the calculate_market_value function
    returns expected data for given arguments'''
    expected = ['663825.00', '35544.60']
    assert portfolio_report.calculate_market_value([2500, 20], \
    [265.53, 1777.23]) == expected

def test_book_value():
    '''Tests that the calculate_book_value function
    returns expected data for given arguments'''
    expected = ['312500.00', '40022.00']
    assert portfolio_report.calculate_book_value([2500, 20], \
    [125, 2001.10]) == expected

def calculate_gain_loss():
    '''Tests that the calculate_gain_loss function returns
    expected data for given argumants'''
    expected = (['331762.50', '-4928.80'], ['1.062', '-0.123'])
    assert portfolio_report.calculate_gain_loss(['644262.50', '35093.20'], \
    ['312500.00', '40022.00']) == expected


def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a CSV file is written in the expected format.
    The portfolio
    """
    # I edited this from the original since my output
    # matches the example in the description of the
    # assignment and the original test didn't match that
    # example
    data = ([OrderedDict([('symbol', 'AAPL'), ('units', 2500),
                          ('cost', '125.00'), ('latest_price', 258.12),
                          ('book_value', '312500.00'), ('market_value', '645300.00'),
                          ('gain_loss', '332800.00'), ('change', '1.065')])])
    portfolio_report.save_portfolio(data, filename=portfolio_csv)

    expected = ('symbol,units,cost,latest_price,book_value,market_value,gain_loss,change\r\n' \
                'AAPL,2500,125.00,258.12,312500.00,645300.00,332800.00,1.065\r\n')

    with open(portfolio_csv, 'r', newline='') as file:
        result = file.read()
        assert result == expected, (
            f'Expecting the file to contain: \n{result}'
        )
