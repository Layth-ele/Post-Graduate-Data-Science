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
    def __init__(self, accountID = 89839832389 ,custObjectOfCustomer = 'None' ,balance = 5000 ,chequing= True):
        super().__init__()
        
        self.accountID = accountID
        self.custObjectOfCustomer = custObjectOfCustomer
        self.balance = balance
        self.chequing = chequing

    def getAccountInfo(self):
        print("Bank Name " + str(self.bankname))
        print("Branch Name " + str(self.branchname))
        print("Account ID" + str(self.accountID))
        
        
    def getBalance(self):
        if self.chequing == True :
            print('Account Type : Chequing Account')
        return self.balance
        
    

    def deposit(self, dep = 2000):
        self.dep = dep
        
        print ('You deposit a ' + '{}'.format(dep) + ' to your chequing account . \n' + 'Your total balance is :', self.balance + self.dep)

    def withdraw(self, withd = 500):
        self.withd = withd
        print ('You withdraw a ' + '{}'.format(withd) + ' from your chequing account . \n' + 'Your total balance is :', self.balance - self.withd)


#4# Create a SavigsAccount class that inherits from the account with the following attributes (Use Super () to
#pass valued to the base class):( SMinBalance)

        
class SavigsAccount (Account):
    def __init__(self ,SMinBalance = 5 ,saving = True ):
        super().__init__()
        
        self.SMinBalance = SMinBalance
        self.saving = saving
        if saving == True:
           print('Account Type : Saving Account')
        
    def getSavingBalance(self):
        return self.balance
    
    def savingDeposit(self):
        self.dep = int(input("Enter the amount you want to deposit : USA "))
        print ('You deposit a ' + '{}'.format(self.dep) + ' $'+ ' to your saving account . \n' + 'Your total balance is :', self.balance + self.dep)

    def savingWithdraw(self):
        self.withd = int(input("Enter the amount you want to withdraw: USA "))
        if (self.balance - self.withd < 0): #Validate MinBalance before allowing withdrawals.
            print("Error Amount not available in card.")
        else :
            print ('You withdraw a ' + '{}'.format(self.withd) + ' $' + ' from your saving account . \n' + 'Your total balance is :', self.balance - self.withd)
            
account1 = Account()
print('\n')         
account1.getAccountInfo()
print('\n')        
print("Total balance: " + str(account1.getBalance()) + ' $ ')
print('\n')
account1.deposit()
print('\n')
account1.withdraw()
print('\n')
account2 = SavigsAccount()
account2.getSavingBalance()
print('\n')
print("Total balance: " + str(account2.getSavingBalance()) + ' $ ')
print('\n')
account2.savingDeposit()
print('\n')
account2.savingWithdraw()
