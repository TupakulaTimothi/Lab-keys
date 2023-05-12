''' Write a program to demonstrate try/finally and with/as    '''

a=int(input("enter a number:"))
b=int(input("enter another number"))
try:
    c=a//b
    
except ZeroDivisionError:
    print("Denominator should not be zero")
else:
    print("c value is ",c)
finally:
    print("this is finally block")
