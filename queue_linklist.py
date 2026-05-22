from linked_list import Node

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.front == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.front == None:
            print("Empty queue")
            return
        temp = self.front.data
        self.front = self.front.next
        self.size += 1
        return temp

    def is_empty(self):
        return self.front == None
    
    def __str__(self):
        if self.front == None:
            return "Empty Queue"
        current_Node = self.front
        text = ""
        while current_Node:
            text += f"{current_Node.data} ->"
            current_Node = current_Node.next
        return text+"None"
    
    def reverse_digit(self, num):
        if num == 0:
            return 0
        else:
            self.enqueue(num%10)
            res = self.reverse_digit(num//10)
            return res * 10 + int(self.dequeue())
            
Q1 = Queue()
print(Q1.reverse_digit(123))

# Q1.enqueue(5)
# Q1.enqueue(6)
# Q1.enqueue(7)
# Q1.enqueue(9)

# Q1.dequeue()

# print(Q1)


            

