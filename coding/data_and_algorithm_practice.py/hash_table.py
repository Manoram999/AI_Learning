def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100
get_hash('march 6')



class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None        

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t.arr
print(t.arr)


t["dec 30"] = 88
t["dec 30"]
del t["march 6"]
t.arr

print(t.arr)
