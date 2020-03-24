"""
File: savings_account.py
Owner: Sam Williams Jebaraj (samwilliams.jebaraj@bt.com)
Account: Facebook ZTP Team
This file works on creating saving account for customers
"""
class SavingsAccount(object):
    """
    This class represents a savings account 
    With the owner's Name, PIN and Balance
    """
    RATE=0.02
    def __init__(self,name,pin,balance = 0.0):
        self._name=name
        self._pin=pin
        self._balance=balance
    
    def __str__(self):
        result="Name: {}\nPIN: {}\nBalance: {}".format(self._name,self._pin,self._balance)
        return result
    
    def getBalance(self):
        """Provides the balance amount in the account"""
        return self._balance
    
    def getName(self):
        """Provides the name of the account holder"""
        return self._name
    
    def getPin(self):
        """Provides the PIN of the account holder"""
        return self._pin
    
    def deposit(self,amount):
        """Deposits the given amount and returns the new balance"""
        self._balance += amount

    def withdraw(self,amount):
        """Withdraws the given amount. 
        Returns None if Sucessful, or an error message
        if Un Sucessful"""
        if amount<0:
            return "Amount must be greater than 0."
        elif self._balance<amount:
            return "Insufficients Funds"
        else:
            self._balance -= amount
            return None

    def computeInterest(self):
        """ Computes, deposits and returns the interest """
        interest=self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest