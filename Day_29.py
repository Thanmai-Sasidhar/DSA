'''
Weighted Graph

Non Weighted Graph

Directed Graph

Un-Directed Graph
'''

#Graph adjacent elements align 

#UNWEIGHTED GRAPH
'''
class graph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[] # creates node in graph and assign empty list 
    def add_edges(self,e,v):
        self.graph.setdefault(e,[]).append(v) # Applies the connection to join from both sides 
        self.graph.setdefault(v,[]).append(e) #
    def display(self):
        for vertex in self.graph:
            print(vertex,"->",self.graph[vertex])

g=graph()
g.add_edges("A","B")
g.add_edges("A","D")
g.add_edges("A","C")
g.add_edges("B","C")
g.add_edges("B","D")
g.display()                
'''


#Directed Graph
'''
class graph:
    def __init__(self):
        self.graph={}
    
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[] # creates node in graph and assign empty list 
    
    
    def add_edges(self,e,v):
        if e not in self.graph:
            self.graph[e]=[]
        if v not in self.graph:
            self.graph[v]=[]    
        self.graph[e].append(v)
    
    
    def display(self):
        for vertex in self.graph:
            print(vertex,"->",self.graph[vertex])

g=graph()
vertices=int(input("Enter the no of vertices: "))
for i in range(vertices):
    vertex=(input("Enter the vertex: "))
    g.add_vertex(vertex)
edges=int(input("Enter the no of edges: "))
for i in range(edges):
    e=(input("Enter the source: "))    
    v=(input("Enter the destination: "))
    g.add_edges(e,v)
g.display()
'''    
        
        
                    
