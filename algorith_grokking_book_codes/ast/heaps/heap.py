import math
from copy import deepcopy

class Heap:
    def __init__(self, elements=[], element_priority=lambda x: x):
        self.prioirty = element_priority
        if len(elements) > 0:
            self._heapify(elements)  # TODO implement
        else:
            self.elements = []

    def _has_lower_priority(self, element1, element2):
        return element1 < element2

    def _has_higher_prioirty(self, element1, element2):
        return element1 > element2

    def _left_child_index(self, index):
        # Will give the left index
        return 2 * index + 1

    def _parent_index(self, index):
        # Will give the right index
        return (index - 1) // 2

    def _heapify(self):
        pass

    def insert(self, element):
        self.elements.append(element)
        self.__bubble_up(len(self.elements)-1)

    def __bubble_up(self, index):
        element = self.elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self.elements[parent_index]
            if self._has_higher_prioirty(element, parent):
                self.elements[index] = parent
                index = parent_index
            else:
                break
        self.elements[index] = element

    def print_heap(self):
        heap = self.elements
        if not heap:
            print("Heap is empty.")
            return
        # Determine the height of the heap tree
        levels = math.floor(math.log2(len(heap))) + 1
        # Print the heap tree level by level
        max_width = 2 ** (levels - 1)
        level_index = 0  # start from level 0

        for i in range(levels):
            level_items = heap[level_index: level_index + 2**i]
            level_index += 2**i

            # Calculate the padding for formatting the tree
            space = " " * (max_width // (2**i))
            print(space.join([str(x) for x in level_items]))
            print("\n")  # add a line break between levels

        return ""

    def _has_higher_prioirty_child_index(self, index):
        first_index = self._left_child_index(index)
        if first_index >= len(self.elements):
            return None  # last element
        if first_index + 1 >= len(self.elements):
            return first_index  # One child element available
        if self._has_higher_prioirty(self.elements[first_index], self.elements[first_index+1]):
            return first_index
        else:
            return first_index+1

    def _push_down(self, index):
        element = self.elements[index]
        current_index = index
        while (True):
            child_index = self._has_higher_prioirty_child_index(current_index)
            if child_index is None:
                break
            if self._has_lower_priority(element, self.elements[child_index]):
                self.elements[current_index] = self.elements[child_index]
                current_index = child_index
            else:
                break
        self.elements[current_index] = element

    def top(self):
        """Return the top element and rearrage the heaps as per the three heap property
        """
        if not self.elements:
            raise ValueError("Getting top of empty Heap")
        elif len(self.elements) == 1:
            return self.elements.pop()
        else:
            element = self.elements[0]
            self.elements[0] = self.elements.pop()
            self._push_down(0)
        return element

    def heapify(self,elements):
        self.elements=deepcopy(elements)
        first_leaf=self.first_leaf_index()-1
        for parent_of_leaf in range(first_leaf,-1,-1):
            self._push_down(parent_of_leaf)
        
        
    
    def first_leaf_index(self):
        return len(self.elements)//2
