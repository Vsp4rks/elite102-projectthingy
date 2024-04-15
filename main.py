import os
import mysql.connector


connection = mysql.connector.connect(
      user = "root",
      database = "abcdefg",
      password = "g01108PF!"
)

cursor = connection.cursor()

account = None


def checkbalance():
    cursor.execute(f"SELECT Balance FROM bankdata WHERE id = {account[0]}")
    result = cursor.fetchone()
    return queryData[0]

def deposit(amt):
    os.system("cls")
    cursor.execute (f"UPDATE bankdata SET Balance = Balance + {amt} WHERE ID = '{account[0]}'")
    connection.commit()
    print(f"${amt} deposited successfully!")



#database close
cursor.close
connection.close