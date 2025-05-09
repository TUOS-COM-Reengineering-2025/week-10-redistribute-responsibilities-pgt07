from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}
        self.customer_phone_numbers = {}
        self.branches = []
        self.branch_opening_times = {}
        self.payroll = None

    def setup_branch(self, branch: Branch):
        if branch not in self.branches:
            self.branches.append(branch)
            self.branch_opening_times[branch] = "9:00"

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in list(branch.get_staff()):
            self.transfer_staff_member(branch, transfer_branch, staff)
        if branch in self.branches:
            self.branches.remove(branch)
            self.branch_opening_times.pop(branch, None)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        if staff in from_branch.get_staff():
            from_branch.get_staff().remove(staff)
            to_branch.get_staff().append(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        if account not in self.accounts:
            self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_addresses[customer] = "NO ADDRESS"
            self.customer_phone_numbers[customer] = "NO PHONE NUMBER"

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        balance = account.get_balance()
        interest_rate = account.get_interest_rate()
        interest = balance * interest_rate
        account.set_balance(balance + interest)

    def add_funds(self, account: Account, amount: float):
        if amount > 0:
            balance = account.get_balance()
            account.set_balance(balance + amount)

    def close_account(self, account: Account):
        if account in self.accounts:
            account.set_customer(None)
            account.set_balance(0)
            self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        if staff not in branch.get_staff():
            branch.get_staff().append(staff)

    def change_opening_time(self, branch: Branch, time: str):
        if branch in self.branches:
            self.branch_opening_times[branch] = time

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        try:
            schedule = self.payroll.get_staff_category_pay_schedule(staff_category)
            schedule.set_pay_date(date)
        except KeyError:
            pass
