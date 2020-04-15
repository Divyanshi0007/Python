
# TODO: use shebang statement

import mysql.connector

# TODO: separate functions for different tasks
# TODO: comments similar to the comments mentioned in argparseexample.py

mydb = mysql.connector.connect(host ="localhost", user="root", passwd ="Gemini@123", database ="test_divyanshi")
mycursor = mydb.cursor()

sql_1 = "create table employee_info(id int(5), name varchar(20), dept varchar(10), salary integer(10))"

sql_2 = "insert into employee_info (id, name, dept, salary) values (%s,%s,%s,%s)"
values_1 = [(1001, "John", "IT", 20000),
            (1002, "Tom", "ADMIN", 20000),
            (1003,"Sana","HR",30000),
            (1004,"Amy","IT",35000),
            (1005,"Ajay","ADMIN",25000),
            (1006,"Kiara","IT",40000),
            (1007,"Lara","HR",24000),
            (1008,"Noah","HR",34000),
            (1009,"Kattie","IT",45000),
            (1010,"Petter","ADMIN",30000)]

# mycursor.execute(sql_1)
mycursor.executemany(sql_2,values_1)
mydb.commit()

mycursor.execute("select * from employee_info")
myresult = mycursor.fetchall()
for v in myresult:
    print(v)
