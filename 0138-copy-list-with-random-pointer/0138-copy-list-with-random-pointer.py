"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldtoNew = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtoNew[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtoNew[cur]
            copy.next = oldtoNew[cur.next]
            copy.random = oldtoNew[cur.random]
            cur = cur.next
        
        return oldtoNew[head]
        
        
