
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.head = None
        self.data = []
        pass

    class __Full:
        def append(self, item):
            self.data[self.cur] = item
            self.data[-1] = self.data[-1]
            self.cur = (self.cur+1) % self.capacity
        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        print(self.data)
        return self.data

# sample usage
if __name__=='__main__':
    buffer=RingBuffer(5)
    
    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    buffer.append('e')
    buffer.append('f')
    buffer.append('g')
    buffer.append('h')
    buffer.append('i')
    buffer.append('j')
    buffer.append('k')

    print(buffer.get())
