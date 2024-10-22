class List:
    def __init__(self, capacity=7):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity // 4:
            self.resize(self.capacity // 2)

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __len__(self):  
        return self.size

    def __str__(self): 
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


if __name__ == "__main__": 
    array_list = List()
    array_list.add(10)
    array_list.add(20)
    array_list.add(30)
    array_list.add(40)
    array_list.add(50)
    array_list.add(60)
    array_list.add(70)

    print("Array List after additions:", array_list)

    array_list.remove(1) 
    print("Array List after removal:", array_list)

    print("Element at index 1:", array_list.get(1)) 
    print("Current size of the array list:", len(array_list))
