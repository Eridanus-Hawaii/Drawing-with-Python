class TestClass:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.last_food = 'Nothing'
	
	def eat(self, food):
		self.last_food = food
		print(self.name, 'eats', food)

	def __str__(self):
		return 'Name:' + self.name + 'Age:' + str(self.age) + 'Last:' + self.last_food

if __name__ == '__main__':
	hana = TestClass("Hana", 23)
	print('-----------')
	print(hana)
	hana.eat('プリン')
	print(hana)
	print('-----------')

	anna = TestClass("Anna", 23)
	anna.eat('Sushi')
	print(anna)
	print('-----------')

	ryos = TestClass("ryos", 57)
	ryos.eat('スパゲッティ')
	print(ryos)
	print('-----------')