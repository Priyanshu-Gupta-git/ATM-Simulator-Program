import datetime
now = datetime.datetime.now()
password = "1234"
balance = 100
print("\033[106;31m"," ".rjust(75,"-"))
print('''\033[95;43m
__        __   _                                       _             
\ \      / /__| | ___ ___  _ __ ___   ___         ___ | |_           
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \       / _ \| __|          
  \ V  V /  __/ | (_| (_) | | | | | |  __/      | (_) | |_           
   \_/\_/ \___|_|\___\___/|_|_|_| |_|\___|       \___/ \__|          
 _ __ ___  _   _        / \|_   _|  \/  |                            
| '_ ` _ \| | | |      / _ \ | | | |\/| |                            
| | | | | | |_| |     / ___ \| | | |  | |                            
|_| |_| |_|\__, |    /_/   \_\_| |_|  |_|                            
           |___/                                              \033[0m''')

print("\033[91;41m"" ".ljust(75,"-"))
print("\nEnter <1> Check Balance")
print("Enter <2> Deposit Money")
print("Enter <3> Withdraw Money")
print("Enter <4> Exit\033[0m")
print("\033[91;107m","*"*50)
while True:
    choice = int(input("Enter your choice: "))
    password_atm = input("\033[A\033[2KEnter ATM password: ")
    if password_atm == password:
        if choice == 1:
            print(f"\033[A\033[2kYour bank balance: Rs {balance}")
        elif choice == 2:
            amount = float(input("\033[A\033[2KEnter the amount: "))
            if amount > 0:
                balance += amount
                print(f"\033[A\033[2KDeposit successful\nTotal Balance: Rs {balance}")
            else:
                print("\033[A\033[2KPlease enter a positive amount.")
        elif choice == 3:
            amount = float(input("Enter the amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"\033[A\033[2KWithdrawal successful\nTotal Balance: Rs {balance}")
            else:
                print("\033[A\033[2KPlease enter a correct amount.")
        elif choice == 4:
            print("\033[A\033[2kThank you for using our service!")
            break
        else:
            print("\033[A\033[2kInvalid choice. Please try again.")
    else:
        print("\033[A\033[2K ATM password is incorrect.")
    
print(now.strftime("\033[1;91;103mdate  %d-%B-%Y \n time %H:%M:%S \\ day- %A\033[0m"))
for i in range(1,7):
    for j in range (1,6):
        print("--",end=":")
