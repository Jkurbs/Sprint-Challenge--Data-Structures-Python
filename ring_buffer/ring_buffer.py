
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.head = None
        pass

    def append(self, item):
        self.size += 1 
        current_node = self.head
        new_node = Node(item)

        # Check for capacity 
        if self.size > self.capacity: 
            print("Full")
            while current_node.next_node: 
                current_node = current_node.next_node 
                print("Node:", current_node)
            new_node.next_node = self.head.next_node
            self.head = None
            current_node.next_node = new_node
            new_node = self.head  

        # Check if it's empty 
        elif not self.head:
            self.head = new_node
            new_node.next_node = self.head
        else: 
            while current_node.next_node != self.head: 
                current_node = current_node.next_node 
            current_node.next_node = new_node 
            new_node.next_node = self.head
            



    def get(self):
        current_node = self.head 
        while current_node: 
            print(current_node.value)
            current_node = current_node.next_node
            if current_node == self.head: 
                break

ring = RingBuffer(3) 

ring.append(0)
ring.append(1)
ring.append(2)
ring.append(3)

ring.get()