'''Write a Python class to implement pow(x, n). '''

from math import*

class pow:
    def __init__(self,x,y):
        z=x**y
        print(f"the value of {x}**{y} is {z}")

a=int(input("enter a number"))
b=int(input("enter another number"))
c=pow(a,b)

