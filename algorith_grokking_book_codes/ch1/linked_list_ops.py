from Node import Node

class linked_list_ops:
    
    def __init__(self):
        self.head=None
        
    def insert(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node   
        else:
            curr_node=self.head
            while(curr_node._next!=None):
                curr_node=curr_node._next
            curr_node._next=new_node
            new_node._next=None
        # Latest tail
    
    def __str__(self):
        if self.head==None:
            print("Head -> ", None)
            return""
        curr=self.head
        while(curr._next!=None):
            print(curr.data(),end="->")
            curr=curr._next
        print(curr.data())
        curr=curr._next
        return ""
    
    def insert_instarting(self,val):
         new_node=Node(val)
         next_node=self.head
         self.head=new_node
         new_node._next=next_node
         
    def delete_node(self,val):
        previous=self.head
        curr=previous._next# 1 step ahead  
        if previous.data()==val:
            # Starting
            if curr:
                self.head=curr
            else:
                self.head=None
            return 
        
        while(curr._next!=None):
            if curr.data()==val:
                previous._next=curr._next
            curr=curr._next
            previous=previous._next
        previous._next=None# previous becomes tail
            
        
         
if __name__=="__main__":
    x=linked_list_ops()
    # x.insert(1)
    # x.insert(2)
    # x.insert(3)
    # x.insert(4)
    # x.insert(5)
    # x.insert(6)
    # x.insert_instarting(10)
    # x.delete_node(1)
    # x.delete_node(6)
    # x.delete_node(4)
    # x.delete_node(5)
    # x.delete_node(2)
    # x.delete_node(10)
    # print("head node",x.head.data())
    x.insert(1)
    x.insert(2)
    x.insert(3)
    x.delete_node(1)
    x.delete_node(2)
    x.delete_node(3)

    print(x)
