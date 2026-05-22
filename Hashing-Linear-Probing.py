# class Dictionary:
#     def __init__(self, size):
#         self.size = size
#         self.array_of_value = [None] * self.size
#         self.array_of_slot = [None] * self.size

#     def put(self, key, value):
#         hash_value = self.hash_function(key)
#         if self.array_of_slot[hash_value] == None:
#             self.array_of_slot[hash_value] = key
#             self.array_of_value[hash_value] = value
#         else:
#             if self.array_of_slot[hash_value] == key:
#                 self.array_of_value[hash_value] = value
#             else:
#                 new_hash = self.rehash(hash_value)
#                 while self.array_of_slot[new_hash] != None and self.array_of_slot[new_hash] != key:
#                     new_hash = self.rehash(new_hash)
#                 if self.array_of_slot[new_hash] == None:
#                     self.array_of_slot[new_hash] = key
#                     self.array_of_value[new_hash] = value
#                 else:
#                     self.array_of_value[new_hash] = value

#     def rehash(self, old_hash):
#         return (old_hash + 1) % self.size
    
#     def hash_function(self, key):
#         return abs(hash(key)) % self.size
    
#     def __setitem__(self, key, value):
        # self.put(key, value)
    
# print(hash("Python"))  # Returns a unique integer
# print(hash(10))        # Returns 10 (integers hash to themselves)

class Dictionary:
    def __init__(self, size : int) -> None:
        self.size = size
        self.array_of_key = [None] * self.size
        self.array_of_value = [None] * self.size
    
    def __setitem__(self, key : str, value : str) -> None:
        index = self.hashing(key)
        if self.array_of_key[index] == None:
            self.array_of_key[index] = key
            self.array_of_value[index] = value
        else:
            if self.array_of_key[index] == key:
                self.array_of_value[index] = value  
            else:
                new_index  = self.rehasing(index)            
                while self.array_of_key[new_index] and self.array_of_key[new_index] != key:
                    new_index = self.rehasing(new_index)
                
                if self.array_of_key[new_index] == None:
                    self.array_of_key[new_index] = key
                    self.array_of_value[new_index] = value
                else:
                    self.array_of_value = value

    def __getitem__(self, key):
        start_position = self.hashing(key)
        current_position = start_position
        while self.array_of_key[current_position]:
            if self.array_of_key[current_position] == key:
                return self.array_of_value[current_position]
            current_position = self.rehasing(current_position)
            if current_position == start_position:
                return "Not found"
        return "Not found/Empty"
    
    def rehasing(self, index) -> int:
        return (index + 1) % self.size
    
    def hashing(self, key: str) -> int:
        return abs(hash(key)) % self.size
    
    def __str__(self):
        text = ""
        for i in range(self.size):
            if self.array_of_key[i] != None:
                text += f"'{self.array_of_key[i]}' : {self.array_of_value[i]}, "
        return "{"+text[:-2]+"}"
        
d1 = Dictionary(3)

d1['a'] = 59
d1['b'] = 100
d1['c'] = 34

print(d1.array_of_key)
print(d1.array_of_value)

print(d1)

print(d1['d'])