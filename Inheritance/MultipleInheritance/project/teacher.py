from OOP.Inheritance.MultipleInheritance.project.employee import Employee
from OOP.Inheritance.MultipleInheritance.project.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'
