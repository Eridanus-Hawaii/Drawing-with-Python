from _typeshed import Self


class TestClass:
	def __init__(self, name):
		self.name = name

if __name__ == '__main__':
	obj1 = TestClass()
	print(obj1)
	obj2 = TestClass()
	print(obj2)