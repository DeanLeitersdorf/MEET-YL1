


if __name__ == "__main__":

    dictionary = {}

    n = int(raw_input("Enter size of dictionary: "))
            
    for x in xrange(n):
        name = raw_input("Enter name " + str(x+1) + " : ")
        age = raw_input("Enter age " + str(x+1) + " : ")

        dictionary.update({name:age})
        print "Added name/age " + str(x+1)
        
    print dictionary
