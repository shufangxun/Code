class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.Trie
        for w in word:
            # 加入到字典
            if w not in cur:
                cur[w] = {}
            # 移动到下一个字符
            cur = cur[w]
        cur['#'] = 1
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.Trie
        for w in word:
            if w not in cur.keys():
                return False
            cur = cur[w]
        return True if '#' in cur else False
    
    def startWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.Trie
        for w in prefix:
            if w not in cur.keys():
                return False
            cur = cur[w]
        return True


