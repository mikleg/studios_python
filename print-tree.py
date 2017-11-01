class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value == val:
            return
        elif val < self.value:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def search(self, val):
        if self.value == val:
            return True
        elif val < self.value:
            if self.left is not None:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.search(val)
            else:
                return False

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.value)
        if self.right is not None:
            self.right.print()


node = Node(5)

node.insert(4)

node.insert(9)

node.print()