class PaySchedule:
    def __init__(self, pay_date):
        self._pay_date = pay_date

    def get_pay_date(self):
        return self._pay_date

    def set_pay_date(self, pay_date):
        self._pay_date = pay_date
