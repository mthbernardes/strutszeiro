import os
from pydal import DAL, Field

class database(object):
    def __init__(self,):
        pass
    def __new__(self,):
        dbPath = os.path.abspath(os.path.join('data','storage.db'))
        path = 'sqlite://{0}'.format(dbPath)
        migrate = True
        if os.path.exists(dbPath):
            migrate = False
        db = DAL(path,migrate=migrate)
        db.define_table('servers',Field('url'))
        return db

if __name__ == '__main__':
    db = database()
