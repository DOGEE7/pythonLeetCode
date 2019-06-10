# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p = l1  # ListNode类型
        q = l2
        curr = dummyHead
        carry = 0
        while (p or q):
            x = p.val if p else 0
            y = q.val if q else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
        if (carry > 0):
            curr.next = ListNode(carry)
        return dummyHead.next

if(__name__=="__main__"):
    l1=ListNode(2)
    l11=l1.next=ListNode(4)
    # l12=l11.next=ListNode(3)
    l2=ListNode(5)
    l21=l2.next=ListNode(6)
    l22=l21.next=ListNode(4)
    solution=Solution()
    re=solution.addTwoNumbers(l1,l2)
    while re:
        print(re.val,end=" ")
        re=re.next
