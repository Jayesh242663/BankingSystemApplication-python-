import connection
acc_no = int(input("acc_no"))
db = connection.Connection().get_connection()
cursor = db.cursor()
cursor.execute("SELECT * FROM login WHERE accno = %s", (acc_no,))
result = cursor.fetchall()
print(result)

cursor.close()
db.close()