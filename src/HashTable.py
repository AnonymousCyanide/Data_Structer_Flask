class Node :
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
class Data :
    def __init__(self , key , value):   
        self.key = key
        self.value = value
        
class HashTable :
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * self.table_size
    def make_hash(self,key):
        hash = 0
        for i in key :
            hash += ord(i)
            hash = (hash *ord(i)) % self.table_size
        return hash
    def add_key_value(self, key , value):
        hash = self.make_hash(key)
        if self.hash_table[hash] == None:
            self.hash_table[hash] = Node(Data(key,value),None)
        else:
            node = self.hash_table[hash]
            while node.next_node :
                node = node.next_node
            node.next_node = Node(Data(key , value),None)
    def get_value(self, key):
        hash = self.make_hash(key)
        
        if self.hash_table[hash] != None:
            node = self.hash_table[hash]
            if node.data.key == key:
                return node.data.value
            else:
                while node.next_node:
                    if node.data.key == key:
                        return node.data.value
                    node = node.next_node
                if node.data.key == key:
                    return node.data.value
        else :
            pass
    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")
        
if __name__ == '__main__':
    ht = HashTable(4)
    ht.add_key_value('hi','there')
    ht.print_table()
    print(ht.get_value('hi'))
        