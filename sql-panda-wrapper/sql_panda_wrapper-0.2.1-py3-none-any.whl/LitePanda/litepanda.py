from SQLPanda.BigPanda.bigpanda import Sqldf

class LiteSqldf(Sqldf):
    '''
    Gets rid of table loading to improve performance and loosing loaded table feature

    Setup:

        from SQLPanda import lite_load

        sdf = lite_load("data.sqlite")
        #where data.splite is the SQLite DB file
    '''
    def __add_tables__(self):
        '''
        Removes the sqlite table loading process which can be computaionally/spacially expensive
        '''
        pass
