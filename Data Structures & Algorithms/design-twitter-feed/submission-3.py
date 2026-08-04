class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for tweet in self.tweets[userId]:
            feed.append(tweet)
        for fol in self.followers[userId]:
            feed.extend(self.tweets[fol])
        heapq.heapify(feed)
        feed.sort(key = lambda x : -x[0])
        return [y for x,y in feed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
