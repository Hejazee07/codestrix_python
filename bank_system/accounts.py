from abstract import IBank

class Savings(IBank):
    def type_of_account(self):
        return "Savings Account"

    def can_withdraw(self, amount):
        if self.balance - amount < 1000:
            return False, "Minimum balance of 1000 must be maintained"
        return True, ""


class Current(IBank):
    def type_of_account(self):
        return "Current Account"

    def can_withdraw(self, amount):
        return True, ""


class Student(IBank):
    def type_of_account(self):
        return "Student Account"

    def can_withdraw(self, amount):
        if amount > 5000:
            return False, "Maximum withdrawal limit is 5000"
        if amount > self.balance:
            return False, "Insufficient balance"
        return True, ""