# TASK:
#
# Achieve full statement coverage on the Queue class. 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

def testaq(q):
    q.checkRep()
    q.empty()
    q.full()
    for i in range(q.size+2):
        q.enqueue(i)
        q.checkRep()

    while not q.empty():
        q.dequeue()
        q.checkRep()
    
    q.dequeue()
    q.checkRep()

    return

# Add test code to test() that achieves 100% coverage of the 
# Queue class.
def test():
    ###Your code here.

    # didn't like this
    #qneg = Queue(-1)
    #testaq(qneg)
    #q0 = Queue(0)
    #testaq(q0)

    q1 = Queue(1)
    testaq(q1)
    q2 = Queue(2)
    testaq(q2)

    # here we will make sure we test self.tail < self.head in checkRep
    q2 = Queue(2)
    q2.enqueue(1)
    q2.dequeue()    # head should now be at 1
    q2.enqueue(2)    # tail should now be at 0
    q2.checkRep()

test()

