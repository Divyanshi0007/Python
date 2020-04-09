import mysql.connector
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
f = args.file.readlines()
print(f)

mydb = mysql.connector.connect(host ="localhost", user="root", passwd ="Gemini@123", database ="test_divyanshi")
mycursor = mydb.cursor()

for i in range(len(f)):
    sql = " insert into employee_info (id,name,dept,salary) values (%s,%s,%s,%s)"
    arr = f[i].split(',')
    val = (int(arr[0]),arr[1],arr[2],int(arr[3]))
    mycursor.execute(sql,val)
    mydb.commit()

mycursor.execute("select * from employee_info")
myresult = mycursor.fetchall()
for v in myresult:
    print(v)