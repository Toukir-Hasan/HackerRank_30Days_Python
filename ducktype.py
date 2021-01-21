import mysql.connector
mydb =mysql.connector.connect(host='localhost', user='root', passwd='bangladesh',database="siam")
mycurs=mydb.cursor()
mycurs.execute("SELECT * FROM student")

myresult = mycurs.fetch()
print(myresult)




