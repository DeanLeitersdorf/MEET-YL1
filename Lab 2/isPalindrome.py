def isPalindrome(s):
    for x in xrange(0, len(s)/2):
       
        if s[x] != s[len(s)-x-1]:
            print "false"
            return False
    print "true"
    return True

if __name__ == "__main__":
    while(True):
        s = raw_input("Enter your string: ")
        isPalindrome(s)


