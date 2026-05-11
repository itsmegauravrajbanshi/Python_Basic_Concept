import ctypes

class PythonList:
    def __init__(self) -> None:
        self.n : int = 0
        self.size : int = 1
        self.Array_A : list[str] = self.__make_array(self.size)

    def __make_array(self, capacity: int) -> None:
        return (capacity * ctypes.py_object)()
    
    def __resize(self, new_capacity) -> None:
        B : list[str] = self.__make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.Array_A[i]

        self.Array_A = B

    def __len__(self) -> int:
        return self.n

    def append(self, item) -> None:
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.Array_A[self.n] = item
        self.n = self.n + 1

    def __str__(self) -> str:
        result : str = ""
        for i in range(self.n):
                if type(self.Array_A[i]) == str:
                    result = result + f"'{str(self.Array_A[i])}',"
                else:
                    result = result + f'{str(self.Array_A[i])},'
        return f"[{result[:-1]}]"

    def __getitem__(self, index) -> str:
        if 0 <= index < self.n:
            return self.Array_A[index]
        else:
            return "Array out of index"

    def pop(self) -> None:
        if self.n == 0:
            return "Empty list"

        print(self.Array_A[self.n-1])
        # self.Array_A[self.n] = None
        self.n = self.n - 1
        
    
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, *args):
        item : str = args[0]
        for i in range(self.n):
             if self.Array_A[i] == item:
                return i 
        return f"{item} is not in the list."
    
    def insert(self, index, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        
        for i in range(self.n, index, -1 ):
            self.Array_A[i] = self.Array_A[i-1]
        
        self.Array_A[index] = item
        self.n += 1
        
    def __delitem__(self, index) -> None:
        if 0 <= index < self.n:
            for i in range(index, self.n-1):
                self.Array_A[i] = self.Array_A[i+1]
            self.n -= 1

    def remove(self, item) -> None:
        temp_index = self.find(item)
        if type(temp_index) == int:
            self.__delitem__(temp_index)
        else:
            print(temp_index)
    
    def sort(self) -> None:
        for i in range(self.n):
            for j in range(self.n):
                if self.Array_A[i] > self.Array_A[j]:
                    temp = self.Array_A[i]
                    self.Array_A[i] = self.Array_A[j]
                    self.Array_A[j] = temp


mylist : PythonList = PythonList()
mylist.append(10)
mylist.append(29)
mylist.append(2.5)
mylist.append(False)
mylist.append("Tree")
print(mylist)

# mylist[3]

# mylist.pop()
# print(mylist)

# print(mylist.find(29))

# print(mylist)
# mylist.clear()

# mylist.insert(0,'insert')
del mylist[0]
mylist.remove(200)
print(mylist)

    
        