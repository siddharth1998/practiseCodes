class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        
        current=head

        # print(type(current))
        # for i in current:
        #     print(type(i))
        prev=None
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
       
        head=prev
        
        return head
x=Solution()
z=x.reverseList(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 5, next= None)))))
               )