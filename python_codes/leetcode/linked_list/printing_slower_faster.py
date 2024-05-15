class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self):
        self.head=None 

    def slower_faster(self,head):
        self.head=head
        before_pointer,ahead_pointer=head,head.next
        print(" Before pointer --- ahead Pointer")
        while ahead_pointer and ahead_pointer.next:
            print(before_pointer.val , " --- ",ahead_pointer.val)
            before_pointer=before_pointer.next
            ahead_pointer=ahead_pointer.next.next
        print(before_pointer.val , " --- ",ahead_pointer.val)
        
        return self.head
    
    
    def __str__(self):
        print("the list is ")
        curr=self.head
        while(curr.next!=None):
            print(curr.val,end=" --- ")
            curr=curr.next
        print(curr.val)
        return ""

x=Solution()
x=Solution()
z=x.slower_faster(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 5, next= ListNode(val= 6, next= ListNode(val= 7, next= ListNode(val= 8, next=  ListNode(val= 9, next=  ListNode(val= 10, next= None))))))))))
               )
print(x)