class Node:
    def __init__(self,data=None):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_head(self,data):
        if self.head:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = Node(data)
    def insert(self,data):
        if self.head == None:
            self.insert_head(data)
        else:
            cursor = self.head
            while cursor.next:
                cursor=cursor.next
            cursor.next = Node(data)
    def printLL(self):
        cursor = self.head
        while(cursor):
            print(cursor.data)
            cursor = cursor.next
    def remove(self,target):
        cursor = self.head
        if cursor.data == target:
            self.head = cursor.next
            return 
        while cursor.next:
            prev = cursor
            cursor = cursor.next
            if cursor.data == target:
                prev.next = cursor.next
    def remove_dups(self):
        cursor = self.head
        H = dict()
        while cursor:
            if cursor.data in H:
                self.remove(cursor.data)
            else:
                H[cursor.data] = True
            cursor=cursor.next

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
data = LinkedList()
data.head = Node(1)
# data.insert_head(2)
# data.insert_head(3)
# data.insert_head(4)
# data.insert_head(5)
# data.insert(0)
# data.insert(1)
data.insert(0)
data.insert(0)
data.insert(0)
data.insert(0)
data.remove_dups()
data.printLL()
