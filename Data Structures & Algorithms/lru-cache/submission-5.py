class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    #initialize and set up head and tail dummy pointers
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    
    #insert at tail prev backwards from right to left
    def insert(self, node) -> None:
        prev, next = self.tail.prev, self.tail

        prev.next = node
        next.prev = node
        node.prev, node.next = prev, next


# 0 - 10 - 20 - 30 - 0
#     0 - 0
    #remove at head
    def remove(self, node) -> None:
        prev, next = node.prev, node.next
    
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            res = self.cache.get(key)
            self.remove(res)
            self.insert(res)
            
            return res.val
            
        return -1
    


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        