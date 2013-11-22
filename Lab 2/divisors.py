def calcDivisors(n):
    for x in xrange(1, n + 1):
        if (n%x == 0):
            print x

    return
    
if __name__ == '__main__':
    while(True):
        
        n = int(raw_input('Enter your number : '))
        calcDivisors(n) 
