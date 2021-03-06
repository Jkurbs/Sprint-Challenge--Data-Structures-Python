class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    

    def append(self, value): 
        if self.head is None:
            new_node = Node(value)
            self.head = new_node 
            return
        else: 
            new_node = Node(value)
            current_node = self.head
            while current_node.next_node: 
                current_node = current_node.next_node 
            current_node.next_node = new_node 
            new_node.next_node = None

    def contains(self, value):
        if not self.head:
            return False
        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def reverse_list(self, node, prev):
        if node is None:
            self.head = prev
            return

        next = node.get_next()
        node.set_next(prev)
        self.reverse_list(next, node)


    def print_list(self): 
        current_node = self.head 
        while current_node: 
            
            print("Node: ", current_node.value)
            current_node = current_node.next_node

linkedList = LinkedList() 
linkedList.add_to_head(5)
linkedList.append(3)
linkedList.append(4)
linkedList.reverse_list(linkedList.head, None)
linkedList.print_list()


