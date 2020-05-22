
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
# Used a double-Linked list here


class LRUCache:
    def __init__(self, cap):
        # Initializing Class Variables
        self.hash_map = dict()
        self.cap = cap
        self.head = Node(0 ,0)
        self.tail = Node(0 ,0)
        # Linking head and tail next to each other and initialized each with key = 0 & value = 0
        self.head.next = self.tail
        self.tail.previous = self.head
                  
    def get(self, key):
        # Retrieve item from provided key. and return -1 if key not found in hash_map
        if key not in self.hash_map:
            return -1
                
        if key in self.hash_map:
            node = self.hash_map[key]
            self.delete(node)
            self._insert(node)
            return node.value
        
    def set(self, key, value):
        # Checking if the key is already present is hash_map
        if key in self.hash_map:
            self.delete(self.hash_map[key])
        
        if key not in self.hash_map:
            node = Node(key, value)
            # Created a new node with given key and value
            self._insert(node)
            self.hash_map[key] = node
        # If the cache is at capacity remove the oldest node
        if len(self.hash_map) > self.cap:
            node = self.head.next 
            self.delete(node)
            
            if node.key is None:
                del self.hash_map[node.key]
                            
    def delete(self, node):
        if self.head is None or node is None:
            return 
        
        if self.head == node:
            self.head = node.next
            
        if node.next is not None:
            node.next.previous = node.previous
        
        if node.previous is not None:
            node.previous.next = node.next
            
    def _insert(self, node):
        node.next = self.head
        node.previous = None

        if self.head is not None:
            self.head.previous = node
        self.head = node


# Test Case 1
cache1 = LRUCache(5)  #Consedring the size of cache=5
cache1.set(1, 3)
cache1.set(2, 4)
print( cache1.get(1))
print( cache1.get(2))
print( cache1.get(3))
cache1.set(3, 5)
print( cache1.get(2))
cache1.set(4, 5)
print(cache1.get(1))
print(cache1.get(3))
cache1.set(3, 6)
print( cache1.get(3))

