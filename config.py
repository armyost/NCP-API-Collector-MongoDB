## Prod Config 입력

db = {			
    'user'     : 'root',
    'password' : 'root',
    'host'     : 'localhost',
    'port'     : 3306,
    'database' : 'test_db'
}

DB_URL = 'mongodb://testuser:testuser@localhost/testdb'
ACCESS_KEY = '엑세스키 입력'
SECRET_KEY = '스크릿키 입력'


## Dev Config 입력

test_db = {			
    'user'     : 'testuser',
    'password' : 'testuser',
    'host'     : 'localhost',
    'port'     : 27017,
    'database' : 'testdb',
}

dev_config = {		
    'DB_URL' : f"mongodb://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}",
    'ACCESS_KEY' : '엑세스키 입력',
    'SECRET_KEY' : '시크릿키 입력'
}