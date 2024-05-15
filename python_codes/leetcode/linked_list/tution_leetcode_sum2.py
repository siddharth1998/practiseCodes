# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> [ListNode]:
        num1=l1
        num2=l2
        head=None
        carry=0
        while(num1 and num2):
            # print(num1.val,num2.val)
            total=num1.val+num2.val+carry
            temp_val=total%10
            carry=(total-(total%10))//10
            if not head:
                head=ListNode(val=temp_val,next=None)
                result=head
            else:
                result.next=ListNode(val=temp_val,next=None)
                result=result.next
            # Going ahead
            num1=num1.next
            num2=num2.next
        # Now cases 
        # if num1  
        # if num2 
        # if carry is left 


        while(num1 or num2):
            if num1:
                total=num1.val+carry
                num1=num1.next
            else:
                total=num2.val+carry
                num2=num2.next
            temp_val=total%10
            carry=(total-(total%10))//10
            if not head:
                head=ListNode(val=temp_val,next=None)
                result=head
            else:
                result.next=ListNode(val=temp_val,next=None)
                result=result.next
            
        if carry:
            result.next=ListNode(val=carry,next=None)
            
        return head


x=Solution()
z=x.addTwoNumbers(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= None))),ListNode(val= 1, next= ListNode(val= 2, next= None))
               )

while(z):
    print(z.val)
    z=z.next

