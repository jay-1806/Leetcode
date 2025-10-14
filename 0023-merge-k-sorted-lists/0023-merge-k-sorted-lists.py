import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        unique_id_counter = 0

        # 1. Initialization - Correctly sets up the heap with all *first* nodes
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, unique_id_counter, head))
                unique_id_counter += 1
    
        dummy = ListNode(0)
        tail = dummy

        # 2. Merging Loop - Correctly builds the list
        while min_heap:
            val , _ , node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next
            
            # 3. Replenishing the Heap - The critical fix
            if node.next:
                new_node = node.next
                
                # FIX: We must push the new_node, not the old 'head' variable
                heapq.heappush(min_heap , (new_node.val, unique_id_counter, new_node))
                
                unique_id_counter += 1

        return dummy.next