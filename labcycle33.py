""" Write a program to demonstrate Try/except/else """

a=int(input("enter a number"))
b=int(input("enter another number"))

try:
    c=a//b
except ZeroDivisionError:
    print("if zero is denominator,then it's value is infinity")
else:
    print("c value is ",c)
    
