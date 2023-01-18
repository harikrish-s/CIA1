import heapq

def prims(graph,start):
    mst = []
    visited = set()
    heap = [(0,start)]
    while heap:
        (cost,node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            mst.append((cost,node))
            for v,c in graph[node]:
                if v not in visited:
                    heapq.heappush(heap,(c,v))
    return mst

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
mst = prims(graph,start)
print("Minimum Spanning Tree : ")
print("Cost - Vertex")
for j in mst:
    print(str(j[0])+" - "+str(j[1]))
