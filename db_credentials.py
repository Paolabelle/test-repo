from variables import datawarehouse_name

# mysql (target db, datawarehouse)
datawarehouse_db_config = [
  {
    'user': 'root',
    'password': '2275',
    'host': 'localhost',
    'database': 'classicmodels',
  }
]

# mysql (source db)
mysql_db_config = [
  {
    'user': 'root',
    'password': '2275',
    'host': 'localhost',
    'database': 'classicmodels',
  }
]

# sql-server (target db, datawarehouse)
#datawarehouse_db_config = {
#  'Trusted_Connection': 'yes',
#  'driver': '{SQL Server}',
#  'server': 'datawarehouse_sql_server',
#  'database': '{}'.format(datawarehouse_name)
#  'user': 'your_db_username',
#  'password': 'your_db_password',
#  'autocommit': True,
#}

# sql-server (source db)
#sqlserver_db_config = [
#  {
#    'Trusted_Connection': 'yes',
#    'driver': '{SQL Server}',
#    'server': 'your_sql_server',
#    'database': 'db1'
#    'user': 'your_db_username',
#    'password': 'your_db_password',
#    'autocommit': True,
# }
#]


# firebird
#fdb_db_config = [
#  {
#    'dsn': "/your/path/to/source.db",
#    'user': "your_username",
#    'password': "your_password",
#  }
#]
