# depth first search

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

def depth_first_search(graph,root):
    stack=[root]
    discovered=[False for x in graph.data]
    parent=[]
    result=[]

    while len(stack)>0:
        current=stack.pop()
        if not discovered[current]:
            result.append(current)
            discovered[current]=True


        for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
    return result,parent


  # if len(result):
  #
  #               parent.append(result[-1])
  #           else:
  #               parent.append(None)




graph=Graph(5,[(0,1),(0,4),(1,2),(1,4),(1,3),(2,3),(3,4)])

print(graph.data)

print(depth_first_search(graph,3))
