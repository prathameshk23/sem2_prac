import heapq


class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0
        self.q = []

    def request(self):
        self.clock += 1
        req = (self.clock, self.pid)
        heapq.heappush(self.q, req)
        print(f"Process {self.pid} requests for CS at {self.clock}")
        return req

    def recive_req(self, request):
        heapq.heappush(self.q, request)
        self.clock = max(self.clock, request[0]) + 1

    def can_enter(self):
        return self.q[0][1] == self.pid

    def release(self):
        heapq.heappop(self.q)
        print(f"Process {self.pid} released from CS")


if __name__ == "__main__":
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)

    req1 = p1.request()
    p2.recive_req(req1)
    p3.recive_req(req1)

    req2 = p2.request()
    p1.recive_req(req2)
    p3.recive_req(req2)

    if p1.can_enter():
        print("P1 enters CS")
        p1.release()

    if p2.can_enter():
        print("P1 enters CS")
        p2.release()
