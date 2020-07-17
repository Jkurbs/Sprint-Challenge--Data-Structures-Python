
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.data = []
        self.index = 0 

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.index] = item
        self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        print(self.data)
        return self.data

# sample usage
if __name__=='__main__':
    buffer=RingBuffer(3)
    
    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')

    print(buffer.get())
