#SumPrimeDivisor

#SumPrimeDiv(value)
# outputs
# SumPrimeDiv(1) => 0
# SumPrimeDiv(7) => 7
# SumPrimeDiv(6) => 2 + 3 = 5

def SumPrimeDiv(x):
        if type(x) is str:      # scanning for string instances
                print "Please choose an integer value."
                return None
        x = int(x)	# forcing values to integer to avoid float issues
        if x < 1:
                print "Please choose a postive integer."
                return None
        if x == 1:	# forcing the edge case of value 1 as a non-prime
                sumlist = [0]
                print "The sum of primes for ", x, " is: ", sum(sumlist)
        else:
                sumlist = [] 	# empty list for divisor values
                for i in range(2, x+1):
                    if x % i == 0:  #identifying the divisor
                        for j in range (2, i+1):  #identifying a prime divisor
                            if i % j == 0:
                                if j != x:
                                        sumlist.append(j)
                                        
                                if len(sumlist) == 0:
                                        sumlist.append(x)
                                        
                                sumlist = set(sumlist)	# force to set for unique divisors
                                sumlist =list(sumlist) 	# force back to list for summation

        print 'The sum of prime divisors for', x, 'is:', sum(sumlist), sumlist
        return
