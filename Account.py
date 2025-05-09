class Account:
    def __init__(self):
        self.customer = None
        self.balance = 0.0
        self.interest_rate = 0.05

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        if balance >= 0:
            self.balance = balance

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, rate):
        if 0 <= rate <= 1:
            self.interest_rate = rate
