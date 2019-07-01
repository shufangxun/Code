class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackpush = []
        self.stackpop = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackpush.append(x)

    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stackpop == []:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())
        
        return self.stackpop.pop()

        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stackpop == []:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())
        
        return self.stackpop[-1]


        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stackpop == [] and self.stackpush == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()