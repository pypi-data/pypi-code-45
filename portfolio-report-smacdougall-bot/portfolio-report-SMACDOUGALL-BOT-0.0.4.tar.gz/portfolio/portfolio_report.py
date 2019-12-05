#pylint: disable-msg=too-many-arguments

"""
Generates performance reports for your stock portfolio.
"""
from collections import OrderedDict
import argparse
import csv
import requests


def main():
    """
    Entrypoint into program.
    """
    # collect arguments included when script is run
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help= \
        "The input csv file containing your portfolio details")
    parser.add_argument("target", help= \
        "The output csv file to which the report will be saved")
    args = parser.parse_args()
    # read the file that includes our portfolio list
    portfolio_list = read_portfolio(args.source)
    # define some lists
    symbols = []
    units = []
    costs = []
    # append the values from our portfolio into the lists we created above
    for row in portfolio_list:
        symbols.append(row['symbol'])
        units.append(int(row['units']))
        costs.append(float(row['cost']))
    # get the latest quotes using the symbols we extracted from the portfolio
    quotes = request_quotes(symbols)
    # extract the price from the tuple that's returned
    latest_prices = [x[1] for x in quotes]
    # calculate values and changes
    market_values = calculate_market_value(units, latest_prices)
    book_values = calculate_book_value(units, costs)
    gain_loss, change = calculate_gain_loss(market_values, book_values)
    # create a list of dictonaries of everything we've done so far
    data = create_dictionary(symbols, units, costs, latest_prices, book_values, \
                      market_values, gain_loss, change)
    # pass the dictionary to the save_portfolio function to write a
    # csv file
    save_portfolio(data, args.target)



def read_portfolio(filename):
    """Returns data from a CSV file"""
    with open(f'{filename}', newline='') as file:
        csv_reader = csv.DictReader(file)
        portfolio_list = []
        for row in csv_reader:
            portfolio_list.append(row)
        return portfolio_list


def request_quotes(symbols):
    '''Gets quotes from IEX using the portfolio read in from a
    csv file'''
    payload = {'symbols': ','.join(symbols)} # this fornmats the payload to what's expected
    response = requests.get('https://api.iextrading.com/1.0/tops/last?', \
        payload)
    data = response.json() # convert data to python
    return [
        (item['symbol'], item['price'])
        for item in data
    ]

def calculate_market_value(units, price):
    '''Calculates the curent market value based on the number
    of units in our portfolio and the current price retrieved
    earlier in the request_quotes function'''
    market = []
    length = len(units)
    for  index in range(length):
        # perform the math on the numbers, but then return a string
        # with the correct number of decimals
        market.append('{:.2f}'.format(round(units[index] * price[index], 2)))
    return market


def calculate_book_value(units, cost):
    '''Calculates the book value of our portfolio from the number
    of units held and the original price of those units'''
    book = []
    length = len(units)
    for index in range(length):
        # perform the math on the numbers, but then return a string
        # with the correct number of decimals
        book.append('{:.2f}'.format(round(units[index] * cost[index], 2)))
    return book

def calculate_gain_loss(market, book):
    '''Calculates the gain or loss of our holdings in both a
    dollar value and percentage'''
    gain_loss = []
    change = []
    length = len(market)
    for index in range(length):
        # perform the math on the numbers, but then return a string
        # with the correct number of decimals
        gain_loss.append('{:.2f}'.format(round(float((market[index])) - float((book[index])), 2)))
        change.append('{:.3f}'.format(round(float((gain_loss[index])) / float((book[index])), 3)))
    return gain_loss, change

def create_dictionary(symbols, units, costs, latest_prices, book_values, \
market_values, gain_loss, change):
    '''Creates a list of dictionaries of everything we've done
    up to now'''
    length = len(symbols)
    data = []
    for i in range(length):
        data.append(OrderedDict([('symbol', symbols[i]),
                                 ('units', units[i]),
                                 ('cost', '{:.2f}'.format(costs[i])),
                                 ('latest_price', latest_prices[i]),
                                 ('book_value', book_values[i]),
                                 ('market_value', market_values[i]),
                                 ('gain_loss', gain_loss[i]),
                                 ('change', change[i])]))
    return data

def save_portfolio(data, filename):
    """Saves data to a CSV file"""
    with open(f'{filename}', 'w', newline='')as file:
        writer = csv.DictWriter(file, ['symbol', 'units', 'cost', \
        'latest_price', 'book_value', 'market_value', 'gain_loss', 'change'])
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()
