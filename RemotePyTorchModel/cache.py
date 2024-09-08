class CacheItem:
    def __init__(self, key, value, timestamp):
        self.key = key
        self.value = value
        self.frequency = 1
        self.timestamp = timestamp  # Used to track aging

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.time = 0  # Global time counter to handle aging

    def insert(self, key, value):
        self.time += 1  # Increment the global time with every operation

        # Check if key already exists in cache, update if it does
        for item in self.cache:
            if item.key == key:
                item.value = value
                item.frequency += 1
                item.timestamp = self.time  # Update timestamp to the current time
                self.__sortCacheByPriority()
                return

        # If cache is full, remove the least frequent item
        if len(self.cache) >= self.capacity:
            self.cache.pop()

        # Insert new item
        new_item = CacheItem(key, value, self.time)
        self.cache.append(new_item)
        self.__sortCacheByPriority()

    def get(self, key):
        self.time += 1  # Increment the global time with every operation

        for item in self.cache:
            if item.key == key:
                item.frequency += 1
                item.timestamp = self.time  # Update timestamp to refresh priority
                self.__sortCacheByPriority()
                return item.value
        return -1  # Key not found

    def __sortCacheByPriority(self):
        # Sort by frequency first, then by timestamp (older items with the same frequency will be deprioritized)
        self.cache.sort(key=lambda x: (x.frequency, x.timestamp), reverse=True)