import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='seng#12$$von',
)
# -------------------------->
cursorObject = dataBase.cursor()
# -------------------------->
cursorObject.execute("CREATE DATABASE employ")
print("All Done!")