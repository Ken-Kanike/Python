import mysql.connector  as c
import json

# Load the JSON file
with open('data.json', 'r') as file:
    config = json.load(file)

# Access the passwords
db_password = config.get("db_password")

con  = c.connect(host='localhost', user='root', passwd=db_password, database='demodb')
if con.is_connected():
    print("Connection successful!")
else :
    print("Connection failed!")