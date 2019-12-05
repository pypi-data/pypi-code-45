from SQLPanda.BigPanda.bigpanda import Sqldf
from SQLPanda.LitePanda.litepanda import LiteSqldf

def load(table_name):
    '''
    Convinience method for creating Sqldf
    '''
    return Sqldf(table_name)
def lite_load(table_name):
    '''
    Convinience method for creating Sqldf with a lite backend
    '''
    return LiteSqldf(table_name)
