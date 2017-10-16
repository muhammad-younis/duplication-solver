# Muhammad Younis and Dessie DiMino
# Tests the inputted string to find the seed
import math


# Asks user for string to input.
s = raw_input("Enter string: ")


# This section determines the seed that the original string came from
# in order to accurately find the shortest tandem duplication length.
length = len(s)
seedfound = 0

if s[0] == "0" and s[length - 1] == "0":
    for i in range(1,length - 1):
        if s[i] == "1":
            seed = "010"
            seedfound = 1
            break
    if seedfound == 0:
            seed = "0"
elif s[0] == "1" and s[length - 1] == "1":
    for i in range(1,length - 1):
        if s[i] == "0":
            seed = "101"
            seedfound = 1
            break
        if seedfound == 0:
            seed = "1"
elif s[0] == "0" and s[length - 1] == "1":
    seed = "01"
    
else:
    seed = "10"

print "Seed: %s" % seed


# Dictionary of solved keys that allows repeat calls on the 
# solver functiong to immediately have a result.
solvedkeys = {}


# 
def solver(n, seed, solvedkeys, currentsmallest):
    if n == seed:
        return 0
    elif n in solvedkeys.keys():
        return solvedkeys[n]
    else:
        smalleststringlength = currentsmallest
        for i in range(0, len(n) - 1):
            #truncating division
            maxrepeat = (len(n) - i) // 2
            #find all possible attempts and return solver
            while maxrepeat > 0:
                if n[i:(maxrepeat + i)] == n[(maxrepeat + i): (2*(maxrepeat) + i)]:
                
                #run solver to get the next branch length
                    branchstringlength = 1 + solver(n[0: i] + n[maxrepeat + i:], seed, solvedkeys, smalleststringlength)
                    solvedkeys[n[i:(maxrepeat + 1)]] = branchstringlength
                
                #make smallest the minvalue
                    smalleststringlength = min(smalleststringlength,branchstringlength)
                        
                maxrepeat -= 1

            solvedkeys[n] = smalleststringlength
        return (smalleststringlength)



steps = solver(s, seed, solvedkeys, float("inf") )
        
print "Steps: %d" % steps                           









        

    