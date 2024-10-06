# Chainning method
class HashMap:
    def __init__(self):
        self.bucket = 16
        self.hashmap = [[] for i in range(self.bucket)]
        
    def __str__(self):
        return str(self.__dict__)
    
    # Hash Function, A function that converts a key (usually a string) into an index where 
    # the corresponding value will be stored in the underlying array
    def hash(self, key):
        return len(key) % self.bucket
    
    def put(self, key, value):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)): # For loop: Iterates through the bucket to check if the key already exists. If it does, the corresponding value is updated.
            if reference[i][0] == key: # checks if the key already exists.
                reference[i][1] = value # updates the value if the key is found.
                return None
        reference.append([key, value])
        return None
        
    def get(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for pair in reference:
            if pair[0] == key:
                return pair[1]
        return -1
    
    def delete(self, key):
        hash_value = self.hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None
    
h = HashMap()
h.put("grapes", 100)
h.put("apples", 200)
h.put("kiwi", 20)
print(h.get("grapes"))
print(h.get("apples"))
print(h.get("kiwi"))
h.delete('kiwi')
print(h)
        