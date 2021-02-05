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
    def length(self):
        cursor = self.head
        count = 0
        while cursor:
            count +=1
            cursor = cursor.next
        return count
    def kth_to_last(self,k):
        size = self.length()
        cursor = self.head
        for i in range(size):
            if i == size-k:
                return cursor.data
            cursor=cursor.next
def sum_lists(list1,list2):
    l1 = list1.head
    l2 = list2.head
    l3 = LinkedList()
    carry = 0
    while l1 or l2:  
        sum_nodes = l1.data + l2.data + carry
        carry = 0
        if sum_nodes >= 10:
            sum_nodes = sum_nodes %10
            carry+=1
            l3.insert(sum_nodes)
        else:
            l3.insert(sum_nodes)
        l1 = l1.next
        l2 = l2.next
    return l3
def palindrome_linked_list(list1):
    l1 = list1.head
    H = dict()
    count = 0
    while l1:
        if l1.data in H:
            H[l1.data] +=1
        else:
            H[l1.data] = 1
        count+=1
        l1= l1.next
    odd = 0
    for v in H.values():
        if v % 2 != 0:
            odd+=1
    if count % 2 == 0 and odd == 0:
        return True
    if count %2 !=0 and odd == 1:
        return True
    return False
    


    


    

data = LinkedList()
data.insert(0)
data.insert(0)
data.insert(2)
data2 = LinkedList()
data2.insert(5)
data2.insert(9)
data2.insert(2)
data3 = sum_lists(data,data2)
data3.printLL()
print(palindrome_linked_list(data))


