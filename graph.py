class Vertex:
    
    def __init__(self,Data):
        self.data=Data
        self.neighbours=None
        self.others=None


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
    
    def __init__(self):
        self.start=None
        self.dirrected=True


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

                            
    def print_vertices(self):
        current=self.start
        ans=[]
        while current!=None :
            ans.append(current.data)
            current=current.others
        print ans
        



    def print_neignours(self,Data):
        v=self.get_v(Data)
        current=v.neighbours
        ans=[]
        while current!=None :
            ans.append(current.vertex.data)
            current=current.next
        print ans

    def print_graph(self):
        current=self.start
        ans=[]
        ans2=[]
        while current!=None :
            ans.append(current.data)
            current2=current.neighbours
            sup=[]            
            while current2!=None :
                sup.append(current2.vertex.data)
                current2=current2.next
                
            ans2.append(sup)
            current=current.others
      
        print ans
        print ans2
    






g=Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_edge("A","B")
g.add_edge("B","A")
g.add_edge("A","C")
g.add_edge("B","D")

g.print_graph()


































            
            
        
