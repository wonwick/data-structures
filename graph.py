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
        V1=self.get_v(data1)
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


    def path(self,data1,data2):
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
        
                


                
g=Graph(True)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("D","E")
g.add_edge("D","F")
g.add_edge("D","A")
g.add_edge("F","G")
g.add_edge("G","H")


g.print_graph()
print("___________________")
print ("ans",map(lambda x:x.data+"->",g.path("A","G")))



































            
            
        
