import heapq

def print_graph(graph):
    print("Граф (список суміжності):")
    for vertex in sorted(graph):
        edges = ", ".join(f"{neighbor}({weight})" for neighbor, weight in graph[vertex])
        print(f"  {vertex} -> {edges}")
    print()

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3)],
        'E': [('C', 8), ('D', 3)]
    }

    print_graph(graph)

    start_vertex = input("Введіть початкову вершину (наприклад, A): ").upper()

    if start_vertex not in graph:
        print(f"Вершина '{start_vertex}' не знайдена в графі.")
        return

    shortest_paths = dijkstra(graph, start_vertex)

    print(f"\nНайкоротші відстані від вершини '{start_vertex}':")
    for vertex in sorted(shortest_paths):
        dist = shortest_paths[vertex]
        dist_str = f"{dist}" if dist != float('inf') else "недосяжна"
        print(f"{vertex}: {dist_str}")

if __name__ == "__main__":
    main()