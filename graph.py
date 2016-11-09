class Vertex:
    def __init__(self,Data):
        self.data=Data
        self.neigbours=None
        self.others=None

    def add_neighbour(self,V):
        current=self.others
        while current!=None or current=V:
            current=current.next
        if current==V:
            print "{0} already exists in the graph".format()
        else:
            current=V
            
class Neighbour:
    def __init__(self,Vertex):
        self.vertex=Vertex
        self.next=None
        
class graph:
    def __init__(self):
        self.start=None
        self.dirrected=True

    def add_vertex(self,Data):
        newV=Vertex(Data)
        current=self.start
        while current!=None or current.Data!=Data:
            current=current.others
        if current.data==Data:
            print "{0} already exists in the graph".format(Data)
        else:
            current=newV

    def get_v(self,Data):
        current=self.start       
        while  current.Data!=Data:
            current=current.others
        return current

    def add_edge(self,data1,data2):
        current=self.start
        while current!=None or (current.Data!=Data1 or current.Data!=Data2) :
            current=current.others

        if current==None:
            print "{0}, {1} doesnt exist".format(Data1,Data2)






































            
            
        
