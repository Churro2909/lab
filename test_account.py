import pytest
from account import *


class Test:
    def setup_method(self):
        self.account1 = Account("John")
        self.account2 = Account("Jane")

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == "John"
        assert self.account1.get_balance() == 0
        assert self.account2.get_name() == "Jane"
        assert self.account2.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(100) is True
        assert self.account1.deposit(0) is False
        assert self.account1.deposit(-100) is False

    def test_withdraw(self):
        self.account2.deposit(1000)
        assert self.account2.withdraw(100) is True
        assert self.account2.withdraw(0) is False
        assert self.account2.withdraw(-100) is False
        assert self.account2.withdraw(1000) is False

    def test_get_balance(self):
        assert self.account1.get_balance() == 0
        assert self.account2.get_balance() == 0
        self.account1.deposit(1000)
        self.account2.deposit(2000)
        assert self.account1.get_balance() == 1000
        assert self.account2.get_balance() == 2000

    def test_get_name(self):
        assert self.account1.get_name() == "John"
        assert self.account2.get_name() == "Jane"
