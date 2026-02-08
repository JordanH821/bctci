class ViewerCounter:
    SUB: str = "subscriber"
    FOL: str = "follower"
    GUE: str = "guest"
    V_TYPES: list[str] = [SUB, FOL, GUE]

    def __init__(self, window: int):
        self._window: int = window
        self._queues: dict[str, list[tuple[int, int]]] = {
            t: [] for t in ViewerCounter.V_TYPES
        }

    def join(self, t: int, v: str) -> None:
        if self._queues[v] and self._queues[v][-1][0] == t:
            # t is the latest on the queue, so update
            #NOTE: use lists for piggybacking information to avoid this inefficient pop and append to update an immmutable tuple
            _, count = self._queues[v].pop()
            self._queues[v].append((t, count + 1))
        else:
            # t is newer than the latest on the queue
            self._queues[v].append((t, 1))

    def get_viewers(self, t: int, v: str) -> int:
        stop_t: int = t - self._window
        viewers: int = 0
        # we can drop anything before stop_t since t >= all previous t and window is constant
        for time, count in self._queues[v]:
            if time >= stop_t and time <= t:
                viewers += count
        return viewers


def run_tests():
    # Test unoptimized version
    counter = ViewerCounter(10)
    counter.join(1, "subscriber")
    counter.join(1, "guest")
    counter.join(2, "follower")
    counter.join(2, "follower")
    counter.join(2, "follower")
    counter.join(3, "follower")
    assert counter.get_viewers(10, "subscriber") == 1
    assert counter.get_viewers(10, "guest") == 1
    assert counter.get_viewers(10, "follower") == 4
    assert counter.get_viewers(13, "follower") == 1
    print("PASS")

    # # Test optimized version
    # counter = ViewerCounterOptimized(10)
    # counter.join(1, "subscriber")
    # counter.join(1, "guest")
    # counter.join(2, "follower")
    # counter.join(2, "follower")
    # counter.join(2, "follower")
    # counter.join(3, "follower")
    # assert counter.get_viewers(10, "subscriber") == 1
    # assert counter.get_viewers(10, "guest") == 1
    # assert counter.get_viewers(10, "follower") == 4
    # assert counter.get_viewers(13, "follower") == 1


run_tests()
