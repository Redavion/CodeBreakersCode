class Container:
    
    def __init__(self):
        self.container = []
        
    def put(self, key, value):
        for index, keyValue in enumerate(self.container):
            if keyValue[0] == key:
                self.container[index] = (key,value)
                return
        self.container.append((key,value))
        
    def get(self, key):
        for (k, v) in self.container:
            if k == key:
                return v
            
        return -1
    
    def remove(self, key):
        for index, keyValue in enumerate(self.container):
            if keyValue[0] == key:
                del self.container[index]
            
    
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.listSize= 2069
        #a list of containers
        self.myMap = [Container() for i in range(self.listSize)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.listSize
        self.myMap[index].put(key, value)
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.listSize
        return self.myMap[index].get(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.listSize
        self.myMap[index].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)