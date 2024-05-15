class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        '''
        l1p = current node when iterating list1
        l2p = current node when iterating list2
        
        '''
      
        head=ListNode()
        tail=head
        print("head address ",id(head))
        print("tail address", id(tail))
        
        print("Initial Address of each linked list ")
        print("address of tail",id(tail),"address of list1",id(list1),"address of list2",id(list2))
        print("\n")

        while(list1 and list2):
            print("Before next operation")
            print("value of tail", tail.val,"value of list1 node",list1.val,"value of list2 ", list2.val)
            print("\n")

            if (list1.val > list2.val):
                tail.next=list2
                list2=list2.next
            else:
                tail.next=list1
                list1=list1.next

            tail=tail.next
            # For showing 
            print("After next operation")
            if(list1!=None and  list2!=None):
                print("value of tail", tail.val,"value of list1 node",list1.val,"value of list2 ", list2.val)

            print("address of tail",id(tail.next),"address of list1",id(list1),"address of list2",id(list2))
            print("\n")
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        print("Printing to check the next value of the first tail ",id(head.next))
        return head.next

x=Solution()
z=x.mergeTwoLists(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= None))),ListNode(val= 0, next= ListNode(val= 1, next= ListNode(val= 5, next= None)))
    )
print("Here")
while(z):
    print(z.val)
    z=z.next