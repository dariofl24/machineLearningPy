import numpy as np
import pandas as pd


### GRADED
### Code a function called "euclid_dist"

### ACCEPT two inputs, points, represented as tuples in the format, (a1, b1,...n1), (a2, b2, ...n2).
### RETURN the euclidean distance

### Remember: "**" is the python operator for exponents.

### YOUR ANSWER BELOW

def euclid_dist(p1, p2):

    dist = 0

    for x in range( len(p1) ):
        diff=p1[x] - p2[x]
        dist += (diff ** 2)

    return dist ** .5


p1 = (5,5)
p2 = (0,0)
p3 = (5,6,7,8,9,10)
p4 = (1,2,3,4,5,6)
print(euclid_dist(p1,p2)) #--> 7.0710678118654755
print(euclid_dist(p3,p4)) #--> 9.797958971132712
