from decimal import*
n1=Decimal(input("enter a no"))
n2=Decimal(input("enter 2nd no"))
diff=n1-n2
if(diff<=0.001):
    print("close")
else:
    print("not close")
print(diff)
