class Vertex:
    
    def __init__(self,Data):
        self.data=Data
        self.neigbours=None
        self.others=None


    def add_neighbour(self,V):
        current=self.others
        while current!=None or current==V:
            current=current.next
        if current==V:
            print "{0} already exists in the graph".format()
        else:
            current=V

            
            
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

                            
    def print_vertices(self):
        current=self.start
        ans=[]
        while current!=None :
            ans.append(current.data)
            current=current.others
        print ans


    def print_edges(self,Data):
        current=self.start
        

    def get_v(self,Data):
        current=self.start
        
        while  current!=None and current.data!=Data:
            current=current.others
            
        if current==None:
            raise NameError ("<{0}> adoesnt exist".format(Data))
        
        return current
    

    def add_edge(self,data1,data2):
        current=self.start
        V1=None
        V2=None
        
        while current!=None or (current.Data!=Data1 or current.Data!=Data2) :
            current=current.others

        if current==None:
            print "{0}, {1} doesnt exist".format(Data1,Data2)
            return None
        
        if current.data== data1:
            V1=current
            
            while current!=None or current.Data!=Data2 :
                current=current.others
                
        elif current.data== data2:
            while current!=None or current.Data!=Data1:
                current=current.others
                
        if v1==None:
            print "<{0}> does not exist".format(data1)
            return None

        if v2==None:
            print "<{0}> does not exist".format(data2)
            return None
        
        v1n=Neighbour(v1)
        v2n=Neighbour(v2)
        v1.add_neighbour(v2n)
        v2.add_neighbour(v1n)




g=Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")


g.print_vertices()


































            
            
        
