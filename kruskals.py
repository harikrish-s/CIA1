import heapq

def krusals(graph,start):

vertex = int(input("Enter the no.of vertices : "))
edge = int(input("Enter the no.of edges : "))
graph = {i: [] for i in range(vertex)}
for i in range(edge):
    print("\n===== EDGE "+ str(i) +" =====")
    src = int(input("Enter the source node : "))
    dest = int(input("Enter the destination node : "))
    weight = int(input("Enter the weight of the edge : ")) 
    graph[src].append((dest,weight))
print("\n==========")
start = int(input("Enter the starting vertex : "))
output = prims(graph,start)
print("Kruskals : ")
