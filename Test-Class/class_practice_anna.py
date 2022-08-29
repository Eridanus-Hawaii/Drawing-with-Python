# practice of anna 
class TestClass:
    def __init__(self, name, age):
        # __init__ is the rule first creator made so every time we have to follow
        self.name = name
        self.age = age
        self.last_food = 'Nothing'

    def eat(self, food):
        self.last_food = food
        print(self.name, 'eats', food)

    def __str__(self):
        return 'Name:' + self.name + '\n' + 'Age:' + str(self.age) + '\n' + 'Last:' + self.last_food


if __name__ == '__main__':
    anna = TestClass('Anna', 23)
    print(anna)
    anna.eat('sushi')
    print(anna)
    print('----')

    hana = TestClass('Hana', 23)
    hana.eat('pudding')
    print(hana)
    print('----')

    ryos = TestClass('ryos', 57)
    ryos.eat('spaghetti')
    print(ryos)