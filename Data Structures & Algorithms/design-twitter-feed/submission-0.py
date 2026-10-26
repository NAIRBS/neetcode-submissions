class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId) # 1. Ensure user follows themselves
        minHeap = [ # Initialize minheap with latest tweet from each followee (and user)
            [count, tweetId, fid, len(self.tweetMap[fid]) - 2]
            for fid in self.followMap[userId]
            if fid in self.tweetMap and self.tweetMap[fid]
            for count, tweetId in [self.tweetMap[fid][-1]]
        ]
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            _, tweetId, fid, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            if index >= 0:
                next_count, next_tid = self.tweetMap[fid][index]
                heapq.heappush(minHeap, [next_count, next_tid, fid, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
