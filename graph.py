class Vertex:
    
    def __init__(self,Data):
        self.data=Data
        self.neighbours=None
        self.others=None
        self.visited=False
        self.discoverd=False
        self.pred=None


    def add_neighbour(self,N):
        current=self.neighbours

        if self.neighbours==None:
            self.neighbours=N
            return
        
        if self.neighbours.vertex==N:
            raise NameError ("<{0}> already exists".format(N.vertex.data))
            
        else:
            while current.next!=None and current.next!=N:
                current=current.next
            if current.next==None:
                current.next=N
            elif current.next==N:
                raise NameError ("<{0}> already exists".format(N.vertex.data))


            
            
class Neighbour:
    
    def __init__(self,Vertex):
        self.vertex=Vertex
        self.next=None


        
        
class Graph:
    
    def __init__(self,dirrected):
        self.start=None
        self.dirrected=dirrected


    def add_vertex(self,Data):
        newV=Vertex(Data)
        current=self.start
        
        if self.start==None:
            self.start=newV
            return
        
        if self.start.data==Data:
            raise NameError ("<{0}> already exists".format(Data))
            
        else:
            while current.others!=None and current.others.data!=Data:
                current=current.others
            if current.others==None:
                current.others=newV
            elif current.others.data==Data:
                raise NameError ("<{0}> already exists".format(Data))
            

    def add_edge(self,data1,data2):
        try:
            V1=self.get_v(data1)
        except:
            self.add_vertex(data1)
            V1=self.get_v(data1)
        try:
            V2=self.get_v(data2)
        except:
            self.add_vertex(data2)
            V2=self.get_v(data2)
        v2n=Neighbour(V2)
        V1.add_neighbour(v2n)

        if not self.dirrected:        
            v1n=Neighbour(V1)
            V2.add_neighbour(v1n)

            
    def get_v(self,Data):
        current=self.start
        
        while  current!=None and current.data!=Data:
            current=current.others
            
        if current==None:
            raise NameError ("<{0}> doesnt exist".format(Data))
        
        return current

        
    def get_vertices(self):
        current=self.start
        ans=[]
        while current!=None :
            ans.append(current.data)
            current=current.others
            
        return ans
        

    def get_neighbours(self,Data):
        v=self.get_v(Data)
        current=v.neighbours
        ans=[]
        while current!=None :
            ans.append(current.vertex)
            current=current.next
            
        return ans
    

    def print_graph(self):
        current=self.start
        ans2=[]
        while current!=None :
            x=current.data
            current2=current.neighbours
            sup=[]            
            while current2!=None :
                sup.append(current2.vertex.data)
                current2=current2.next
                
            ans2.append((x,sup))
            current=current.others
            
        print ans2


    def BFS_path(self,data1,data2):
        self.reset()
        v1=self.get_v(data1)
        v2=self.get_v(data2)
        current=v1
        l=[]
        l.append(current)
        ans=[]
        while len(l)>0:
            current=l.pop(0)
            if current==v2:                        
                break
                
            elif not current.visited:                
                current.visited=True
                
                ll=self.get_neighbours(current.data)
                if len(ll)>0:
                    for i in ll:
                        if i.discoverd:
                            pass
                        else:
                            i.pred=current
                            i.discoverd=True
                    l.extend(ll)    
            else:
                pass
                        

        
        while not current.pred==v1:
            ans.insert(0,current.pred)
            current=current.pred
            
        ans.insert(0,v1)

        return ans
    

    def shortest_way_len(self,v1,v2):
        return len(self.path(v1,v2))

    def reset(self):
        current=self.start
        while current.others!=None:
            current.visited=False
            current.discoverd=False
            current.pred=None
            current=current.others

    def DFS_path(self,data1,data2):
        self.reset()
        v1=self.get_v(data1)
        v2=self.get_v(data2)
        current=v1
        current.pred=v1
        l=[]
        l.append(current)
        ans=[]
        while len(l)>0:
            current=l.pop()
##            print current.data,"    pred: ",current.pred.data
            
            if current==v2:                        
                break
                
            elif not current.visited:                
                current.visited=True
                current.discoverd=True
                ll=self.get_neighbours(current.data)
##                print "ll: ",map(lambda x:x.data,ll)
                
                if len(ll)>0:
                    for i in ll:
                        if i.discoverd:
##                            print i.data,"already discovered"
                            pass
                        else:
##                            print i.data," pred is set to ",current.data
                            i.pred=current
                            i.discoverd=True
                    l.extend(ll)
                    
            else:
                pass
##            print map(lambda x:x.data,l)
            
                        

        
        while not current.pred==v1:
            ans.insert(0,current.pred)
            current=current.pred
##            print "ans",map(lambda x:x.data,ans)
            
        ans.insert(0,v1)

        return ans
        
        
        
        
                
                
g=Graph(False)



string="lab,a,h,d g,a d,a b,a c,b e,e f,f g,g h"
string=string.split(",")
word=string[0]
start=string[1]
end=string[2]
string=string[3:]
for i in string:
    x=i.split()
    g.add_edge(x[0],x[1])

ans=map(lambda x:x.data,g.BFS_path(start,end))

for j in ans:
    word+=j


print word+end

word="lab"


ans=map(lambda x:x.data,g.DFS_path(start,end))

for j in ans:
    word+=j


print word+end
































            
            
        
