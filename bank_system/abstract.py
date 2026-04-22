from abc import ABC, abstractmethod
import datetime


class IBank(ABC):
    def __init__(self, pin, initial_balance=10000):
        self.balance = initial_balance
        self.transactions = []
        self.pin = pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        self.balance += amount
        self._add_transaction("Deposit", amount)
        return f"Deposited Rs {amount}. Balance: Rs {self.balance}"

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            return "Invalid PIN"

        if amount <= 0:
            return "Invalid amount"

        allowed, msg = self.can_withdraw(amount)
        if not allowed:
            return msg

        self.balance -= amount
        self._add_transaction("Withdraw", amount)
        return f"Withdrew Rs {amount}. Balance: Rs {self.balance}"

    def _add_transaction(self, t_type, amount):
        self.transactions.append({
            "type": t_type,
            "amount": amount,
            "time": str(datetime.datetime.now())
        })

    def show_transactions(self):
        if not self.transactions:
            return "No transactions yet"

        return "\n".join(
            f"{t['time']} | {t['type']} | Rs {t['amount']}"
            for t in self.transactions
        )

    @abstractmethod
    def type_of_account(self):
        pass

    @abstractmethod
    def can_withdraw(self, amount):
        pass