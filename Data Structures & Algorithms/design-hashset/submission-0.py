class MyHashSet:

    def __init__(self):
        self.cache = {}
        

    def add(self, key: int) -> None:
        if key in self.cache:
            return
        else:
            self.cache[key] = 1
        

    def remove(self, key: int) -> None:
        if key in self.cache:
            del self.cache[key]
        else:
            return

        

    def contains(self, key: int) -> bool:

        if key in self.cache:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)