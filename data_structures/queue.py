class Queue():
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def length(self):
        return len(self.q)

    def dequeue(self):
        if len(self.q) < 1:
            return None
        self.q.pop(0)

    def display(self):
        print(self.q)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()
