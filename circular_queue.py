class CircularQueue:
    def __init__(self, max_length):
        self.queue = {}
        self.max_length = max_length
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.max_length:
            self.dequeue()

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_length
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return None

        removed_item = self.queue.pop(self.front)
        self.front = (self.front + 1) % self.max_length
        self.size -= 1
        return removed_item

    def display(self):
        if self.size == 0:
            print("Queue is empty")
            return

        index = self.front
        count = 0
        while count < self.size:
            print(self.queue[index], end=" ")
            index = (index + 1) % self.max_length
            count += 1
        print()


# Example
# cq = CircularQueue(5)
# cq.enqueue(1)
# cq.enqueue(2)
# cq.enqueue(3)
# cq.enqueue(4)
# cq.enqueue(5)
# cq.display()  # Output: 1 2 3 4 5
# cq.enqueue(6)
# cq.display()  # Output: 2 3 4 5 6
