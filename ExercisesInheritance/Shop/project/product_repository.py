from OOP.ExercisesInheritance.Shop.project.food import Food
from OOP.ExercisesInheritance.Shop.project.drink import Drink


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
        except StopIteration:
            return

        return product

    def remove(self, product_name):
        try:
            self.products.remove(next(filter(lambda p: p.name == product_name, self.products)))
        except StopIteration:
            pass

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)