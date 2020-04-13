'''
1. postTweet(userId, tweetId): 创建一条新的推文
2. getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
3. follow(followerId, followeeId): 关注一个用户
4. unfollow(followerId, followeeId): 取消关注一个用户
'''

import heapq

class Tweet:
    # 链表存储推文，包括发推ID、时间
    def __init__(self, tid: int, time: int) -> None:
        self.tid = tid
        self.time = time
        self.next = None

class User:
    # hash存储关注，包括Id，关注列表ID，当前用户发推列表
    def __init__(self, uid: int):
        self.uid = uid
        self.following = set()
        self.tweetlst = None
        # 自己要follow自己
        self.follow(uid)

    def post(self, tid: int, time: int) -> None:
        tweet = Tweet(tid, time)
        # 将新建的推文插入链表头
        # 越靠前的推文 time 值越大
        tweet.next = self.tweetlst
        self.tweetlst = tweet

    def follow(self, uid: int) -> None:
        if uid not in self.following:
            self.following.add(uid)

    def unfollow(self, uid: int) -> None:
        # one cannot unfollow itself
        if uid != self.uid and uid in self.following:
            self.following.remove(uid)

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id2user = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.id2user: 
            # 包含hashset、linklist
            self.id2user[userId] = User(userId)
        user = self.id2user[userId]
        user.post(tweetId, self.timestamp)
        # 全局变量
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap, user = [], self.id2user.get(userId)

        if user:
            # 用堆的做法，把所有推搞出来
            # 另一种做法是合并多个链表
            for uid in user.following:
                tweets = self.id2user[uid].tweetlst
                while tweets:
                    heap.append(tweets)
                    tweets = tweets.next
            return [twt.tid for twt in heapq.nlargest(10, heap, key= lambda twt: twt.time)]
        else: return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.id2user:
            self.id2user[followerId] = User(followerId)
        if followeeId not in self.id2user:
            self.id2user[followeeId] = User(followeeId)
        self.id2user[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.id2user:
            self.id2user[followerId].unfollow(followeeId)