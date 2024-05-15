# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> [ListNode]:
        carry=0
        num1=l1
        num2=l2
        
        
        while(l1.next and l2.next):
            total=l1.val+l2.val+carry
            l1.val=total%10
            carry=(total-l1.val)//10
            l1=l1.next
            l2=l2.next
        
        total=l1.val+l2.val+carry
        l1.val=total%10
        carry=(total-l1.val)//10
        l1=l1.next
        l2=l2.next

        if l1 and l1.next :
            total=l1.val+l2.val+carry
            l1.val=total%10
            carry=(total-l1.val)//10
            l1=l1.next
            l2=l2.next
            while(carry and l1):
                if l2:
                    total=l1.val+carry+l2.val
                    l2=l2.next
                else:

                    total=l1.val+carry 
                l1.val=total%10
                carry=(total-l1.val)//10
                l1=l1.next
                if carry==0:
                    break
        if l2 and l2.next:
            aheadNode=l2
            total=l1.val+l2.val+carry
            l1.val=total%10
            carry=(total-l1.val)//10
            l1=l1.next
            l2=l2.next
            while(carry and l2):
                if l1:
                    total=l2.val+carry+l1.val
                    l1=l1.next
                else:
                    total=l2.val+carry
                l2.val=total%10
                carry=(total-l1.val)//10
                l2=l2.next
                if carry==0:
                    break
            l1.next=aheadNode

        return num1
    
x=Solution()
z=x.addTwoNumbers(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= None))),ListNode(val= 1, next= ListNode(val= 2, next= None))
               )
# z=x.addTwoNumbers(
#     ListNode(val= 0, next= None),ListNode(val= 0, next= None)
#                )
while(z):
    print(z.val)
    z=z.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         carry=0
#         num1=l1
#         num2=l2
        
        
#         while(l1.next and l2.next):
#             total=l1.val+l2.val+carry
#             l1.val=total%10
#             carry=(total-l1.val)//10
#             l1=l1.next
#             l2=l2.next
        
#         total=l1.val+l2.val+carry
#         l1.val=total%10
#         carry=(total-l1.val)//10
#         l1=l1.next
#         l2=l2.next

#         if l1 and l1.next :
            
#             while(carry and l1):
#                 if l2:
#                     total=l1.val+carry+l2.val
#                     l2=l2.next
#                 else:

#                     total=l1.val+carry 
#                 l1.val=total%10
#                 carry=(total-l1.val)//10
#                 l1=l1.next
#                 if carry==0:
#                     break
#         if l2 and l2.next:
#             aheadNode=l2
#             while(carry and l2):
#                 if l1:
#                     total=l2.val+carry+l1.val
#                     l1=l1.next
#                 else:
#                     total=l2.val+carry
#                 l2.val=total%10
#                 carry=(total-l1.val)//10
#                 l2=l2.next
#                 if carry==0:
#                     break
#             l1.next=aheadNode
#         if carry:
#             x=num1
#             while(x.next):
#                 x=x.next
#             x.next=ListNode(val=carry,next=None)


#         return num1