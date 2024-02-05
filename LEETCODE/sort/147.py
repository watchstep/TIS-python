# 147. Insertion Sort List

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object): # 1151ms
    def insertionSortList(self, head) :
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # curr 정렬되어 있는 대상
        # head 정렬해야 하는 대상
        curr = parent = ListNode(None)
        
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            # 삽입 위치 찾았다면
            curr.next, head.next, head = head, curr.next, head.next
            # 찾은 curr 위치에 head
            # head.next에 cur.next 연결해 이어지도록.
            # 다음 head는 head.next 이어받기
            curr = parent
        return curr.next
    
class Solution(object): # 96ms
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        curr = parent = ListNode(0) # 초깃값 None -> 0
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            curr.next, head.next, head = head, curr.next, head.next
            
            # 필요할 때만 curr 포인터가 되돌아가도록 처리 (삽입 위치를 계속 찾을 필요  X)
            if head and curr.val > head.val:
                curr = parent
        return parent.next
    
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head