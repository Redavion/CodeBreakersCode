class RecentCounter:

    def __init__(self):
        self.myQueue = collections.deque()

    def ping(self, t: int) -> int:
        self.myQueue.append(t)
        while self.myQueue[0] < t-3000:
            self.myQueue.popleft()
        return len(self.myQueue)
