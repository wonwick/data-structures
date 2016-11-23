import datetime

class Node:
    def __init__(self,Data):
        self.data=Data
        self.left=None
        self.right=None
        


class BST( object ):
 
    def __init__( self ):
        self.root = None


    def getRoot( self ):
        return self.root
    

    def add( self, el ):
        n, p = self.root, None

        while n is not None :
          p = n
          if el.price <= n.data.price:
            n = n.left
          else:
            n = n.right


        if p is None:
            self.root = Node( el )
        elif el.price <= p.data.price:
            p.left = Node( el )
        else:
            p.right = Node( el )
            

    def find(self,price):
        n, p = self.root, None
        print ("price: ",price)

        while n is not None:
            if (n.data.price<=price and n.data.av==True and abs(n.data.price-price)<5):
                break
            print ("price: ",price,"    nodes prize:",n.data.price,"nodes name:",n.data.name)
            print(n.data.price<=price,n.data.av==True)
            if price < n.data.price:
                print("chose left")
                n = n.left
            elif price > n.data.price:
                print("chose right")
                n = n.right
                
        if n is None:
          print ("n is None no match found")      
          return

        if n is not None and abs(n.data.price-price)<5:
            print ("matched")
            n.data.av=False
            return n.data.name
        else:
            
            print ("chose else because difference is bigger than what is needed")
            return
        

    def preOrder(self,root):
        l=[]    
        s=""
        def sup(root):        
            if root!=None:
                l.append(root.data.price)
                sup(root.left)
                sup(root.right)
        sup(root)
        for i in l:
            s+=str(i)+" "
        print (s)
        

    def inOrder(self,root):
        l=[]    
        s=""
        def sup(root):       
            if root!=None:
                sup(root.left)
                l.append(root.data.price)
                sup(root.right)

        sup(root)
        for i in l:
            s+=str(i)+" "
        print (s)
        

    def postOrder(self,root):
        l=[]    
        s=""
        def sup(root):       
            if root!=None:
                
                sup(root.left)
                sup(root.right)
                l.append(root.data.price)

        sup(root)
        for i in l:
            s+=str(i)+" "
        print (s)



class Cust:
    def __init__(self,bid):
        x=bid.split(",")
        self.av=True
        self.name=x[0]
        self.price=int(x[1])
        self.time=datetime.datetime.strptime(x[2], "%H:%M")



def match(seller,buyersTree):
  ans=buyersTree.find(seller.price)
  if ans==None:
    return
  else:
    return (ans,seller.name)                
        

buyersTree=BST()



##buyers=input().split("#")
##sellers=input().split("#")

buyers="A,30000,01:35#B,13000,18:45#C,10000,12:54#D,10000,11:34#E,999,01:34".split("#")
sellers="X,13000,05:30#Y,25000,21:00#Z,30001,04:09#P,10000,09:09".split("#")
##print (buyers)
##print (sellers)








buyersl=[]
sellersl=[]

for i in buyers:
    buyersl.append(Cust(i))
    
    
for j in sellers:
    sellersl.append(Cust(j))

buyersl.sort(key=lambda x:x.time)
sellersl.sort(key=lambda x:x.time)
buyersl.sort(key=lambda x:x.price,reverse=True)
sellersl.sort(key=lambda x:x.price,reverse=True) 
  
for k in buyersl:
    buyersTree.add(k)




    


print ("buyersl",list(map(lambda x:x.name+"  "+str(x.time)+"  "+str(x.price),buyersl)))
print ("sellersl",list(map(lambda x:x.name+"  "+str(x.time)+"  "+str(x.price),sellersl)))




    
buyersTree.preOrder(buyersTree.root)
##buyersTree.inOrder(buyersTree.root)
##buyersTree.postOrder(buyersTree.root)





answer=[]
for j in sellersl:
  answer.append(match(j,buyersTree))

print (answer)    
    
    


