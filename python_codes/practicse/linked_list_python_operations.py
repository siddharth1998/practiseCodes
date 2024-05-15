# Declare a linked list
# insert in the linked list
# delete from a linked list
# insert in last of the list
# Insert at the end of the list

class Node(object):  # creating a node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self, value):  # Add an element in the ending of the list

        new_node = Node(value)
        try:
            if self.head == None:
                self.head = new_node
            else:
                current = self.head
                while (current.next != None):
                    current = current.next
                current.next = new_node
            return True
        except Exception as e:
            return False

    def __str__(self):
        print("The linked list is ::")

        current = self.head
        while (current):
            if current.next == None:
                print(current.data)
            else:
                print(current.data, end=" == > ")
            current = current.next
        return ""

    def add_node_start(self, value):
        new_node = Node(value)

        current = self.head
        self.head = new_node
        new_node.next = current
        return True

    def add_node_between(self, value, postion):
        '''
        value => is the value which is need to be added into the list 
        postion => is the postion at which you want to add the node 

        '''
        if postion < 0:
            raise Exception("Value greater than -1")
        new_node = Node(value)
        current = self.head
        count = 0

        while (count < postion-1):  # Index start from 0
          
            if current.next == None:
                current.next = new_node
                return True
            count += 1
            current = current.next
        next_node = current.next
        current.next = new_node
        new_node.next = next_node
        return True

    def delete_node_from_starting(self):
        curr=self.head
        curr=curr.next
        self.head=curr
        
    def delte_node_from_end(self):
        curr=self.head
        if curr.next==None:
            curr.data=None
            self.head=None
            return True
        nextNode=self.head.next
        
        while(nextNode.next!=None):
            curr=curr.next
            nextNode=nextNode.next
        # print(curr.data,"nextNode data",nextNode)
        curr.next=None
        return True
    
    def delete_from_postion(self,pos):
        curr=self.head
        count=0
        while(count<pos):
            curr=curr.next
            count+=1
        
        tempNext=curr.next
        
normal_linked_list = LinkedList()
normal_linked_list.add_node(1)
normal_linked_list.add_node(2)
normal_linked_list.add_node_start(4)
normal_linked_list.add_node_between(10, 4)
normal_linked_list.add_node_between(11, 1)
normal_linked_list.add_node(3)
normal_linked_list.add_node_between(11, 11)

print(normal_linked_list)

print(normal_linked_list, "before")

normal_linked_list.delete_node_from_starting()
print(normal_linked_list,"after deletion from starting")
normal_linked_list.delte_node_from_end()
print(normal_linked_list,"for the delete of the link")