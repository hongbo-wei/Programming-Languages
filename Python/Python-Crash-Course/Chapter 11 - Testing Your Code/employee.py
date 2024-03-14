# 11-3 Employee
class Employee:
    """A class contains: a first name, a last name and an annual salary"""

    def __init__(self, first, last, salary):
        self.name = f"{first} {last}".title()
        self.annual_salary = int(salary)

    def give_raise(self, raise_amount=''):
        if raise_amount:
            self.annual_salary += int(raise_amount)
        else:
            self.annual_salary += 5000

    def show_salary(self):
        print(f"${self.annual_salary}")
