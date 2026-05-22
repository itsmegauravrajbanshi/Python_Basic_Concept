from linked_list import Node, Linklist

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def is_Empty(self):
        return self.top == None
    
    def push(self, item):
        new_node = Node(item)
        self.size += 1
        if self.top == None:
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if not self.is_Empty():
            return self.top.data
        return "Stack is empty"
    def pop(self):
        if self.is_Empty():
            print("Stack is Empty")
            return
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def __len__(self):
        return self.size

    def __str__(self):
        current_Node = self.top
        text = ""
        while current_Node:
            text += str(current_Node.data)+"\n"
            current_Node = current_Node.next
        return text[:-1]

    def reverse(self, text):
        for c in text:
            q1.push(c)
        print(q1.is_Empty())
        print(q1)
        temp = ""
        while not q1.is_Empty():
            temp = temp + q1.pop()
        print(temp)
    
    def text_editor(self, action, text):
        stack1 = Stack()
        stack2 = Stack()
        for i in text:
            stack1.push(i)
    
        for a in action:
            if a == 'u':
                stack2.push(stack1.pop())
            elif a == 'r':
                stack1.push(stack2.pop())
        print(stack1)

    def balance(self, text):
        stack1 = Stack()
        j = None
        for i in text:
            if j =="(" and i == ")" or j =="[" and i =="]" or j =="{" and i =="}":
                stack1.pop()
                j = stack1.peek()
                continue
            stack1.push(i)
            j = i
        if stack1.is_Empty():
            print("Balance Parentheses")
        else:
            print("Not Balance")

    def valid_parenthese(self, text):
        j = None
        lst = []
        for i in text:
            if j == "(" and i == ")" or j == "{" and i == "}" or j == "[" and i == "]":
                if len(lst) == 1:
                    lst.pop()
                    j = None
                    continue
                
                lst.pop()
                j = lst[-1]
                continue
            lst.append(i)
            j = i
        if lst:
            print("Not Balance")
        else:
            print("Balance")
stack = Stack()
# # q1.reverse(text)
# q1.text_editor('uuuu','kolkata')
text = "(){}{}"
stack.balance(text)
stack.valid_parenthese(text)

