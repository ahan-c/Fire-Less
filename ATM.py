import time
print("Welcome to ATM")
time.sleep(1)
bal = 0
print("\nBefore using the ATM you need to create a bank account first, enter your username and PIN below.")
user = input("Enter an username:")
pin = int(input("Enter a PIN:"))

time.sleep(0.7)
print("\n\nYou currently have no balance in your account, enter how much balance you want to put in your bank account.")
bal1 = int(input("Enter value to be deposited:"))
bal = bal + bal1
print("Succesfully, deposited ₹"+str(bal1),"in your bank account.")
time.sleep(1.2)
print("\nNow your bank balance is ₹"+str(bal)+".")

print("You've succesfully done your first transaction, as a reward ₹5000 will be added to your bank account.")

print("\nYou get 500 bank cred. Bank cred is a type of credit which you can trade in for real money, 1 bank cred = ₹1.")
print("Each time you make a transaction you get rewarded 1 bank cred. In 1 day if you make more than 1 transaction you won't receive any bank creds.")
print("\nNice job on making the transactions and thanks for chosing this bank.")
print("\nYou Can anytime make t")