class customRandom(object):
	"""A Custom random class for 'Mnm Dige'"""
	def __init__(self, iterable):
		if not hasattr(iterable, "__iter__"):
			raise TypeError(f"Object of type {type(iterable)} is not iterable")
		if not len(iterable):
			raise Exception("iterable must be non-empty")

		self.items = iterable
		self.length = len(self.items)
		self.luck = [100 / self.length for _ in range(self.length)]


	def setLuck(self, iterable):
		if not hasattr(iterable, "__iter__"):
			raise TypeError(f"Object of type {type(iterable)} is not iterable")
		if not len(iterable):
			raise Exception("iterable must be non-empty")
		if len(iterable) != self.length:
			raise IndexError("luckList must have the same length as itemsList")

		if type(iterable) is dict:
			if sum(iterable.values()) != 100:
				raise Exception("sum of the luckList must be 100")

			temp, i = 0, 0
			for item in self.items:
				try:
					temp += iterable[item]
				except KeyError:
					raise KeyError(f"item {item} is not in your itemsList")
				self.luck[i] = temp
				i += 1

		else:
			if sum(iterable) != 100:
				raise Exception("sum of the luckList must be 100")

			temp = 0
			for i in range(self.length):
				temp += iterable
				self.luck[i] = temp

	def getRandom(self):
		try:
			random
		except NameError:
			import random

		temp = random.randint(1, 100)
		for i in range(self.length):
			if self.luck[i] >= temp:
				return (self.items[i], temp)

theRandom = customRandom([1, 2, 3, 4])
theRandom.setLuck({1: 50, 2: 15, 3: 25, 4: 10})
print(theRandom.luck, theRandom.items)
for _ in range(20):
	print(theRandom.getRandom())
