for x in lFizzBuzz:
    if (x % 3 == 0 and x % 5 == 0):
        print "fizzbuzz: " + str(x)
    elif x % 3 == 0:
        print "fizz: " + str(x)
    elif x % 5 == 0:
        print "buzz: " + str(x)
    else: print x

