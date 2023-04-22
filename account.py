class Account:
    def __init__(self, name: str) -> None:
        """
        Function creates a new Account with param name and an account balance of 0
        :param name: name of account
        """
        self.__account_name = name
        self.__account_balance = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Function adds amount to balance if amount is positive
        :param amount: amount to be added to balance
        :return: True if amount is positive, False if not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function removes money from balance if amount is positive and less or equal to amount in balance
        :param amount: amount to be removed from balance
        :return: True if amount is positive and less or equal to current balance, False if not
        """
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Function returns account balance
        :return: __account_balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function returns account name
        :return: __account_name
        """
        return self.__account_name
