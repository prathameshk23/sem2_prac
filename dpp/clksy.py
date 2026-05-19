import time
import random


class TimeServer:
    def get_time(self):
        return time.time()


class Client:
    def __init__(self, offset):
        self.offset = offset

    def get_local_time(self):
        return time.time() + self.offset

    def sync(self, server):

        t1 = self.get_local_time()

        time.sleep(random.uniform(0.1, 0.5))

        server_time = server.get_time()

        time.sleep(random.uniform(0.1, 0.5))

        t2 = self.get_local_time()

        rtt = t2 - t1

        adjusted_time = server_time + (rtt / 2)

        self.offset = adjusted_time - time.time()
        print(f"new client time {self.get_local_time()}")


if __name__ == "__main__":
    server = TimeServer()
    client = Client(offset=-5)

    print(f"Server time {server.get_time()}")
    print(f"Initial time is {client.get_local_time()}")

    client.sync(server)
