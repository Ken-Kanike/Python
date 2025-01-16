import mysql.connector  as c
import json

# Load the JSON file
with open(r'PyMySQL\data.json', 'r') as file:
    config = json.load(file)

# Access the passwords
db_password = config.get("db_password")

con  = c.connect(host='localhost', user='root', passwd=db_password, database='pydb')
if con.is_connected():
    print("Connection successful!")
    # pydb already exists , and demo table with int(id) , varchar(name) and int(code) created..

cursor = con.cursor()

while True:
    choice = input("Enter your choice (1-Insert, 2-Select, 3-Exit): ")

    if choice == '1':
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        code = int(input("Enter code: "))
        InsertQuery = "INSERT INTO demo VALUES('{}', '{}', '{}')".format(id, name, code)
        cursor.execute(InsertQuery)
        con.commit()
    
    elif choice == '2':
        SelectQuery = 'SELECT * FROM demo'
        cursor.execute(SelectQuery)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == '3':
        break
    




