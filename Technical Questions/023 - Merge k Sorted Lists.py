# There's also the minor point that .pop will be slightly slower than the del since it'll translate to a function call rather than a primitive. – Noufal Ibrahim Apr 19 '11 at 8:06
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/articles/merge-k-sorted-list/

class Solution(object):
    def heapify(self, array):
        for index in range(len(array) // 2, -1, -1):
            self.min_heapify(array, index)
        return array
    
    # Min heapify on the value of the linked list
    def min_heapify(self, array, index):
        left, right = 2 * index + 1, 2 * index + 2
        smallest = index
        
        # Find smallest out of the three
        if left < len(array) and array[left].val < array[index].val: 
            # Need to swap right away, what if its not the same
            smallest = left
            array[left], array[index] = array[index], array[left]
        if right < len(array) and array[right].val < array[index].val:
            smallest = right
            array[right], array[index] = array[index], array[right]
            
        # Recurse on the rest
        if smallest != index:
            self.min_heapify(array, smallest)
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Need a dummy head to track the rest
        head = ListNode(None)
        pointer_to_head = head
        
        # Initially Clean up any Nones
        heapified_list = self.heapify([node for node in lists if node])
        
        # The 0th element is the minimum, so make head.next that node, and then that value becomes array[0] = array[0].next
        # if the 0th element becomes None, delete it from the list
        while heapified_list != []:
            # advance first element's node to next
            head.next, heapified_list[0] = heapified_list[0], heapified_list[0].next
            head = head.next # advance to the next node
            if not heapified_list[0]: # Check if this is none
                del heapified_list[0]
            heapified_list = self.heapify(heapified_list)
            
        # Returns none if theres nothing in the list
        return pointer_to_head.next


"""
# WITH PRIORITY QUEUE to read...
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next
"""
