class Solution:
    def __init__(self):
        self.queue = []
        self.d = dict()  
    def firstAppearingOnce(self):
        """
        :rtype: str
        """
        for i in range(len(self.queue)):
            if self.d[self.queue[i]] == 1:
                return self.queue[i]

        return '#'
        
    def insert(self, char):
        """
        :type char: str
        :rtype: void
        """
        if char in self.d.keys():
            self.d[char] += 1
        else:
            self.d[char] = 1
            self.queue.append(char)

