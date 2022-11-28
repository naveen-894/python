# dijkstras-algorithm
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


def Shortest_distance(graph,source,target):
    distances=[float('inf')]*len(graph.data)
    visited=[False]*len(graph.data)
    visited[source]=True
    distances[source]=0

    queue=[source]
    index=0

    while index<len(queue) and not visited[target]:
        current=queue[index]
        visited[current]=True
        index+=1
        update=updateDistances(graph,distances,current)
        next_node=pick_next_node(distances,visited)

        if next_node:
            queue.append(next_node)
    return distances[target]
def updateDistances(graph,distances,current):
    weights=graph.weights[current]
    nodes=graph.data[current]
    for i, node in enumerate(nodes):
        weight=weights[i]
        if distances[current]+weight<distances[node]:
            distances[node]=distances[current]+weight

def pick_next_node(distances,visited):
    next_node=None
    min_dis=float('inf')
    for i, distance in enumerate(distances):
        if not visited[i] and distance<min_dis:
            min_dis=distance
            next_node=i
    return next_node

graph=Graph(5,[(0,1,14),(0,4,4),(1,2,15),(1,4,6),(1,3,10),(2,3,3),(3,4,4)],True)
# graph=Graph(5,[(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)],directed=True)
print(graph.data)
print(graph)

print(Shortest_distance(graph,0,1))

