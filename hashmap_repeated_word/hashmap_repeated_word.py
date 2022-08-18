class Node:
    """
    Node Instructor.
    This class will have only an __init__ method to create nodes.
    """

    def __init__(self, value, next=None):
        """
        Node Constructor.
            :param value: value of the node
            :param next: reference of next node in line
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Singly linked list constructor.
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
            :param value: Value to insert
            :return: None
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        """
        This function is used to print the entire liked list in a
        specific format.
        :return: String
        """
        temp_list = ''
        current = self.head

        while current:
            temp_list += f"{{ {current.value} }} -> "
            current = current.next

        temp_list += "NULL"
        return temp_list


class HashTable:
    """
    HashTable class will have multiple methods, set, get,
    contains, keys and hash.
    It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
    """

    def __init__(self, size=1024):
        """
        HashTable constructor.
            :param size: the size of the data structure
        """
        self.__size = size
        self.__buckets = [None] * size
        self.__keys = []

    def __hash(self, key):
        """
        This method returns the index in the collection of buckets for that key
            :param key: key to reference can be string, number, etc...
            :return: number
        """

        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        """
        this method will  hash the key and set the value and key pair in the buckets, also handling the collisions as needed.
            :param key: key to reference can be string, number, etc...
            :param value: value of the referenced key
            :return: None
        """

        h_key = self.__hash(key)
        if self.__buckets[h_key] is None:
            h_list = LinkedList()
            self.__buckets[h_key] = h_list
        self.__keys.append(key)
        self.__buckets[h_key].insert((key, value))


    def get(self, key):
        """
        Used to find the value that is associated with the passed key.
            :param key: Hash key
            :return: referenced value by passed key
        """
        value = []

        h_key = self.__hash(key)
        linked_list_in_buckets = self.__buckets[h_key]
        if linked_list_in_buckets is None:
            return None

        current = linked_list_in_buckets.head
        while current:
            if current.value[0] == key:

                value.append(current.value[1])
            current = current.next

        if len(value) > 1:
            return tuple(value)

        else:
            return value[0]

    def contains(self, key):
        """
        Used to find if the value is contained in the Hash Table or not.
            :param key: key to reference can be string, number, etc...
            :return: bool
        """

        if self.get(key):
          return True

        return False

    def keys(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        :return: an array
        """

        return self.__keys





def repeated_word(string):
    import re
    """
    This function finds the first repeated word within a given string.
    :param string: The string to check
    :return: string
    """
    if len(string.split(" ")) < 2:
        return string


    hash_table = HashTable()

    string = re.sub(r'[^\w\s]', '', string)

    string=string.lower()

    string_words = string.split(" ")

    for i in string_words:
        hash_table.set(i, "0")
        if len(hash_table.get(i)) > 1:
            return i


