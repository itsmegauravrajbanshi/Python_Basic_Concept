from linked_list import Node
from linked_list import Linklist
import sys

l1 = Linklist()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

prevNode = None
currentNode = l1.head
while currentNode:
    temp = currentNode.next
    currentNode.next = prevNode
    prevNode = currentNode
    currentNode = temp
l1.head = prevNode

curr = l1.head
while curr:
    print(curr.data)
    curr = curr.next




