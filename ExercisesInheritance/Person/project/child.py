from OOP.ExercisesInheritance.Person.project.person import Person


class Child(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

