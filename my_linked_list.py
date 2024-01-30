from tkinter import N


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self, head = None, next = None):
        self.head = head
        self.next = next

    
    def push_front(self, data):
        self.next = self.head
        self.head = Node(data, self.next)
        # return new_node
    
    def pop_front(self):
        if self.head != None:
            return_value = self.head.data
            new_head = self.head.next
            self.head = new_head
            return return_value
    
    def push_back(self, data):
        head = self.head
        while True:
            if head == None:
                head = Node(data)
                self.head = head
                break
            elif head.next == None:
                head.next = Node(data)
                break
            head = head.next

    def pop_back(self):
        head = self.head
        while head != None:
            if head.next == None:
                return_value = head.data
                self.head = None
                self.next = None
            elif head.next.next == None:
                return_value = head.next.data
                head.next = None
            head = head.next
        return return_value
       

    def get_size(self):
        counter = 0
        head = self.head
        while head != None:
            counter += 1
            head = head.next            
        return counter

    def __str__(self):
        string = ""
        n = self.head
        while n != None:
            string += str(n.data) + " "
            n = n.next
        return string                   
            

    def print_recursive(head):
        n = head
        if n != None:
            print(n.data, end=" ")
            LinkedList.print_recursive(n.next)

print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_back())
print(lis.pop_back())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_back())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)