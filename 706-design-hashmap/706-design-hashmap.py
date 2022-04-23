class MyHashMap:

    def __init__(self):
        self.d={}
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.d[key]=value
            
        else:
            self.d[key]=value
        

    def get(self, key: int) -> int:
        if key in self.d:
            return self.d[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.d:
            del self.d[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)