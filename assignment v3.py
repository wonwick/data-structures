import datetime

class Cust:
    def __init__(self,bid):
        x=bid.split(",")
        self.av=True
        self.name=x[0]
        self.price=int(x[1])
        self.time=datetime.datetime.strptime(x[2], "%H:%M")

##buyers=input().split("#")
##sellers=input().split("#")

sellers="A,30000,01:35#B,13000,18:45#C,10000,12:54#D,10000,11:34#E,999,01:34".split("#")
buyers="X,13000,05:30#Y,25000,21:00#Z,30001,04:09#P,10000,09:09".split("#")
##print (buyers)
##print (sellers)

buyersList=[]
sellersList=[]


for i in buyers:
    buyersList.append(Cust(i))
    
    
for j in sellers:
    sellersList.append(Cust(j))

buyersList.sort(key=lambda x:x.time)
sellersList.sort(key=lambda x:x.time)

buyersList.sort(key=lambda x:x.price)
sellersList.sort(key=lambda x:x.price)

##print (list(map(lambda x:x.name+" "+str(x.price),buyersList)))

s=len(sellersList)
b=len(buyersList)
ans=[]

for k in range(s):
        seller=sellersList.pop(0)
##        print (seller.name,seller.price)
##        print (list(map(lambda x:x.name+" "+str(x.price),buyersList)))

        while len(buyersList)>0:
            buyer=buyersList[0]
##            print ("bp",buyer.price)
            if buyer.price<seller.price:
                del(buyersList[0])
                    
            else:                
##                print ("     ",buyer.name,buyer.price)
                dif=buyer.price-seller.price
##                print ("      dif:",dif)
                if dif<5:
##                    print ("      matched")
                    ans.append((seller.name,buyer.name))
                    del(buyersList[0])
                    break                    
                else:
                    break
            
print (ans)
        
        
