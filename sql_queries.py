mysql_extract = (''' 
	SELECT products.productCode, products.productName, products.productLine, products.productScale, products.productVendor,
    products.productDescription, products.quantityInStock, products.buyPrice, products.MSRP  FROM classicmodels.products;
''')

mysql_insert = ('''
	INSERT INTO employees.products2 VALUES (?,?,?,?,?,?,?,?,?)
''')

# exporting queries
class SqlQuery:
  def __init__(self, extract_query, load_query):
    self.extract_query = extract_query
    self.load_query = load_query
    
# create instances for SqlQuery class
mysql_query = SqlQuery(mysql_extract, mysql_insert)

# store as list for iteration
mysql_queries = [mysql_query]