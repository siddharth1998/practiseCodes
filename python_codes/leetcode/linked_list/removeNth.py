# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        slower,faster=head,head.next
        distance_in_mid=1
        prev=None
        isOdd=False
        while ( faster ):
            next=slower.next
            slower.next=prev
            prev=slower
            slower=next
            # until this point have reversed the list 
            if faster.next==None:
                isOdd=True
                break
            faster=faster.next.next
            distance_in_mid+=1
        if isOdd:
            # Even number
            length=distance_in_mid*2
        else:
            # Odd number
            length=distance_in_mid*2-1

        # distance_in_mid is the postion of the slower pointer
        deviation_from_middle=distance_in_mid-n

        if deviation_from_middle > 0 :
            # move in forward direction 
            curr=slower.next
            while(deviation_from_middle):
                curr=curr.next
                deviation_from_middle-=1
            pass
        else:
            # move in reverse direction 
            pass

x=Solution()
z=x.removeNthFromEnd(
    ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= ListNode(val= 5, next=None)))))
               ,4)