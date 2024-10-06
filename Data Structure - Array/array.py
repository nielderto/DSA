class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
                
    def get(self, index):
        return self.data[index]
    
    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length-1]
        return last_item
    
    def delete(self, index):
        deleted_item = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
            
        del self.data[self.length - 1]
        self.length -= 1
        return deleted_item
    

arr=Array()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
arr.delete(0)
print(arr)