class Node:
    def __init__(self, data, val):
        self.data = data      # key
        self.val = val        # value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Dummy head and tail nodes
        self.dumm1 = Node(0, 0)
        self.dumm2 = Node(0, 0)

        self.dumm1.next = self.dumm2
        self.dumm2.prev = self.dumm1

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert right after head (Most Recently Used)

        first_node = self.dumm1.next

        self.dumm1.next = node
        node.prev = self.dumm1

        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.cap:

            lru_node = self.dumm2.prev

            self.remove(lru_node)
            del self.cache[lru_node.data]