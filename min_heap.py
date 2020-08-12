# Author: Amy Salley
# Description: Implementation of a Min Heap data structure


# Import DynamicArray and LinkedList classes
from sll_and_da_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property
        Runtime complexity is O(logN)
        """
        self.heap.append(node)
        length = self.heap.length()

        child_index = length - 1
        parent_index = (child_index - 1) // 2

        parent = self.heap.get_at_index(parent_index)

        # Move node up the tree to the correct location
        while parent_index >= 0:

            if node < parent:
                self.heap.swap(parent_index, child_index)
                child_index = parent_index
                parent_index = (parent_index - 1) // 2
                parent = self.heap.get_at_index(parent_index)

            else:
                return

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap
        Runtime complexity is O(1)
        """
        if self.is_empty():
            raise MinHeapException

        # Get the first value in the Dynamic Array
        min_key = self.heap.get_at_index(0)

        return min_key

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap
        Runtime complex is O(logN)
        """
        # Raise exception for an empty heap
        if self.is_empty():
            raise MinHeapException

        # Get the minimum value from the beginning of the Dynamic Array
        min_key = self.heap.get_at_index(0)
        length = self.heap.length()

        # Swap first and last values
        self.heap.swap(0, length - 1)
        self.heap.pop()
        length = length - 1

        # Return minimum value if the heap is now one item or empty
        if length <= 1:
            return min_key

        # Move the new value at the top of the heap to the correct position
        parent_index = 0
        parent = self.heap.get_at_index(0)

        child_index1 = 2 * parent_index + 1
        child_index2 = 2 * parent_index + 2

        # Find the value of the left child
        if child_index1 < length:
            child1 = self.heap.get_at_index(child_index1)
        else:
            return min_key

        # Find the value of the right child
        if child_index2 < length:
            child2 = self.heap.get_at_index(child_index2)
        else:
            child2 = child1

        # Compare child values and select the minimum
        if child1 <= child2:
            child = child1
            child_index = child_index1
        else:
            child = child2
            child_index = child_index2

        while parent > child:
            self.heap.swap(parent_index, child_index)
            parent_index = child_index

            child_index1 = 2 * parent_index + 1
            child_index2 = 2 * parent_index + 2

            # Find the value of the left child
            if child_index1 < length:
                child1 = self.heap.get_at_index(child_index1)
            else:
                return min_key

            # Find the value of the right child
            if child_index2 < length:
                child2 = self.heap.get_at_index(child_index2)
            else:
                child2 = child1

            # Compare child values and select the minimum
            if child1 <= child2:
                child = child1
                child_index = child_index1
            else:
                child = child2
                child_index = child_index2

        return min_key

    def build_heap(self, da: DynamicArray) -> None:
        """
        Takes a Dynamic Array as a parameter and builds a proper Min Heap
        Runtime complexity is O(N)
        """
        # Initialize the new Dynamic Array
        new_heap = DynamicArray()

        array_length = da.length()
        last_index = array_length - 1

        # Copy data to the new Dynamic Array
        for i in range(array_length):
            new_heap.append(da.get_at_index(i))

        tree_counter = (last_index - 1) // 2

        # Move the nodes to the correct location
        while tree_counter >= 0:

            parent_index = tree_counter
            child_index1 = 2 * parent_index + 1
            child_index2 = 2 * parent_index + 2

            while child_index1 < array_length:
                parent = new_heap.get_at_index(parent_index)
                child1 = new_heap.get_at_index(child_index1)

                if child_index2 < array_length:
                    child2 = new_heap.get_at_index(child_index2)
                else:
                    child2 = child1

                if child1 <= child2:
                    child = child1
                    child_index = child_index1
                else:
                    child = child2
                    child_index = child_index2

                if parent > child:
                    new_heap.swap(parent_index, child_index)

                parent_index = child_index
                child_index1 = 2 * parent_index + 1
                child_index2 = 2 * parent_index + 2

            # Move up the tree to the next node
            tree_counter = tree_counter - 1

        self.heap = new_heap
