import mysql.connector

conn=mysql.connector.connect(host='localhost', username='root',password='22111101@2005',database='REGISTRATIONS')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("Connnection succcsfullyy created !!!")