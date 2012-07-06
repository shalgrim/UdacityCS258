'''
Date: 7/2/12
Author: Scott Halgrim, shalgrim@hotmail.com
Functionality: This code tries to break code we know is buggy but don't have access to.  It is problem set 1 for Udacity CS 258
URL for this problem set is http://www.udacity.com/view#Course/cs258/CourseRev/1/Unit/81001/Nugget/142001
'''
# Making a change EOD 7/3/12 to test push after I've been unable to clone

# 7/5 Now I'm at home.  I can see that 7/3/12 push did work.
# And now I've cloned succesfully at home, but with cmd line
# and with git extensions via VS.
# Making a change to see if this push works.

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
    assert q.enqueue(-20)
    assert not q.empty()
    assert q.full()
    assert not q.enqueue(-30)
    assert not q.empty()
    assert q.full()
    value = q.dequeue()
    assert value == -10
    assert not q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value == -20
    assert q.empty()
    assert not q.full()
    value = q.dequeue()
    assert value is None
    assert q.empty()
    assert not q.full()
    q = Queue(0)
    assert q.full()
    assert q.empty()
    assert not q.enqueue(15)
    assert q.full()
    assert q.empty()
    value = q.dequeue()
    assert value is None
    assert q.full()
    assert q.empty()

    q2 = Queue(3)
    assert q2.empty()
    assert not q2.full()
    assert q2.enqueue(1)
    assert not q2.empty()
    assert not q2.full()
    assert q2.enqueue(2)
    assert not q2.empty()
    assert not q2.full()
    assert q2.enqueue(3)
    assert not q2.empty()
    assert q2.full()
    assert not q2.enqueue(4)
    assert not q2.empty()
    assert q2.full()
    value = q2.dequeue()
    assert value == 1
    assert not q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value == 2
    assert not q2.empty()
    assert not q2.full()
    assert q2.enqueue(5)
    assert not q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value == 3
    assert not q2.empty()
    assert not q2.full()
    assert q2.enqueue(6)
    assert not q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value == 5
    assert not q2.empty()
    assert not q2.full()
    assert q2.enqueue(7)
    assert not q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value == 6
    assert not q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value == 7
    assert q2.empty()
    assert not q2.full()
    value = q2.dequeue()
    assert value is None
    assert q2.empty()
    assert not q2.full()

    # I got this aprt after viewing the solution.  Weird.
    q16 = Queue(16)

    for i in range(16):
        assert q16.enqueue(i)

    for i in range(16):
        value = q16.dequeue()
        assert value == i







    #q = Queue(-1)
    #assert not q.full() # I feel like this should be assert q.full(), but then I get the error about the correct code erroring out
    #assert q.empty()
    ##assert not q.enqueue(15) # this causes an error, but not an assertion error
    ##assert not q.full()
    ##assert q.empty()
    #value = q.dequeue()
    #assert value is None
    #assert not q.full()
    #assert q.empty()


