import random
import array


def tossCoin():
    global tossAmount
    global randProbabilityForHeads
    
    while(tossAmount<=-10): #tossAmount is -10 if user didn't specify how many times to toss.
        userInput = raw_input("Press n + ENTER to continue. ")
        if(userInput=="n"):
            randInt = random.random()
            if(randInt<randProbabilityForHeads):
                print "H"
            else:
                print "T"
    if(tossAmount>0):
            
            array = []
            for x in xrange(tossAmount):
                randInt = random.random()
                if(randInt<randProbabilityForHeads):
                    print "H"
                    array.append("H")
                else:
                    print "T"
                    array.append("T")
            print array
            return array
    
        

if __name__ == '__main__':
    global randProbabilityForHeads
    global tossAmount
    

    print "Possible codes: "
    print "Equal_Probability - Flips coin at equal probability, and prints result"
    print "Certain_Heads_Probability - Asks user for probability for heads, and then tosses coin"
    print "Toss_N_Times - Asks user how many times to toss, and tosses at 0.5 prob"
    print ""

    typeOfCode = raw_input("Enter what type of code you want to run: ")
    if(typeOfCode=="Equal_Probability"):
        randProbabilityForHeads = 0.5
        tossCoin()
    if(typeOfCode=="Certain_Heads_Probability"):
        randProbabilityForHeads = int(raw_input("Insert probability for heads: "))
        tossCoin()
    if(typeOfCode=="Toss_N_Times"):
        randProbabilityForHeads = 0.5
        tossAmount = int(raw_input("Enter number of times to toss: "))
        tossCoin()
