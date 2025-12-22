class Employee:
    _salary = 1000
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

e = Employee("John", 5000)
print(e.salary)
e.salary = 1000
print(e.salary)