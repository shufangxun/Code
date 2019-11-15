# 滑动窗口

## 滑动窗口的最大值(元素) [参考](https://blog.csdn.net/u010429424/article/details/73692248)  

>1．给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。  
>2．返回滑动窗口中的最大值(元素)

```python
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
```

借助一个双端队列，从头遍历数组，根据如下规则进行入队列或出队列操作：

1. 如果队列为空，则当前数字入队列
2. 如果当前数字大于队列尾，则删除队列尾，直到当前数字小于等于队列尾，或者队列空，然后当前数字入队列
3. 如果当前数字小于队列尾，则当前数字入队列
4. 如果队列头超出滑动窗口范围，则删除队列头
5. 这样能始终保证队列头为当前的最大值
6. 队列中存储数组的下标而非数值，这样通过判断下标之间的差值是否大于窗口的大小

```python
def maxSlidingWindow(self, nums, k):
    if len(nums) < k:
        return []
    window, res = [], []
    for i, num in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and num >= nums[window[-1]]:
            window.pop(-1)
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res
```
