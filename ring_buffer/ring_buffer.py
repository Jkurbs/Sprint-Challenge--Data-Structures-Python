
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
            last_node = self.head.next_node.next_node.next_node.next_node
            new_node.next_node = self.head.next_node
            last_node.next_node = new_node
            self.head = new_node
            return 

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
        arr = []
        while current_node: 
            print(current_node.value)
            arr.append(current_node.value)
            print("array: ", arr)
            current_node = current_node.next_node
            if current_node == self.head: 
                break
        return arr

if __name__ == "__main__":
    ring = RingBuffer(5) 
    ring.append("a")
    ring.get()
