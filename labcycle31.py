'''Write a Python class to reverse a string word by word '''

class string:
    def __init__(self,s):
        self.s=s
        sp=s.split(" ")
        rev=list(reversed(sp))
        j=" ".join(rev)
        print(j)
st=input("enter a string")
sd=string(st)
        





1
