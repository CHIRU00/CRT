
#implementayion graph
from collections import defaultdict
#Add edges to graph:fun
graph = defaultdict(list)
def ae(graph,u,v):
    graph[u].append(v)
##function Description
    
def ge(graph):
    edges=[]
    #for each node in graph
    for node in graph:
        #for each neighbour node of a single node 
        for neighbour in graph[node]:

            #if edge exists then append
            edges.append((node,neighbour))
    return edges
ae(graph,'a','c')
ae(graph,'b','c')
ae(graph,'b','e')
ae(graph,'c','d')
ae(graph,'c','e')
ae(graph,'c','a')
ae(graph,'c','b')
ae(graph,'e','b')
ae(graph,'d','c')
ae(graph,'e','c')
#printing graph
print(ge(graph))
