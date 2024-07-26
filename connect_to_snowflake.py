import snowflake.connector
import os
# Define connection parameters
account = 'XXXXX'
user = 'VIVEKSTARK'
password = 'PWD'
warehouse = 'AIRBNB'
database = 'TABLES'
schema = 'PROJECT'

# Print the values to debug
print(f"Account: {account}")
print(f"User: {user}")
print(f"Password: {password}")
print(f"Warehouse: {warehouse}")
print(f"Database: {database}")
print(f"Schema: {schema}")

# Establish the connection
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT CURRENT_VERSION()")

# Fetch and display the result
result = cur.fetchone()
print(result)

# Close the cursor and connection
cur.close()
conn.close()
