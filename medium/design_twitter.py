# https://leetcode.com/problems/design-twitter/

from collections import defaultdict
import heapq
from typing import List


class Twitter:
    """
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

    Cases
    - User has posts, someone follows
    - User has no posts before followers
    - User has posts and followers, someone unfollows

    Solution
    - Keep track of every user's tweets. Form feed by looking at all tweets from all followed, capped at 10 sorted
    - Keep track of users feed
        - Add followee posts on follow
        - Remove followee post on unfollow
        - Update feed on tweet
    """

    def __init__(self):
        self.user_to_followers = defaultdict(set)
        self.user_to_feed = defaultdict(list)
        self.user_to_tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
        """
        self.user_to_followers[userId].add(userId)
        self.user_to_tweets[userId].append((self.count, tweetId))
        for followerId in self.user_to_followers[userId]:
            heapq.heappush(self.user_to_feed[followerId], (self.count, tweetId))
        self.count += 1
        print(self.user_to_tweets)
        print(self.user_to_followers)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself.
        Tweets must be ordered from most recent to least recent.
        """
        return [tweetId for _, tweetId in heapq.nlargest(10, self.user_to_feed[userId])]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId started following the user with ID followeeId.
        """
        if followerId not in self.user_to_followers[followeeId]:
            for postTime, tweetId in self.user_to_tweets[followeeId]:
                heapq.heappush(self.user_to_feed[followerId], (postTime, tweetId))
        self.user_to_followers[followeeId].add(followerId)
        print(self.user_to_followers[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId started unfollowing the user with ID followeeId.
        """
        if followeeId not in self.user_to_followers:
            return
        if followerId not in self.user_to_followers[followeeId]:
            return
        self.user_to_followers[followeeId].remove(followerId)
        tweets = set([tweetId for _, tweetId in self.user_to_tweets[followeeId]])
        self.user_to_feed[followerId] = [
            (postTime, tweetId)
            for postTime, tweetId in self.user_to_feed[followerId]
            if tweetId not in tweets
        ]
        heapq.heapify(self.user_to_feed[followerId])
        print(self.user_to_followers[followeeId])


a = [
    "Twitter",
    "postTweet",
    "getNewsFeed",
    "follow",
    "postTweet",
    "getNewsFeed",
    "unfollow",
    "getNewsFeed",
]
b = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]


twitter = Twitter()

for i, action in enumerate(a):
    print(action, b[i])
    if action == "postTweet":
        twitter.postTweet(b[i][0], b[i][1])
    elif action == "getNewsFeed":
        print(twitter.getNewsFeed(b[i][0]))
    elif action == "follow":
        twitter.follow(b[i][0], b[i][1])
    elif action == "unfollow":
        twitter.unfollow(b[i][0], b[i][1])
