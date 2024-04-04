import mysql.connector
connectionInfo = mysql.connector.connect(
    host= "localhost", 
    user="root", 
    password="*****",##enter your password of MySQL workbench
    database= "joinsdb"
    )
if connectionInfo.is_connected():
    print("MySQL Connected...")
else:
    print("Failed to connect MySQL")

mycursor= connectionInfo.cursor()

##create new table emp(emp, dept)
# emptable= "create table if not exists emp (empname text, deptname text, empsalary text)"
# mycursor.execute(emptable)

##create another table dept(id, dept)
# depttable= "create table if not exists dept (deptid int, deptname text)"
# mycursor.execute(depttable)

##insert data in emp table
# insertEmp = "insert  into emp values('{}', '{}', '{}')".format(input("Enter employee name: "), input("Enter department: "), input("Enter employee salary: "))
# mycursor.execute(insertEmp)
# connectionInfo.commit()

##insert data in dept table
# insertdept = "insert  into dept values({}, '{}')".format(int(input("Enter department id: ")), input("Enter department name: "))
# mycursor.execute(insertdept)
# connectionInfo.commit()

##find the common record in emp and dept using inner joins
# innerjoins= "select * from emp INNER JOIN dept ON emp.deptname = dept.deptname"
# mycursor.execute(innerjoins)
# print(mycursor.fetchall())
# connectionInfo.commit()

##LEFT joins
# leftjoins= "select * from emp LEFT JOIN dept ON emp.deptname = dept.deptname"
# mycursor.execute(leftjoins)
# print(mycursor.fetchall())
# connectionInfo.commit()

##right joins
# rightjoins= "select * from emp RIGHT JOIN dept ON emp.deptname = dept.deptname"
# mycursor.execute(rightjoins)
# print(mycursor.fetchall())
# connectionInfo.commit()

# ##cross/multiplication joins
# crossjoin= "select * from emp CROSS JOIN dept"
# mycursor.execute(crossjoin)
# print(mycursor.fetchall())
# connectionInfo.commit()

##self joins used to work on more then one table using where condition
# selfjoin= "select emp.empname, emp.deptname from emp, dept where emp.deptname = dept.deptname "
# mycursor.execute(selfjoin)
# print(mycursor.fetchall())
# connectionInfo.commit()

##UNION it will work on same records(merge  two or more result sets)
unionquery="select deptname from emp UNION ALL select deptname from dept"
mycursor.execute(unionquery)
print(mycursor.fetchall())
connectionInfo.commit()