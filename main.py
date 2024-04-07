import mysql.connector


connection = mysql.connector.connect(
      user = "root",
      database = "abcdefg",
      password = "g01108PF!"
)

cursor = connection.cursor()


def checkbalance():
    cursor.execute("SELECT balance FROM users WHERE username = %s", (username,))