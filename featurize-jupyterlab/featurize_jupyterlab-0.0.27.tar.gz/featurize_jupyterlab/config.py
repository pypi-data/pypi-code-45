from sqlalchemy import create_engine
import os


class Config:
    if os.environ.get('FENV', None) == 'test':
        engine = create_engine('postgresql+psycopg2://featurize:featurize@localhost:5432/luoge')
    else:
        engine = create_engine('postgresql+psycopg2://postgres:postgres@demo.featurize.ai:6777/postgres')

    server_proto = 'http://'
    server_addr = '127.0.0.1'
    server_port = 8888
    rpc_port = '6725'
