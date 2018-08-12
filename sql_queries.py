# example equiries, will be different across different db platforms

mysql_extract = (''' 
	SELECT products.productCode, products.productName, products.productLine, products.productScale, products.productVendor,
    products.productDescription, products.quantityInStock, products.buyPrice, products.MSRP  FROM classicmodels.products;
''')

mysql_insert = ('''
	INSERT INTO employees.products2(productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES (?,?,?,?,?,?,?,?,?);
''')

# exporting queries
class SqlQuery:
  def __init__(self, extract_query, load_query):
    self.extract_query = extract_query
    self.load_query = load_query
    

# create instances for SqlQuery class
#fbd_query = SqlQuery(firebird_extract, firebird_insert)
#fbd_query_2 = SqlQuery(firebird_extract_2, firebird_insert_2)
#sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)
mysql_query = SqlQuery(mysql_extract, mysql_insert)

# store as list for iteration
#fbd_queries = [fbdquery, fbd_query_2]
#sqlserver_queries = [sqlserver_query]
mysql_queries = [mysql_query]