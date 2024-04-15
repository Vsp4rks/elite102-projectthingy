import os
import mysql.connector

#later find out why it doesnt think its connected
#context: whenever i reference my sql table at all it (or any sql stuff),
#it doesnt know what im talking about and comes up as an error

connection = mysql.connector.connect(
      user = "root",
      database = "abcdefg",
      password = "g01108PF!"
)

cursor = connection.cursor()

account = None

#important stuff goes below this comment

def checkbalance():
    os.system("cls")
    cursor.execute(f"SELECT Balance FROM bankdata WHERE id = {account[0]}")
    queryData = cursor.fetchone()
    return queryData[0]

def deposit(amt):
    os.system("cls")
    cursor.execute (f"UPDATE bankdata SET Balance = Balance + {amt} WHERE ID = '{account[0]}'")
    connection.commit()
    print(f"${amt} deposited successfully!")

def accountcreate():
     addData = ("INSERT into bankdata(Username, Password, Balance) VALUES (%s,%s,%s)")
     Username = input("Username?: ")
     Password = input ("Password?: ")
     Balance = input("Balance?: ")
     values = (Username,
               Password,
               Balance
               )
     
      cursor.execute(addData, values) #i actually cant put it anywhere else or else everything else gets an error
      connection.commit()


def withdraw(amt):
  os.system("cls")
  print("How much would you like to withdraw?: ")
  withdraw_amt = float(input("> "))
    #check if valid
   if withdraw_amt <= 0:
      print("Invalid amount!")
      return
   if withdraw_amt > checkbalance():
      print("Insufficient funds!")
      return
   cursor.execute (f"UPDATE bankdata SET Balance = Balance - {withdraw_amt} WHERE ID = '{account[0]}'")
   connection.commit()
   print(f"${withdraw_amt} withdrawn successfully!")
  
def accountdelete():
    cursor.execute(f"DELETE FROM bankdata WHERE ID = {account[0]}")
    connection.commit()
    print("Account deleted successfully!")

#time for CUI thing

while True:
   
   answer = int(input("Good Afternoon! What would you like to do today?\n\n1: Login\n 2: Sign up\n"))
    
   if answer == 1: #login
      username = input("Enter your username: ")
      password = input("Enter your password: ")

      #does the account exist?
      #if not, say something then go back to start
      cursor.execute(f"SELECT * FROM bankdata WHERE Username = '{Username}' AND Password '{Password}'")
      user = cursor.fetchone()
      if (user != None):
         account = user
         break
      os.system("cls")
      print("Not an existing user. Please try again.\n")
   elif answer == 1: #sign up
        username = input("Enter your username: ")
        password = input ("Enter your password: ")
        balance = input("Enter your balance: ")
        values = (username, password, balance)
        mySql_insert_query = (f"INSERT INTO bankdata (Username, Password, Balance) VALUES (%s, %s, %s)")
        cursor.execute(mySql_insert_query, values)
        connection.commit()
        print("Registration Successful!")
        account = cursor.fetchone()
        break


#database close
cursor.close
connection.close