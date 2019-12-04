import tushare as ts
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--code', '-c', required=True, default='600519', type=str, help='stock code .eg. 600519')
@click.option('--date', '-d', required=True, default='2019-10-10', type=str, help='date .eg. 2019-10-10')
def get_tick_data(code, date):
    if len(code)==9:
        code=code[:6]
    return ts.get_tick_data(code, date, src='tt')
