# breadth-first-search
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

def Breadth_first_search(graph,root):
    queue=[]
    discoverd=[False for _ in graph.data]
    distance=[]
    parent=[]

    index=0
    queue.append(root)
    discoverd[root]=True
    distance.append(index)
    parent.append(None)

    while index<len(queue):
        current=queue[index]
        index+=1

        for node in graph.data[current]:
            if not discoverd[node]:
                queue.append(node)
                discoverd[node]=True
                parent.append(current)
                distance.append(index)
    return queue,distance,parent

graph=Graph(5,[(0,1),(0,4),(1,2),(1,4),(1,3),(2,3),(3,4)])

print(graph.data)

print(Breadth_first_search(graph,3))
