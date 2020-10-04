import sqlite3
connection=sqlite3.connect("chinook.db")


cursor=connection.execute("""select * 
                          from customers 
                          where city='Prague' or city='Berlin'
                          order by FirstName desc""")


for row in cursor:
    print("First Name=" + row[1])
    print("Last Name=" + row[2])



cursor=connection.execute("""select city,count(*) from Customers 
                          group by city having count(*)>1 order by count(*) desc""")
for row in cursor:
    print("City="+row[0])
    print("Count="+str(row[1]))
connection.close() 
