import os
import mysql.connector

connection = mysql.connector.connect(
      user = "root",
      database = "abcdefg",
      password = "g01108PF!"
)

cursor = connection.cursor()

account = None
def main():
 #important stuff goes below this comment

 def checkbalance():
    os.system("cls")
    cursor.execute(f"SELECT Balance FROM bankdata WHERE ID = {account[1]}")
    queryData = cursor.fetchone()
    return queryData[0]

 def deposit(amt):
    os.system("cls")
    cursor.execute (f"UPDATE bankdata SET Balance = Balance + {amt} WHERE ID = '{account[1]}'")
    connection.commit()
    print(f"${amt} deposited successfully!")

 def accountcreate():
     addData = (f"INSERT into bankdata(Username, Password, Balance) VALUES (%s,%s,%s)")
     Username = input("Username?: ")
     Password = input ("Password?: ")
     Balance = input("Balance?: ")
     values = (Username,
               Password,
               Balance
               )
     
     cursor.execute(addData, values)
     connection.commit()


 def withdraw(amt):
  os.system("cls")
  print("How much would you like to withdraw?: ")
  withdraw_amt = float(input("> "))
  if withdraw_amt <= 0:
      print("Invalid amount!")
      return
  if withdraw_amt > checkbalance():
      print("Insufficient funds!")
      return
  cursor.execute (f"UPDATE bankdata SET Balance = Balance - {withdraw_amt} WHERE ID = '{account[1]}'")
  connection.commit()
  print(f"${withdraw_amt} withdrawn successfully!")
  
 def accountdelete():
    cursor.execute(f"DELETE FROM bankdata WHERE ID = {account[12]}")
    connection.commit()
    print("Account deleted successfully!")


 while True:
   
   answer = int(input("Good Afternoon! What would you like to do today?\n\n1: Login\n2: Sign up\n"))
    
   if answer == 1: #login
      username = input("Enter your username: ")
      password = input("Enter your password: ")

      #does the account exist?
      #if not, say something then go back to start
      cursor.execute(f"SELECT * FROM bankdata WHERE Username = '{username}' AND Password '{password}'")
      user = cursor.fetchone()
      if (user != None):
         account = user
         break
      os.system("cls")
      print("Not an existing user. Please try again.\n")
   elif answer == 2: #sign up
        ID = input("Enter your ID: ")
        username = input("Enter your username: ")
        password = input ("Enter your password: ")
        balance = input("Enter your balance: ")
        values = (ID, username, password, balance)
        mySql_insert_query = (f"INSERT INTO bankdata (ID, Username, Password, Balance) VALUES (%s, %s, %s, %s)")
        cursor.execute(mySql_insert_query, values) #error here
        connection.commit()
        print("Registration Successful!")
        account = cursor.fetchone()
        break

 while True:
    response = int(input("What would you like to do?\n\n1: Check Balance\n2: Make a Deposit\n3: Make a Withdrawal\n4: Make a New Account\n5: Delete Your Account"))

    if response == 1:
        checkbalance()
    elif response == 2:
        amt = float(input("How much do you want to deposit? \n"))
        deposit()
    elif response == 3:
        amt = float(input("How much do you want to withdraw? \n"))
        withdraw()
    elif response == 4:
       accountcreate()
    elif response == 5:
       accountdelete()


 #database close
cursor.close
connection.close

if __name__ == "__main__":
  main()