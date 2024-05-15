# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self):
        pass 

    def reorderList(self, head: ListNode) -> None:
        curr=head
         # Code to divide the list into 2 halves
        before_pointer,ahead_pointer=curr,curr.next
        while ahead_pointer and ahead_pointer.next:
            before_pointer=before_pointer.next
            ahead_pointer=ahead_pointer.next.next
        print("value of before and ahead pointer ",before_pointer.val,ahead_pointer.val)
        # starting of the next list 
        head_next_list=before_pointer.next # To create a second head for the second list
        before_pointer.next=None # To divide the first half from second
        # Reverse a list

        print("value of head_next_list",head_next_list.val)
        curr=head_next_list
        # temp_curr_next=curr.next
        # curr.next=None
        # curr=temp_curr_next
        # print("printing curr value after first changes",)
        prev=None
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        second_head=prev

        # Now merging code 
        curr=head
        other_curr=second_head

        while(curr):
            # print(curr.val,"  ",other_curr.val)
            # Store the current next into a variable 
            curr_next=curr.next
            #assign teh curr next to the value from second list
            curr.next=other_curr
            other_curr=other_curr.next
            # Move to the next node 
            curr=curr.next
            # Assign the next value of this node to original node
            curr.next=curr_next
            # now move formward 
            curr=curr_next
            # Move Second_head forward
            
        
      
            
        
    

            
       

    

   

x=Solution()
x=Solution()
z=x.reorderList(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 7, next= ListNode(val= 8, next= None))))))))
               )

curr=z
while(curr!=None):
    print(curr.val)
    curr=curr.next