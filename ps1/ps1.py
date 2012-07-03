'''
Date: 7/2/12
Author: Scott Halgrim, shalgrim@hotmail.com
Functionality:
    This code tries to break code we know is buggy but don't have access to.
It is problem set 1 for Udacity CS 258
URL for this problem set is:
http://www.udacity.com/view#Course/cs258/CourseRev/1/Unit/81001/Nugget/142001
'''
# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    q = Queue(1)
    assert q.empty()
    assert not q.full()
    assert q.enqueue(5000)
    assert q.full()
    assert not q.empty()
    value = q.dequeue()
    assert value == 5000
    assert q.empty()
    assert not q.full()
    assert q.enqueue(10)
    assert not q.enqueue(100)
    assert q.full()
    assert not q.empty()
    value = q.dequeue()
    assert value == 10
    value = q.dequeue()
    assert value is None
    assert q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value is None
    assert q.empty()
    assert not q.full()
    q = Queue(2)
    assert q.empty()
    assert not q.full()
    assert q.enqueue(20)
    assert not q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value == 20
    assert q.empty()
    assert not q.full()
    assert q.enqueue(30)
    assert not q.empty()
    assert not q.full()
    assert q.enqueue(40)
    assert not q.empty()
    assert q.full()
    assert not q.enqueue(50)
    assert not q.empty()
    assert q.full()
    value = q.dequeue()
    assert value == 30
    assert not q.full()
    assert not q.empty()
    assert q.enqueue(60)
    assert q.full()
    assert not q.empty()
    assert not q.enqueue(70)
    value = q.dequeue()
    assert not q.full()
    assert not q.empty()
    assert value == 40
    value = q.dequeue()
    assert value == 60
    assert q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value is None
    assert q.empty()
    assert not q.full()
    assert q.enqueue(0)
    assert not q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value == 0
    assert q.empty()
    assert not q.full()
    assert q.enqueue(-10)
    assert not q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value == -10
    assert q.empty()
    assert not q.full()


