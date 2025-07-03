import csv
import heapq

# Load graph from CSV
def load_graph(filename):
    graph = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            src, dst = row['from'], row['to']
            time = float(row['time_min'])

            graph.setdefault(src, []).append((dst, time))
            graph.setdefault(dst, []).append((src, time))  # bidirectional
    return graph

# Dijkstra's algorithm
def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        (cost, current, path) = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)
        path = path + [current]

        if current == end:
            return path, cost

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path))

    return None, float('inf')

def calculate_fare(time_minutes):
    # ₹10 for first 5 mins, then ₹5 per 5 min chunk
    if time_minutes <= 5:
        return 10
    extra = ((time_minutes - 5) + 4.9) // 5  # ceiling division
    return 10 + int(extra) * 5
