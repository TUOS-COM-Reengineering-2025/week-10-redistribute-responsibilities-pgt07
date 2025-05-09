from PaySchedule import PaySchedule


class Payroll:
    def __init__(self):
        self.staff_category_pay_schedules = {"Manager": PaySchedule("1st")}

    def get_staff_category_pay_schedule(self, staff_category):
        return self.staff_category_pay_schedules.get(staff_category, PaySchedule("1st"))

    def get_staff_category_pay_day(self, staff_category):
        schedule = self.staff_category_pay_schedules.get(staff_category)
        return schedule.get_pay_date() if schedule else None
