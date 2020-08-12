# Author: Amy Salley
# Description: Hash Map data structure implementation with a Dynamic Array
# hash table and Singly Linked Lists for collision resolution


# Import DynamicArray and LinkedList classes
from sll_and_da_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on Dynamic Array with Singly Linked List
        for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the content of the hash map without changing the underlying hash table capacity
        """
        for i in range(self.capacity):
            # Find the Linked List at each index
            list_at_index = self.buckets.get_at_index(i)

            # Remove each node
            for node in list_at_index:
                list_at_index.remove(node.key)
                self.size = self.size - 1

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key.
        Returns None if the key does not exist.
        """
        for i in range(self.capacity):
            # Find the Linked List at each index
            list_at_index = self.buckets.get_at_index(i)

            # See if the list contains the key
            node = list_at_index.contains(key)
            if node:
                return node.value

        return None

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If the given key already exists
        in the hash map, the value is replaced with the new value.
        """
        # Calculate index of Hash Table
        index = self.hash_function(key) % self.capacity

        # Find the Linked List at the index
        list_at_index = self.buckets.get_at_index(index)

        # Check if the key already exists
        node = list_at_index.contains(key)

        # If the key exists, replace the value
        if node:
            # node.value = value
            list_at_index.remove(key)
            list_at_index.insert(key, value)

        # If the key does not exist, insert the Node and increase the size
        else:
            list_at_index.insert(key, value)
            self.size = self.size + 1

        # Update the Hash Table
        self.buckets.set_at_index(index, list_at_index)

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the hash map
        """
        for i in range(self.capacity):
            # Find the Linked List at each index
            list_at_index = self.buckets.get_at_index(i)

            # See if the list contains the key
            node = list_at_index.contains(key)

            # If the key is found, remove the node and decrease the size
            if node:
                list_at_index.remove(node.key)
                self.size = self.size - 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map. Otherwise returns False.
        """
        for i in range(self.capacity):
            # Find the Linked List at each index
            list_at_index = self.buckets.get_at_index(i)

            if list_at_index.contains(key):
                return True

        return False

    def empty_buckets(self) -> int:
        """
        Returns a number of empty buckets in the hash table
        """
        count = 0

        # Check the length of each Linked List in the Dynamic Array
        # If the list length is zero, the bucket is empty
        for i in range(self.capacity):
            length = self.buckets.get_at_index(i).length()
            if length == 0:
                count = count + 1

        return count

    def table_load(self) -> float:
        """
        Returns the current hash table load factor
        """
        load = self.size/self.capacity
        return load

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table.  All existing key/value
        pairs remain in the new hash map, and all hash table links are rehashed.
        """
        if self.capacity < 1:
            return

        # Initialize a new hash table
        new_buckets = DynamicArray()

        for i in range(new_capacity):
            new_buckets.append(LinkedList())

        # Copy the contents of the old hash map to the new hash map
        for j in range(self.capacity):

            list_at_index = self.buckets.get_at_index(j)

            for item in list_at_index:
                # Calculate the new index for each item
                new_index = self.hash_function(item.key) % new_capacity

                # Create the new Linked List
                new_list = new_buckets.get_at_index(new_index)

                # Insert the node to the new Linked List
                new_list.insert(item.key, item.value)

                # Update the new hash table
                new_buckets.set_at_index(new_index, new_list)

        # Update the capacity and the hash table
        self.capacity = new_capacity
        self.buckets = new_buckets

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stored in the hash map
        """
        key_array = DynamicArray()

        for i in range(self.capacity):
            # Find the Linked List at each index
            list_at_index = self.buckets.get_at_index(i)

            # Append each key to the Dynamic Array
            for node in list_at_index:
                key_array.append(node.key)

        return key_array

