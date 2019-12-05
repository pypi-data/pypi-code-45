import pandas as pd, sqlite3

class Sqldf:
    '''
    Wraps SQLite3 instance to streamline the SQL query to Pandas DataFrame process.

    Any DataFrames produced by this object are detached from the sqlite database (so
    mutating the df's will not have an effect on the source table)

    Warning: Can be slow with large database files. In such a case use the lite_load
    method inplace of the load method.


    Setup:

        from SQLPanda import load

        sdf = load("data.sqlite")
        #where data.splite is the SQLite DB file

    Main method examples:
        df = sdf.q("Select * from table_name")

        table_names = sdf.tables()

        df_head = sdf.head("table_name")

        df = sdf.__name_of_table_in_sqlite_db__

    '''
    def __init__(self,path):
        '''
        Ex./
            sdataframe = Sqldf("data.sqlite")
        '''
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.__table_names__ = []
        self.__add_tables__()
    prop = property(fget=lambda self:"Hi")
    def q(self,query):
        '''
        For general soft queries. Does not mutate database file, but will add changes to cursor.

        Parameters:
            query:
                SQL query as string
        Returns:
            Panda dataframe (empty if no respose).
        '''
        self.cursor.execute(query)
        fetched = self.cursor.fetchall()
        if self.cursor.description is not None:
            columns = [x[0] for x in self.cursor.description]
            if len(fetched) == 0:
                return pd.DataFrame(columns=columns)
            df = pd.DataFrame(fetched)
            df.columns = columns
            return df
    def tables(self):
        '''
        Returns:
            Panda series with all table names in DB.
        '''
        return self.q('Select name from sqlite_master where sqlite_master.type like \'table\'')
    def info(self):
        '''
        Returns:
            Pandas dataframe with all info from sqlite_master
        '''
        return self.q('Select * from sqlite_master')
    def head(self,table,length = 5):
        '''
        Similar to Pandas head method, but requires a table name.

        Parameters:
            table:
                table name as string
            length:
                count of rows to return
        Returns:
            Pandas dataframe of head of table
        '''
        return self.q(f'Select * from {table} limit {length}')
    def commit(self,query):
        '''
        Runs query and writes back all changes to database file.

        see Sqldf.q() for details
        '''
        df = self.q(query)
        self.connection.commit()
        self.__add_tables__()
        return df
    def __add_tables__(self):
        for table_name in self.__table_names__:
            del self.__dict__[table_name]
        self.__table_names__ = []
        for table_name in self.tables().name:
            self.__dict__[table_name] = self.__get_table__(table_name)
            self.__table_names__.append(table_name)
    def __get_table__(self,table_name):
        return self.q(f"select * from {table_name}")
