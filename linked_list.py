class Node:
    def __init__(self, value: str = None)-> None:
        self.data = value
        self.next = None
   
class Linklist:
    def __init__(self) -> None:
        self.head = None  # root = head
        self.tail = None
        self.size = 0
    
    def append(self, value : str) -> None:
        new_node = Node(value)
        self.size += 1
        if self.head != None:
            self.tail.next = new_node
            self.tail = new_node
            return
        self.head = self.tail = new_node
        
    def prepend(self, value: str) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at(self, *args) -> None:
        index, value = args[0], args[1]
        if index == 0:
            return self.prepend(value)
            
        elif index == self.size:
            print("Invalid Index - Index out of range")
            return
        count = 0
        currentNode = self.head
        prevNode = None
        while currentNode:
            if index == count:
                break
            prevNode = currentNode
            currentNode = currentNode.next
            count += 1

        new_node = Node(value)
        temp = prevNode.next
        prevNode.next = new_node
        new_node.next = temp
        self.size += 1
    
    def remove(self, item):
        if self.head == None:
            return "Empty link list"
        
        if self.head.data == item:
            return self.pop_head()
        
        currentNode = self.head
        while currentNode:
            if currentNode.next.data == item:
                print(f"Found Data and Deleted = {currentNode.next.data}")
                break
            currentNode = currentNode.next
            if currentNode.next == None:
                print("Data not found")
                return
        currentNode.next = currentNode.next.next
        self.size -= 1
        
        
    def pop_head(self):
        if self.head == self.tail == None:
            return "Empty link list"
        self.head = self.head.next
        self.size -= 1

    def pop(self) -> None:
        if self.head == None:
            return "Empty Link List"

        currentNode = self.head
        
        if currentNode.next == None:
            return self.pop_head()
        
        while currentNode.next.next != None:  
            currentNode = currentNode.next

        self.tail = currentNode
        currentNode.next = None
        self.size -= 1
    
    def search(self, value):
        index = 0
        currentNode = self.head
        while currentNode:
            if currentNode.data == value:
                return index-1 
            index += 1
            currentNode = currentNode.next
        return "Not found"
    
    def __getitem__(self, index):
        position = 0
        currentNode = self.head
        while currentNode:
            if position == index:
                return currentNode.data
            position += 1
            currentNode = currentNode.next
        return "Index Error"
        
    def __str__(self):
        lst1 = ""
        if self.head is None:
            return "Empty link list"
        currentNode = self.head
        while currentNode:
            lst1 += str(currentNode.data)+"->"
            currentNode = currentNode.next
        return lst1[:-2]
       
    def __len__(self) -> int:
        return self.size
    
    def clear(self) -> None:
        self.head = None
        self.size = 0
    
    def reverse(self) -> None:
        prev_node = None
        current_Node = self.head
        while current_Node:
            temp_node = current_Node.next
            current_Node.next = prev_node
            prev_node = current_Node
            current_Node = temp_node
        self.head = prev_node

    def replace_max(self, value):
        current_Node = self.head
        max_value = current_Node

        while current_Node:
            if current_Node.data > max_value.data :                
                max_value = current_Node
            current_Node = current_Node.next
        max_value.data = value

if __name__ == "__main__":
    node = Linklist()
    node.append(45)
    node.append(2)
    node.append(3)
    node.append(4)
    node.append(50)

    print(node)
    # # node.clear()
    # print(node)
    # #node.pop_head()
    # # node.remove(1)
    # # node.remove(1)
    # # node.remove(2)
    # node.remove(30)
    # print(node)
    # node.remove(1)
    # # print("size",len(node))
    # print(node)
    # print(node.search(5))
    # print(node[2])
    # node.reverse()
    node.replace_max(58)
    print(node)