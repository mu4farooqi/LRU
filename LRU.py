from collections import OrderedDict

"""
I have written Two implementations for LRU cache. First solution is implemented using Doubly LinkedList and HashTable
 and Second is implemented using in-built OrderDict Library of Python
"""


class Node(object):
    """
    Node is a single Node of Doubly Linked List
    """
    def __init__(self, key, value, next=None, prev=None):
        """
        This is initializer of a node of Doubly Linked List
        :param key: `key` part of Data
        :param value: `value` part of Data
        :param next: Next node in the Linked List 
        :param prev:  Previous Node in Linked List
        """
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache(object):
    """
    LRU is a cache data structure which is the backbone of Paging Algorithms in Operating Systems. As OS use very fast 
    and hence expensive cache memory to store pages so LRU algorithm helps in that scenario to make turnaround time
    as fast as possible
    """
    def __init__(self, size):
        """
        In initializer, we'll set size. hash table and doubly linked list
        :param size: Maximum Size of LRU Cache
        """
        self.size = 0
        self.head = None
        self.tail = None
        self.hash = dict()
        self.max_size = size

    def get(self, key):
        """
        This method will check if the key is present in cache. If it's there it'll first move that key to the start of
        the cache i.e. will make it as Most Recently Used and then will return the corresponding value
        Time Complexity: O(1)
        :param key: Key for which we'll search in cache.
        :return: 
        """
        if self.max_size != 0 and key in self.hash:
            self.move_to_start(self.hash[key])
            return self.hash[key].value
        return -1

    def put(self, key, value):
        """
        This method will do the following
            --> If key is already there, it'll move it in the start of cache and will update its value
            --> If key is not there already, it'll just add it in the cache in the start
            --> If size of cache exceeds maximum cache size, it'll remove least recently used key
        Time Complexity: O(1)
        :param key: Key of the data which is going to be inserted in Cache
        :param value: Value of the data which is going to be inserted in Cache
        :return: 
        """
        if self.max_size == 0:
            return -1

        if not self.head:
            self.head = Node(key=key, value=value)
            self.tail = self.head
            self.hash[key] = self.head
            self.size += 1
            return

        if key not in self.hash:
            new_node = Node(key=key, value=value, next=self.head)
            self.head.prev = new_node
            self.head = new_node
            self.hash[key] = self.head
            self.size += 1
        else:
            self.move_to_start(self.hash[key])
            self.hash[key].value = value

        if self.size > self.max_size:
            self.tail.prev.next = None
            del self.hash[self.tail.key]
            self.tail = self.tail.prev
            self.size -= 1

    def move_to_start(self, node):
        """
        It's a utility method, which will delete a node from a doubly linked list and move it to the front of List
        and make it as head
        Time Complexity: O(1)
        :param node: Node which is going to be removed and made head
        :return: 
        """
        if node.prev:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            node.next = self.head
            self.head.prev = node
            node.prev = None

        self.head = node


class LRUCacheLibrary(object):
    """
    This is LRUCache implementation using Python in-built Order Dict Library. That's why it's fast, efficient and have
    short code too. Big O time for both of these implementations is same.
    """

    def __init__(self, size):
        """
        In this method, we are initializing cache (using OrderedDict) and max_size
        Time Complexity: O(1)
        :param size: Maximum size of LRU cache
        """
        self.cache = OrderedDict()
        self.max_size = size

    def get(self, key):
        """
        If key is present in OrderedDict, this method will pop it and will insert it again (To make it most recently used)
        and then will return the corresponding value
        Time Complexity: O(1)
        :param key: Key to be retrieved
        :return: 
        """
        if self.max_size != 0 and key in self.cache:
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        This method will do following
            --> If key is already there, it'll pop it
            --> Will add the key to cache
            --> If key size has exceeded maximum size, it'll remove least recently used key
        Time Complexity: O(1)
        :param key: Key of the Data which is going to be inserted
        :param value: Value of the data which is going to be inserted
        :return: 
        """
        if self.max_size == 0:
            return -1

        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)



