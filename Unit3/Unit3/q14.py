# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.

import copy

def is_luhn_valid(n):
    ###Your code here.
    strn = str(n)
    origDigs = [int(dig) for dig in strn]
    assert int(''.join([str(d) for d in origDigs])) == n

    modDigs = copy.copy(origDigs)
    for i in range(len(modDigs)-2, -1, -2):
        #print 'i: %d'%(i)
        modDigs[i] = (modDigs[i]*2)%10
    #print modDigs
    total = sum(modDigs)

    if total%10 == 0:
        return True
    else:
        return False


#print 0, is_luhn_valid(0)
#print 5, is_luhn_valid(5)
#print 50, is_luhn_valid(50)
#print 55, is_luhn_valid(55)
#print 999, is_luhn_valid(999)
#print 500, is_luhn_valid(500)
#print 505, is_luhn_valid(505)
#print 5000, is_luhn_valid(5000)
#print 5005, is_luhn_valid(5005)
#print 50000, is_luhn_valid(50000)

#raw_input()
