# 148. Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def get_mid(head):
            slow = head
            fast = head
            if head is None:
                return head
            while (fast.next is not None) and (fast.next.next is not None):
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge_sort(head):
            if not (head and head.next):
                return head
            half, slow, fast = None, head, head
            while fast and fast.next:
                half, slow, fast = slow, slow.next, fast.next.next 
                # slow는 한 칸씩, fast는 두 칸씩 앞으로 이동 
                # -> fast가 맨 끝에 도달했을 때, slow는 중앙에 도달.
                # half는 slow의 바로 이전 값
            half.next = None # 연결 리스트 관계 끊기
            
            l1 = merge_sort(head) # head 시작 노드
            l2 = merge_sort(slow) # slow 탐색을 통해 발견한 중앙지점
            
            return merge(l1, l2) # 크기 비교하면서 정렬하여 합치기
        
                
        def merge(l1, l2):
            if l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                l1.next = merge(l1.next, l2)
            return l1 or l2

        return merge_sort(head)

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        
        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next 
        return head
                
            