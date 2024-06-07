import heapq

def dijkstra(graph, start):
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0 
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances

graph = {
    'A': {'B': 6, 'C': 4},
    'B': {'A': 1, 'F': 1, 'C': 5, 'D': 5},
    'C': {'A': 11, 'B': 2, 'F': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
    'F': {'B': 8, 'C': 1}
}

shortest_paths = dijkstra(graph, "A")

for vertex, distance in shortest_paths.items():
    print(f"Distance A - {vertex}: {distance}")
