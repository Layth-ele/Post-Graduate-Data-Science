'''
Created on 2 Jun 2022

@author: laythal-shblawi
'''

#1#  Create a bank class with the following attributes:(IFSC_Code ,bankname ,branchname ,loc)
from xmlrpc.client import boolean

class Bank:
    def __init__(self ,IFSC_Code = 0000 ,bankname = 'ABC' ,branchname = 'DEF' ,loc = 9999):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc

class Customer:
    def __init__(self, customerID = 00000, custname = "GHI", address= "JKL", contactdetails =987654321):
        self.customerID = customerID
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails


class Account(Bank):
    def __init__(self, accountID = 89839832389 ,custObjectOfCustomer = 'None' ,balance = 5000):
        super().__init__()
        self.accountID = accountID
        self.custObjectOfCustomer = custObjectOfCustomer
        self.balance = balance

    def getAccountInfo(self):
        print("Bank Name " + str(self.bankname))
        print("Branch Name " + str(self.branchname))
        print("Account ID" + str(self.accountID))
        
    def getBalance(self):
        return self.balance

    def deposit(self, dep = 2000, chequing= True):
        self.dep = dep
        self.chequing = True
        if self.chequing == True :
                print('Account Type : Chequing Account')
        print ('You deposit a ' + '{}'.format(dep) + ' to your chequing account . \n' + 'Your total balance is :', self.balance + self.dep)

    def withdraw(self, withd = 500):
        self.withd = withd
        print ('You withdraw a ' + '{}'.format(withd) + ' from your chequing account . \n' + 'Your total balance is :', self.balance - self.withd)

        
class SavigsAccount (Bank):
    def __init__(self,accountID = 89839832389 ,SMinBalance = 2003 ,balance = 2000 ):
        super().__init__()
        self.SMinBalance = SMinBalance
        self.balance = balance
        self.saving = True
        if SMinBalance > balance: 
            print('You have not enough money in your saving account')     
            
    def getSavingBalance(self):
        return self.balance
        
    def savingDeposit(self, dep = 2000, saving= True):
        if self.saving == True :
            print('Account Type : Saving Account')
        self.dep = dep
        print ('You deposit a ' + '{}'.format(dep) + ' to your saving account . \n' + 'Your total balance is :', self.balance + self.dep)

    def savingWithdraw(self, withd = 500):
        self.withd = withd
        print ('You withdraw a ' + '{}'.format(withd) + ' from your saving account . \n' + 'Your total balance is :', self.balance - self.withd)
                    



            


account1 = Account()
account1.getAccountInfo()
print('\n')
print("Total balance: " + str(account1.getBalance()) + ' $ ')
print('\n')
account1.deposit()
print('\n')
account1.withdraw()

account2 = SavigsAccount()
account2.getSavingBalance()
print('\n')
print("Total balance: " + str(account2.getSavingBalance()) + ' $ ')
print('\n')
account2.savingDeposit()
print('\n')
account2.savingWithdraw()
