
# TODO: use shebang statement

import mysql.connector
import argparse


# TODO: separate functions for different tasks

# TODO: parse_args() - should return the parsed arguments
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
f = args.file.readlines()
print(f)

# TODO: separate function to handle connection creation - can return connection/cursor
mydb = mysql.connector.connect(host ="localhost", user="root", passwd ="Gemini@123", database ="test_divyanshi")
mycursor = mydb.cursor()

# TODO: separate function for inserting records - should take cursor, query and records to insert
for i in range(len(f)):
    sql = " insert into employee_info (id,name,dept,salary) values (%s,%s,%s,%s)"
    arr = f[i].split(',')
    val = (int(arr[0]),arr[1],arr[2],int(arr[3]))
    mycursor.execute(sql,val)
    mydb.commit()

# TODO: Separate function to fetch results from database - should take cursor and query and return the result
mycursor.execute("select * from employee_info")
myresult = mycursor.fetchall()
for v in myresult:
    print(v)


# TODO: You forgot to close the database connection
# In case of resource acquisition and release we should ensure the proper acquiring and release of resource, in this case database connection
