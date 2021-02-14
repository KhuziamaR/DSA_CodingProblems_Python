class TreeNode:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data > self.data:
                if self.right == None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
            elif data < self.data:
                if self.left == None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data
    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

root = TreeNode(1)
root.insert(4)
root.insert(2)
root.insert(2)
root.insert(3)
root.insert(5)


# root.print_tree()
root.delete(1)
# print('/n')
root.print_tree()
    

