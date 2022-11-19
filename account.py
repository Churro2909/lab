class Account:
    '''
    A class that represents the details of a bank account.
    '''

    def __init__(self, name: str) -> None:
        '''
        This initializes the class with the name entered and a default balance of 0.
        :param name: Name of account as String.
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float or int) -> bool:
        '''
        This function deposits an amount of money that is greater than 0 to the account.
        :param amount: Amount deposited as numeric value.
        :return: Boolean based on if the deposit was successful (True) or not (False).
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float or int) -> bool:
        '''
        This function withdraws an amount greater than 0 but no more than amount available from the account.
        :param amount: Amount withdrawn as a numeric value.
        :return: Boolean based on if the withdrawal was successful (True) or not (False).
        '''
        if amount <= 0 or amount > self.get_balance():
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Checks the current balance of the account.
        :return: Balance as a numeric value.
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Checks the current name of the account.
        :return: Name as a String.
        '''
        return self.__account_name
