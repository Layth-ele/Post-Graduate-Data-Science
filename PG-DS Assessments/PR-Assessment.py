'''
Created on 2 Jun 2022

@author: laythal-shblawi
'''

#1#  Create a bank class with the following attributes:(IFSC_Code ,bankname ,branchname ,loc)

class Bank:
    def __init__(self ,IFSC_Code = 0000 ,bankname = 'ABC' ,branchname = 'DEF' ,loc = 9999):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc
        
#2# Create a customer class with the following attributes(CustomerID, custname, address, contactdetails)

class Customer:
    def __init__(self, customerID = 00000, custname = "GHI", address= "JKL", contactdetails =987654321):
        self.customerID = customerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails

#3# Create an account class that inherits from bank class with the following attributes (Use Super () to pass value to the base class):
#(AccountID ,Cust Object of Customer ,balance

#Add the following methods to get account information, withdraw, and deposit:

# getAccountInfo()
# deposit(2000,'true')
# widthraw(500)
# getBalance()


class Account(Bank):
    def __init__(self, accountID = 89839832389 ,custObjectOfCustomer = 'None' ,balance = 5000 ,type = True):
        super().__init__()
        
        self.accountID = accountID
        self.custObjectOfCustomer = custObjectOfCustomer
        self.balance = balance
        self.type = type

    def getAccountInfo(self):
        print("Bank Name " + str(self.bankname))
        print("Branch Name " + str(self.branchname))
        print("Account ID" + str(self.accountID))
        print('\n')
        
        if self.type == True :
            print('Account Type : Chequing Account')
            print('Account Balance :', self.balance)

        
        
    def getBalance(self): # calculate the total balance 
        balance = self.balance +self.dep - self.withd
        print("Total balance: " + str(balance) + ' $ ')


    def deposit(self, dep = 2000):
        self.dep = dep
        
        print ('You deposit a ' + '{}'.format(dep) + ' to your chequing account . \n' + 'Your balance is :', self.balance + self.dep)

    def withdraw(self, withd = 500):
        self.withd = withd
        print ('You withdraw a ' + '{}'.format(withd) + ' from your chequing account . \n' + 'Your New Balance is :', self.balance - self.withd)


#4# Create a SavigsAccount class that inherits from the account with the following attributes (Use Super () to
#pass valued to the base class):( SMinBalance)

        
class SavigsAccount (Account):
    def __init__(self ,SMinBalance = 5 ,type = False ):    
        super().__init__()
        
        self.SMinBalance = SMinBalance
        self.type = type
        if type == False:
           print('Account Type : Saving Account')
           print('Account Balance :', self.balance)


    def savingDeposit(self):
        self.dep = int(input("Enter the amount you want to deposit : USA "))
        print ('You deposit a ' + '{}'.format(self.dep) + ' $'+ ' to your saving account . \n' + 'Your total balance is :', self.balance + self.dep)

    def savingWithdraw(self):        
        self.withd = int(input("Enter the amount you want to withdraw: USA "))
        
        SMinBalance = self.balance - self.withd #Validate MinBalance before allowing withdrawals.

        if (SMinBalance < 0): 
            print("Error Amount not available in card.")
        else :
            print ('You withdraw a ' + '{}'.format(self.withd) + ' $' + ' from your saving account . \n' + 'Your New Balance Is :', SMinBalance )
            
    def getSavingBalance(self):# calculate the total balance
        balance = self.balance +self.dep - self.withd
        if(balance > 0):    
            print(" balance: " + str(balance) + ' $ ')
        else:
            print("Transaction can\'t be completed!")
            
            
            
            ####################################################################################################
            
                                                      #Test the Code#
            ####################################################################################################
                                                                                  
            
account1 = Account()
print('\n')         
account1.getAccountInfo()
print('\n')
account1.deposit()
print('\n')
account1.withdraw()
print('\n')
account1.getBalance()
print('\n')        
account2 = SavigsAccount()
print('\n')
account2.savingDeposit()
print('\n')
account2.savingWithdraw()
print('\n')
account2.getSavingBalance()