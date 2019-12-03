import pymongo


def connMongo(dbName=None, connName=None, ip='127.0.0.1', port=27017, authen=False, user=None, pwd=None):
    '''
    :param ip:
    :param port:
    :param dbName:
    :param connName:
    :return:
    '''
    if dbName is None or connName is None:
        raise TypeError('input your dbName and connName')
    if authen:  # 认证
        if user is None or pwd is None:
            raise NameError('input your user and pwd')
        myclient = pymongo.MongoClient("mongodb://{}:{}@{}:{}/".format(user, pwd, ip, port))
    else:
        myclient = pymongo.MongoClient("mongodb://{}:{}/".format(ip, port))
    mydb = myclient[dbName]
    mycol = mydb[connName]
    return mycol


if __name__ == '__main__':
    mycol = connMongo('student', 'student', authen=True, user='admin', pwd='123456', ip='192.168.0.2')
    counts = mycol.find()
