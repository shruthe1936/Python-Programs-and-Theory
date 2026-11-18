import time

class RateLimiter:

    def __init__(self):
        self.limit = 5
        self.time_window = 60
        self.requests = {}

    def allow_request(self, user):

        current_time = time.time()

        if user not in self.requests:
            self.requests[user] = []

        self.requests[user] = [
            t for t in self.requests[user]
            if current_time - t < self.time_window
        ]

        if len(self.requests[user]) < self.limit:
            self.requests[user].append(current_time)
            return True

        return False


limiter = RateLimiter()

for i in range(6):

    if limiter.allow_request("Student1"):
        print("Request allowed")
    else:
        print("Request rejected")