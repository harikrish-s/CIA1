import heapq

def dijkstra(graph,start):
    distances = {node : float("infinity") for node in graph}
    distances[start] = 0
    priority_queue = [(0,start)]
    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor,weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return distances

graph = {}
vertex = int(input("Enter the no.of vertices  :  "))
for i in range(vertex) :
    node = input("Enter Vertex name : ")
    edges_dict = {}
    edges = int(input("Enter the number of edges for Vertex %s : " % node))
    for j in range(edges) :
        neighbor = input("Enter the adjacent vertex name  : ")
        weight = int(input("Enter the weight of the edge : "))
        edges_dict[neighbor] = weight
    graph[node] = edges_dict
start = input("Enter the starting node : ")
output = dijkstra(graph,start)
print("Dijsktra's : ")
print(output)
