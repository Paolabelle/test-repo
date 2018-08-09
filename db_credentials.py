from variables import datawarehouse_name

# mysql (target db, datawarehouse)
datawarehouse_db_config = {
	'user': 'root',
    'password': '2275',
    'host': 'localhost',
    'database': 'classicmodels',
}

# mysql (source db)
source_db_config = {
	'user': 'root',
    'password': '2275',
    'host': 'localhost',
    'database': 'employees',
}