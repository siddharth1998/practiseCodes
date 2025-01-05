from node import Node


class BinarySearchTree:
    """Simple implementation of binary search tree"""

    def __init__(self, node=None):
        self._root = node

    def _search(self, value):
        """Simple searching on the basis of the binary search concept

        Args:
            value (int): Integer value to search

        Returns:
            tuple: Will return a tuple of node and parent node
        """
        parent = None
        node = self._root
        while node:
            node_val = node.val
            if node_val == value:
                return node, parent
            parent = node
            if value > node_val:
                node = node._right
            else:
                node = node._left
        return None, None

    def find_max_subtree(self,cnode=None):
        """Find the max element value in the whole tree

        Returns:
           tuple: right most node, parent
        """
        parent = None
        if cnode==None:
            node = self._root
        else:
            node=cnode
        while node._right:
            parent = node
            node = node._right

        return (node, parent)

    def insert(self, value):

        node = self._root
        if node is None:
            self._root = Node(value)
            return
        while node:
            if value <= node._value:
                if node.left(node) is None:
                    node = node.set_left(Node(value))
                    break
                else:
                    node = node.left(node)
            else:
                if node.right(node) is None:
                    node = node.set_right(Node(value))
                    break
                else:
                    node = node.right(node)

    def print_bst(self, node=None, space=0, level_gap=5):

        if node == None:
            return

        # Increase distance between levels
        space += level_gap

        # Process right child first (to display it on the right side)
        self.print_bst(node._right, space)

        # Print current node after spaces
        print()
        print(" " * (space - level_gap) + str(node._value))

        # Process left child
        self.print_bst(node._left, space)
    
    def delete_node(self,root,key):
        #Base Case
        if root is None:
            return root
        print(root._value,key)
        if root._value > key:
            # go left
            root._left=self.delete_node(root._left,key)
        elif root._value < key:
            # Go right
            root._right=self.delete_node(root._right,key)
        else:
            # Matched
            if root._left and root._right:
                max_value_node,_=self.find_max_subtree(cnode=root._left)
                root._value=max_value_node._value
                # swapped it not removed it
                root._left=self.delete_node(root._left,max_value_node._value)
            elif root.left:
                # Case parent of leaf node¸
                root=root._left
            else:
                # Case parent of leaf node¸
                root=root._right
        return root