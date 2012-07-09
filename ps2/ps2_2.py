# TASK:
#
# This is the SplayTree code we saw earlier in the 
# unit. We didn't achieve full statement coverage 
# during the unit, but we will now!
# Your task is to achieve full statement coverage 
# on the SplayTree class. 
# 
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

# Ima add a line here at work just for fun to see if I can then get it on my home PC.

# Okay I proved that I could add a line here and it would show up in a clone.
# But how about if I add these lines and push from work.  Will it show up with
# a pull on my home PC?

#covered = set()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            #covered.add(1)
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            #covered.add(2)
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            #covered.add(3)
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            #covered.add(4)
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            #covered.add(5)
            return

        # Now delete the root.
        if self.root.left== None:
            #covered.add(6)
            self.root = self.root.right
        else:
            #covered.add(7)
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            #covered.add(27)
            return None
        x = self.root
        while x.left != None:
            #covered.add(28)
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            #covered.add(8)
            return None
        x = self.root
        while (x.right != None):
            #covered.add(9)
            x = x.right
        #covered.add(10)
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            #covered.add(11)
            return None
        self.splay(key)
        if self.root.key != key:
            #covered.add(12)
            return None
        #covered.add(29)
        return self.root.key

    def isEmpty(self):
        #covered.add(13)
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                #covered.add(14)
                if t.left == None:
                    #covered.add(15)
                    break
                if key < t.left.key:
                    #covered.add(16)
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        #covered.add(17)
                        break
                #else:
                    #covered.add(18)
                #covered.add(19)
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                #covered.add(20)
                if t.right == None:
                    #covered.add(21)
                    break
                if key > t.right.key:
                    #covered.add(22)
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        #covered.add(23)
                        break
                ##else:
                #    #covered.add(24)
                l.right = t
                l = t
                t = t.right
            else:
                #covered.add(25)
                break
        #covered.add(26)
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


# Write test code in this function to achieve 
# full statement coverage on the SplayTree class.
def test():
    ###Your code here.
    st = SplayTree()
    st.insert(37)
    st.insert(36)
    st.insert(35)
    st.insert(37)
    st.insert(38)

    # insert on right first
    st = SplayTree()
    st.findMax()
    st.findMin()
    st.find(11)
    st.insert(37)
    st.find(11)
    st.find(37)
    st.insert(38)
    st.remove(37)
    st.insert(39)
    st.insert(37)
    st.insert(38)
    st.findMin()
    st.insert(1)
    st.find(1)
    st.insert(25)
    st.insert(20)
    st.insert(40)
    st.insert(39)
    st.remove(39)
    st.remove(17)
    st.findMin()
    st.findMax()
    st.isEmpty()

test()

#print sorted(list(covered))
#print len(covered)