# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This solution is for the Floyd's Tortoise and Hare (neetcode)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    


# Below is the solution I came up with
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         curr = head
#         seen = []

#         while curr:
#             if curr not in seen:
#                 seen.append(curr)
#                 curr = curr.next
#             elif curr in seen:
#                 return True
#         return False
        