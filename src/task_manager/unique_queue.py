class EmptyQueueError(Exception):
    pass

class UniqueQueue:
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO,LIFO]
    def __init__(self, strategy: str = LIFO):
        self.strategy = strategy
        self.storage = []
        if self.strategy not in self.STRATEGIES:
            raise TypeError

    def add(self, item):
        if item in self.storage:
            return
        if self.strategy == self.FIFO:
            self.storage.append(item)
        if self.strategy == self.LIFO:
            self.storage.insert(0, item)

    def remove(self):
        if not self.storage:
            raise EmptyQueueError
        if self.strategy == self.LIFO:
            return self.storage.pop()
        if self.strategy == self.FIFO:
            return self.storage.pop(0)


    def len_uniq_queue(self):
        return len(self.storage)

    def last_item(self):
        if self.strategy == self.FIFO:
            return self.storage[-1]
        else:
            return self.storage[0]