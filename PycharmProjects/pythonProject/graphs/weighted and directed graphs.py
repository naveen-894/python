class Graph:
    def __init__(self,nodes,edges,weighted=False,directed=False):
        self.nodes=nodes
        self.weighted=weighted
        self.data=[[] for _ in range(nodes)]
        self.weights=[[] for _ in range(nodes)]

        for node in edges:
            if weighted:
                node1,node2,weight=node
                self.data[node1].append(node2)
                self.weights[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weights[node2].append(weight)

            else:
                node1,node2=node
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    def __iter__(self):
        result=''
        if self.weighted:
            for i,(nodes,weights) in enumerate(zip(self.data,self.weights)):
                result+='{}:{}\n'.format(i,list(zip(nodes,weights)))
        else:
            for i,nodes in enumerate(self.data):
                result+='{}:{}\n'.format(i,nodes)
        return result

    def __str__(self):
        return self.__iter__()


graph=Graph(5,[(0,1,44),(0,4,44),(1,2,55),(1,4,66),(1,3,77),(2,3,44),(3,4,66)],True)
# graph=Graph(5,[(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)],directed=True)
print(graph.data)
print(graph)








