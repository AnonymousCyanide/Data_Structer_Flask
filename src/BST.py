class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    
    def _insert_recursive(self,data,node):
        if node.data['id'] > data['id']:
            if node.left == None:
                node.left = Node(data)
            else :
                self._insert_recursive(data,node.left)
        elif data['id'] > node.data['id']:
            if node.right == None:
                node.right = Node(data)
            else :
                self._insert_recursive(data,node.right)
        else:
            return
            
                
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else :
            self._insert_recursive(data,self.root)
    def _search_recursive(self,id,node):
        if id == node.data['id']:
            return node.data
        if node.left == None and node.right == None:
            return False
        if id < node.data['id']:
            if id == node.left.data['id']:
                return node.left.data
            return self._search_recursive(id,node.left)
        if id > node.data['id']:
            if id == node.right.data['id']:
                return node.right.data
            return self._search_recursive(id,node.right)
        
    def search(self,id):
        id = int(id)
        if self.root is None :
            return False
        return self._search_recursive(id,self.root)
        