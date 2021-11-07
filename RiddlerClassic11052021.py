"""Riddler Classic

From Emma Knight comes a unit conversion conundrum:

The sum of the factors of 36 — including 36 itself — is 91. Coincidentally, 36 inches rounded to the nearest centimeter is … 91 centimeters!

Can you find another whole number like 36, where you can “compute” the sum of its factors by converting from inches to centimeters?

Extra credit: Can you find a third whole number with this property? How many more whole numbers can you find?"""


# subproblem 1 : Given a number N find all the factors. 
# Algorithm : loop from 2 to N/2 and check if the mod is 0. Add to a list. 

import numpy as np
def findAllFactors(N):
    factors = [1]
    for i in range(2, 1+np.ceil(N/2).astype(int)):
        if N%i==0:
            factors.append(i)
    factors.append(N)
    return factors

def toClosestCenti(N):
    return np.floor(N*2.54).astype(int)

# print(f'The factors of 36 are : {findAllFactors(36)} and they add up to {np.sum(findAllFactors(36))}')
# print(f'The closest value of 36 inches in cm is {toClosestCenti(36)}')

i=37
solutionNotFound=True
secondSolutionNotFound = True
while(solutionNotFound or secondSolutionNotFound):
    # print(i)
    if np.sum(findAllFactors(i)) == toClosestCenti(i):
        print(f'The factors of {i} are : {findAllFactors(i)} and they add up to {np.sum(findAllFactors(i))}')
        print(f'The closest value of {i} inches in cm is {toClosestCenti(i)}')
        if solutionNotFound:
            solutionNotFound=False
            i+=1
        else:
            secondSolutionNotFound=False
    else:
        i+=1
    