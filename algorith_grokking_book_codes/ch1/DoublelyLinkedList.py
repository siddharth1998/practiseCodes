from DNode import DoublyLinkedList as dl


class DoublyLinkedListOps:
    def __init__(self):
        self._head = None
        self._tail = None

    def insertInFront(self, val):
        if self._head is None:
            self._tail = self._head = dl.Node(val)
        else:
            old_head = self._head
            self._head = dl.Node(val)
            old_head._prev = self._head
            self._head._next = old_head

    def insertInEnd(self, val):
        if self._tail is None:
            # Empty List
            self.insertInFront(val)
        else:
            old_tail = self._tail
            new_node = dl.Node(val)
            old_tail._next = new_node
            new_node._prev = old_tail
            # tail will become the new node
            self._tail=new_node
            
    def deleteNode(self, target):
        if self._head is None:
            return "Empty List"
        if self._head._data==target:
            if self._head._next is None:
                self._head=self._prev=None
                return "Empty List"
                
            print("Found Node in starting")
            # delete in starting
            self._head=self._head._next
            self._head._prev=None
            return "Find the element in the starting"
        elif self._tail._data==target:
            print("Found the Node in the Ending")
            # Delete in the end
            self._tail=self._tail._prev
            self._tail._next=None
        else:
            # Try to search somewhere in between 
            curr=self._head._next
            print(type(curr))
            counter=1
            while(curr._next):
                print(type(curr))
                if curr._data==target:
                    prev_node=curr._prev
                    next_node=curr._next
                    
                    # Detaching
                    curr._next=None
                    curr._prev=None
                    
                    # Connecting 
                    prev_node._next=next_node
                    next_node._prev=prev_node
                    return f"Done found element in {counter} postion"
                curr=curr._next
                counter+=1
            pass

    def __str__(self):
        if self._head is None:
            print("Empty List")
        curr = self._head
        while (curr):
            print(curr._data)
            curr = curr._next
        return ""

if __name__=="__main__":    
    x = DoublyLinkedListOps()
    x.insertInFront(1)
    x.insertInFront(2)
    x.insertInFront(3)
    x.insertInFront(4)
    x.insertInEnd(10)
    x.insertInEnd(12)
    x.insertInFront(-1)
    print(x)
    print("Delete node in starting")
    x.deleteNode(-1)
    print(x)
    print("Delete the Node in the ending")
    x.deleteNode(12)
    print(x)
    print("Delte node in between")
    x.deleteNode(1)
    print(x)
    
    print("Deleting all the nodes")
    x.deleteNode(3)
    x.deleteNode(2)
    x.deleteNode(1)
    x.deleteNode(10)
    x.deleteNode(4)
    print(x)
