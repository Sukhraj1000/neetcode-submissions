# Define a Node class to hold key, value and pointers to next and previous nodes
class Node:
    def __init__(self, key, val):
        self.key = key              # Store the key
        self.val = val              # Store the value
        self.prev = None            # Pointer to the previous node (for doubly linked list)
        self.next = None            # Pointer to the next node
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity         # Maximum number of items allowed in cache
        self.cache = {}             # Hashmap to store key -> Node

        # Create left (LRU) and right (MRU) dummy nodes
        self.left = Node(0, 0)      
        self.right = Node(0, 0)

        # Connect the dummy nodes together
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert a node right before the right dummy (MRU end)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    # Get the value if the key exists in cache
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])     # Remove it from its current spot
            self.insert(self.cache[key])     # Reinsert it at the MRU position
            return self.cache[key].val
        return -1

    # Put a key-value pair into the cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])     # Remove old node if already exists

        self.cache[key] = Node(key, value)   # Create new node and store in hashmap
        self.insert(self.cache[key])         # Insert it at the MRU position

        if len(self.cache) > self.cap:       # If we exceed capacity
            lru = self.left.next             # LRU is next to the left dummy
            self.remove(lru)                 # Remove from list
            del self.cache[lru.key]          # Remove from hashmap
