# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self):
        pass 

    def reorderList(self, head: ListNode) -> None:
        self.head=head
        """
        Do not return anything, modify head in-place instead.
        """
        # When to stop ?
        # check the times you reorder meaning how many time you bring the last element to forward

        # observation Even : n//2 -1
        # observation odd : n//2 :: try to check out a way to parse the linkedlist and change the head by itself
        length=0
        temp=head

        while(temp):
            
            length+=1
            temp=temp.next


        if length%2==0:
            num_reorder=length//2-1
        else:
            num_reorder=length//2

        curr=head
        while(num_reorder>0):
            temp_next=curr.next # the node which is in present connected
            parsing_node_ahead=curr
            while(parsing_node_ahead.next!=None):
                
                parsing_node_before=parsing_node_ahead
                parsing_node_ahead=parsing_node_ahead.next
            parsing_node_before.next=None
            curr.next=parsing_node_ahead
            parsing_node_ahead.next=temp_next
            curr=temp_next
            num_reorder-=1
        self.head=head
        return self.head
    

    def __str__(self):
        curr=self.head
        while(curr.next!=None):
            print(curr.val)
            curr=curr.next
        return ""

x=Solution()
x=Solution()
z=x.reorderList(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 7, next= ListNode(val= 8, next= None))))))))
               )

curr=z
while(curr!=None):
    print(curr.val)
    curr=curr.next