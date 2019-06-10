# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=head
        q=p
        count=0
        if not head.val:return None
        while q:
            count+=1
            q=q.next
        if n>count:return None
        n=count-n+1
        if n==1:
            head=p.next
            return head
        for i in range(n-2):
            p=p.next
        des=p.next
        p.next=des.next
        return head
        # p1, p2 = head, head
        # while n:
        #     p2 = p2.next
        #     n -= 1
        # if not p2:
        #     return head.next
        # while p2.next:
        #     p2 = p2.next
        #     p1 = p1.next
        # tmp = p1.next.next
        # p1.next = tmp
        # return head
if __name__=='__main__':
    head=ListNode(1)
    p=head
    n=2
    i=2
    while i<6:
        p.next=ListNode(i)
        p=p.next
        i+=1
    p.next=None
    solution=Solution()
    p=solution.removeNthFromEnd(head,n)
    while p:
        print(p.val,end=' ')
        p=p.next






