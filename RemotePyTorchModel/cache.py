class Cache():
	# very fast way to prototype a cache... should fix some optimization and error handling issues
	def __init__(self, n):
		self.cache = []
		# cache is a list of items, which are list of 2 elements: a couple (a list of 2 elements, key value pairs)
		# and a number, which is the query frequency of the key [[key, value], f]
		self.sizeLimit = n 

	def insert(self, hashedKey, value):
		keyValuePair = [hashedKey, value]
		self.cache = self.cache[:self.sizeLimit-1]
		for el in self.cache:
			el[1] -= 1
		self.cache.append([keyValuePair, 1])
		self.__sortCacheByPriority()

	def get(self, key):
		toReturn = -1
		for el in self.cache:
			if el[0][0] == key: 
				toReturn = el[0][1]
				el[1] += 1
				break
		self.__sortCacheByPriority()
		return toReturn

	def __sortCacheByPriority(self):
		self.cache.sort(key=lambda x: x[1], reverse=True)