class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, increment=5000):
        self.salary += increment
