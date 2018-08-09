# variables
from db_credentials import datawarehouse_db_config, source_db_config
from sql_queries import mysql_queries
from variables import *
import mysql.connector

# methods
from etl import etl_process

def main():
	print('starting etl')
	
# establish connection for target database (mysql)
target_cnx = mysql.connector.connect(**datawarehouse_db_config)

# loop through credentials

# mysql
##for config in source_db_config:
##	try:
##		print("loading db:" + config('database')
##	etl_process(queries, target_cnx, source_db_config, db_platform)
##	except Exception as error:
##		print("etl for {} has error".format(config['database'])
##		print('error message: {}format(error))
##		continue
		
etl_process(mysql_queries, target_cnx, source_db_config, 'mysql')
		
if __name__ == "__main__":
	main()