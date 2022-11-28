class Graph:
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.data=[[] for _ in range( nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return '\n'.join( ['{}:{}'.format(x,value) for x,value in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()
graph=Graph(5,[(0,1),(0,4),(1,2),(1,4),(1,3),(2,3)])
print(graph)