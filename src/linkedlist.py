class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node 
         

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        self.size = 0
    def print_ll(self):
        s = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            s += f' {str(node.data)} ->'
            if node.next_node is None:
                s+= ' None'
            node = node.next_node
        print('size = '+str(self.size))
        print(s)
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data,None)
            self.last_node = self.head
            self.size += 1
        else:
            new_node = Node(data,self.head)
            self.head = new_node
            self.size += 1
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_beginning(data)
        '''if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = Node(data,None)
            self.last_node = node.next_node
            self.size += 1
        else :'''
        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node
        self.size += 1
    def to_array(self):
        arr = []
        if self.head is None:
            return arr
        else:
            node = self.head
            arr.append(node.data)
            while node.next_node:
                node = node.next_node
                arr.append(node.data)
                
            return arr
if __name__ == '__main__':
    a = LinkedList()
    a.insert_beginning('a')
    a.insert_beginning('b')
    a.insert_beginning('c')
    a.insert_beginning('d')
    a.insert_beginning('e')
    a.insert_at_end('z')
    a.print_ll()
    print(a.to_array())    
            
        