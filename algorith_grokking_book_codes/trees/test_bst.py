from bst import BinarySearchTree

if __name__=="__main__":
    x=BinarySearchTree()
    x.insert(1)
    x.insert(0)
    x.insert(2)
    x.insert(5)
    x.insert(4)
    x.insert(-1)
    x.insert(-0.5)
    x.print_bst(x._root)
    x.delete_node(x._root,1)
    breakpoint()