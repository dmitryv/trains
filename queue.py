class Queue:
    def __init__(self):
        self.queue = []
        return

    def put(self, term):
        self.queue.append(term)
        return

    def get(self):
        term = self.queue[0]
        self.queue = self.queue[1:]
        return term

    def is_empty(self):
        return 0 == len(self.queue)
