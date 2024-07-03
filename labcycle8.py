#8) Write a program that asks the user to enter a word and prints out whether that word contains any vowels.
s=input("enter a string")
v='aeiouAEIOU'
f=0
if i in v:
    if i in s:
        f=1
        break
if f==1:
    print("the given word contains vowels")
else:
    print("the given word does not contain vowels")
