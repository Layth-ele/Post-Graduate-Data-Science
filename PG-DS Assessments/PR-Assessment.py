'''
Created on 2 Jun 2022

@author: laythal-shblawi
'''

#1#  Create a bank class with the following attributes:(IFSC_Code ,bankname ,branchname ,loc)

class Bank:
    def __init__(self ,IFSC_Code ,bankname ,branchname ,loc):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc
        
        
        
#2#  Create a  customer class with the following attributes:(CustomerID ,custname ,address ,contactdetails)
       
class Customer:
    def __init__(self ,customerID ,custname ,address ,contactDetails):
        self.customerID = customerID
        self.custname = custname
        self.address = address
        self.contactDetails = contactDetails
        
        
#3#  Create an account class that inherits from bank class with the following attributes (Use Super () to pass value to the base class)

class Account(Bank):
    def __init__(self ,accountID ,custObjectOfCustomer ,balance):
        self.accountID = accountID
        self.custObjectOfCustomer = custObjectOfCustomer
        self.balance = balance
        super().__init__(IFSC_Code ,bankname ,branchname ,loc)
        
        def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
            
    #
    # getAccountInfo()
    # deposit(2000,'true')
    # widthraw(500)
    # getBalance()  
    
#4# Create a SavigsAccount class that inherits from the account with the following attributes (Use Super () to pass valued to the base class
    
pass
    
# getSavingAccountInfo()
# deposit(2000,'true')
# widthraw(500)
# getBalance()
        
    