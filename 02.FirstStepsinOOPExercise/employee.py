class Employee:

    def __init__(self, id, firstname, lastname, salary):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

