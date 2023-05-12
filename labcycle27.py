'''
27) Write a class called Product. The class should have fields called name, amount, and 
price, holding the product’s name, the number of items of that product in stock, and 
the regular price of the product. There should be a method get_price that receives the 
number of items to be bought and returns a the cost of buying that many items, where 
the regular price is charged for orders of less than 10 items, a 10% discount is applied 
for orders of between 10 and 99 items, and a 20% discount is applied for orders of 
100 or more items. There should also be a method called make_purchase that receives 
the number of items to be bought and decreases amount by that much.
'''

class product:
    def __init__(self,name,amount,price):
        self.name=name
        self.amount=amount
        self.price=price
    def get_price(self):
        print("FLAT 10% OFF ON PURSHACE OF 10 TO 99 ",self.name,"s")
        print("FLAT 10% OFF ON PURSHACE ABOVE 100 ",self.name,"s")
        print("enter no.of items you want to buy:")
        b=int(input())
        cost = self.price*b
        discount=0 
        a=0
        if(b<=self.amount):
            if(b<=10):
                print("--->Normal Price is charged for your order",self.price)
            elif(b<100 and b>10):
                discount=(cost*10)/100
                a=10
            elif(b>99):
                discount=(cost*20)/100
                a=20
            finalcost=cost-discount
            print(f"Product ordered        :{self.name}")
            print(f"price                  :{self.price}$")
            print(f"Actual                 :{cost}$")
            print(f"discount for your order:{discount}$")
            print(f"Total amount           :{finalcost}$")
        
        else:
            print("stock not available")
        
print("Enter name of product:")
na=input()
print(f"Enter cost of each {na}:")
co=int(input())
print("Enter stock available:")
st=int(input())
obj=product(na,st,co)
obj.get_price()
