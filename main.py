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
    cursor.execute("SELECT balance FROM users WHERE username = %s", (username,))    cursor.execute(f"SELECT Balance FROM bankdata WHERE id = {account[1]}")
    result = cursor.fetchone()
    for x in result:
        print(x)

def 