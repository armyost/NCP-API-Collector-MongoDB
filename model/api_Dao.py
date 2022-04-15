from sqlalchemy import text

class apiDao:
    def __init__(self, database):
        collection = database.testdb.getServerInstanceList
        self.db=collection

    def insert_data_serverInstance(self, row):
        self.db.insert_one(row)