w=input("enter a word")
v="AEIOUaeiou"
flag=0
for i in v:
    for j in w:
        if(i==j):
            flag=flag+1
if(flag==0):
    print("no vowels")
else:
    print("vowels there")
        
