# 链表

## 排序链表

> 在 $O(nlogn)$ 时间复杂度和常数级空间复杂度下，对链表进行排序

解法：归并排序

- 递归式：时间复杂度 $O(nlogn)$，空间复杂度 $O(logn)$
  - 快慢指针找到中点
  - 归并排序

    ```python
    def sortList1(head):
        if not head or not head.next:
            return head
        # 快慢指针找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        # 归并
        l = sortList1(head)
        r = sortList1(mid)
        # 哑变量
        h = res = ListNode(0)
        while l and r:
            if l.val < r.val:
                h.next, l = l, l.next
            else:
                h.next, r = r, r.next
            h.next = h

        return res.next
    ```

- 循环式：时间复杂度 $O(nlogn)$，空间复杂度 $O(1)$

    ```python
        [4,3,1,7,8,9,2,11,5,6]
        step=1: (3->4)->(1->7)->(8->9)->(2->11)->(5->6)
        step=2: (1->3->4->7)->(2->8->9->11)->(5->6)
        step=4: (1->2->3->4->7->8->9->11)->5->6
        step=8: (1->2->3->4->5->6->7->8->9->11)
    ```

  - 先每 $2$ 个 $merge$，完成一趟后，再每 $4$ 个 $merge$，直到结束
　- 统计链表总长度
  - $merge(l1, l2)$，双路归并
  - $cut(l, n)$，将链表$l$切掉前$n$个节点，并返回后半部分的链表头
  - 哑变量使用

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        dummyhead.next = head
        p, length = head, 0
        while p:
            length += 1
            p = p.next

        size = 1
        while size < length:
            cur = dummyhead.next
            tail = dummyhead
            while cur:
                left = cur
                right = self.split(left, size)
                cur = self.split(right, size)
                tail.next = self.merge(left, right)
                while tail.next:
                    tail = tail.next
            size += size
        return dummyhead.next

    def merge(self, left, right):
        p = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return res.next

    def split(self, head, n):
        while head and n-1:
            head = head.next 
            n -= 1
        # 返回剩余节点
        if head is None: return None
        res = head.next
        head.next = None
        return res
```

## 合并

### 合并两个有序链表

- 设置好哑变量即可

```python
def mergeTwoLists(l1, l2):
    dummyhead = ListNode(0)
    p = dummyhead
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    p.next = l1 if l1 else l2
    return dummyhead.next
```

## 反转链表

见剑指offer-week03

## 两数相加

> 给出两个**非空**的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储**一位**数字

```python
输入：(7 -> 8 ) + (6 -> 4)
输出：3 -> 3 -> 1
原因：87 + 46 = 133
```

解法：进位和增加位数，考虑三点：

- 两数不一样长
- 有进位
- 最后有进位
- 拓展：正向，那就用栈压入再弹出

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy # 这一步必须的，为了能从dummy返回整个链表，所以以cur替代dummy迭代
        C = 0
        # 补0
        while l1 or l2:
            if l1 and l2:
                S = l1.val + l2.val + C
                l1, l2 = l1.next, l2.next
            elif l1 is None:
                S = l2.val + 0 + C
                l2 = l2.next
            else:
                S = l1.val + 0 + C
                l1 = l1.next
            # 求进位和当前和
            C = S // 10
            cur.next = ListNode(S % 10)
            # 移动到下一个结点
            cur = cur.next
        # 最后可能有进位
        if C == 1:
            cur.next = ListNode(1)
        return dummy.next
```

## 删除链表中的节点

> $O(1)$ 时间复杂度删除节点

思路：将下一个节点值覆盖当前要删除节点，然后将下一个节点的下一个节点连接到当前节点之后

```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```
