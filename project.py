# banking system(using class and file handling)

# a.create accounts with initial capital
# b.deposit/withdraw
# c.transaction history in a file

class Bank :
    
      with open("accounts.txt", "w") as f:
             f.write(f"{"Name":<25}{"d.o.b":<15}{"phno":<20}{"Capital":<20}{"email_id":<35}{"nominee":<20}{"adhaarcard":<15}\n")
   
      def __init__(self,name,dob,phno,emailid,nominee,adhaarcard):
             self.name = name
             self.dob = dob
             self.phno = phno
             self.emailid = emailid
             self.nominee = nominee
             self.adhaarcard = adhaarcard
             self.capital=0
             while self.capital<1500:
                self.capital=int(input("Enter the initial capital(minimum 1500):"))
                if self.capital>=1500:
                     with open("accounts.txt", "a") as f:
                         f.write(f"{self.name:<25}{self.dob:<15}{self.phno:<20}{self.capital:<20}{self.emailid:<35}{self.nominee:<20}{self.adhaarcard:<15}\n")
                else:
                     print(f'insufficient capital for starting an account for {self.name} .Please try again')
             print(f'Account created for {self.name} successfully ')
             self.file_name = f"{self.name.replace(" ","_")}_transactions"
        
    
             

             with open(f"{self.file_name}.txt","w")as f:
                 f.write(f'{"name":<25}{"deposit":<15}{"withdrawal":<15}{"total":<15}\n')
             
      def deposit(self,amt) :
             self.capital+=amt
             print(f'{amt} amount deposited on {self.name}s account')
             with open(f"{self.file_name}.txt","a") as f:
                    f.write(f'{self.name:<25}{amt:<15}{"none":<15}{self.capital:<15}\n')
                                         
      def  withdraw(self,amt) :
             if self.capital-amt<1500:
                   print("Withdrawal not possible")
                   return
             self.capital-=amt
             print(f'{amt} debited from {self.name}s account avail balance={self.capital}')
             with open(f"{self.file_name}.txt","a") as f:
                 f.write(f'{self.name:<25}{"none":<15}{amt:<15}{self.capital:<15}\n')
      def  transactionhistory(self):
         try:
             with open(f'{self.file_name}.txt','r') as f:
                 print(f.read())
         except FileNotFoundError:
               print("Transaction File not found")
# count=0
# set1=[]
# n=int(input("Enter 1 for creating bank account: 2 for depositing: 3 for withdrawal : and 4 for transaction history:"))
# if n==1:
#          name=input("Enter the account holder name:")
#          dob=input("Enter Dob in dd/mm/yyyy format:")
#          phno=input("Enter phone number:")
#          email_id=input("Enter email id:")
#          nominee=input("Enter nominee name:")
#          aadhar=input("Enter aadhar number:")
#          count+=1
#          acname=f"account{count}"
         
#          set1.append({name:count})
#          acname=Bank(name,dob,phno,email_id,nominee,aadhar)
# if n==2:
#          name=input("Enter account holder name:")
#          for  name in set1:
#                acname=f"account{set1[name]}"
#          amount=int(input("Enter the amount:"))
#          acname.deposit(amt)
# if n==3:
#          name=input("Enter account holder name:")
#          for  name in set1:
#                acname=f"account{set1[name]}"
#          amount=int(input("Enter the amount:"))
#          acname.withdraw(amt)
# if n==4:
#          name=input("Enter account holder name:")
#          for  name in set1:
#                acname=f"account{set1[name]}"
       
#          acname.transactionhistory()

         

accounts = {}  # Store Bank objects

count = 0
while True:
    n = int(input("\nEnter 1 for creating bank account, 2 for depositing, 3 for withdrawal, 4 for transaction history, or 5 to exit: "))
    
    if n == 1:
        name = input("Enter the account holder name: ")
        dob = input("Enter DOB (dd/mm/yyyy): ")
        phno = input("Enter phone number: ")
        email_id = input("Enter email id: ")
        nominee = input("Enter nominee name: ")
        aadhar = input("Enter Aadhar number: ")

        count += 1
        
        # Create the account
        bank_account = Bank(name, dob, phno, email_id, nominee, aadhar)
        accounts[name] = bank_account  # Save the object to the dictionary
        print(f"Account created for {name} successfully.")

    elif n == 2:
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = int(input("Enter the amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found!")

    elif n == 3:
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = int(input("Enter the amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found!")

    elif n == 4:
        name = input("Enter account holder name: ")
        if name in accounts:
            accounts[name].transactionhistory()
        else:
            print("Account not found!")

    elif n == 5:
        print("Exiting the banking system. Goodbye!")
        break  # Exit the loop

    else:
        print("Invalid option, please try again.")