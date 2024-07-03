'''
program 14
Write a program that generates 100 random integers that are either 0 or 1. Then find 
the longest run of zeros, the largest number of zeros in a row. For instance, the longest 
run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''
import random
x=[]
for i in range(10):
    x.append(random.int(0,1))
max=0
count=0
