import queue

class Queue:
    def __init__(self, string):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        for char in string:
            self.q1.put(char)

    def shuffle(self):
        result = ''
        while not self.q1.empty():
            result += self.q1.get() 
            if not self.q1.empty(): 
                self.q2.put(self.q1.get()) 
        while not self.q2.empty():
            result += self.q2.get() 
        return result


q = Queue('ABCDEFGH')
print(q.shuffle())  