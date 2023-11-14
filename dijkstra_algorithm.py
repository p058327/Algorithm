import heapq
from tqdm import tqdm


def relax_neighborhoods(point, heap, visits_nodes, graph):
    """Updating the cost of the route from the starting point to the nodes adjacent to the node that left the heap"""
    # Verifies the existence of the neighboring object
    for neighbor in point.neighborhoods:
        if neighbor in visits_nodes:
            neighbor_obj = visits_nodes[neighbor]
        else:
            neighbor_obj = graph[neighbor]
        if point.distance + point.neighborhoods[neighbor] < neighbor_obj.distance:
            neighbor_obj.distance = point.distance + point.neighborhoods[neighbor]
            neighbor_obj.previous = point
            heapq.heappush(heap, neighbor_obj)
            visits_nodes[neighbor] = neighbor_obj


def dijkstra(start, end, graph: dict):
    """Gets a graph of GraphNode objects with weights for the arcs, and calculates the path with the lowest weight"""
    visits_nodes = {}
    final_group = set()
    start_node = graph[start]
    start_node.distance = 0
    heap = [start_node]
    current_position = start_node
    tq = tqdm()
    # Dijkstra's algorithm terminates when the cheapest route is found or no route is possible.
    while heap and current_position.position != end:
        tq.update(1)
        relax_neighborhoods(current_position, heap, visits_nodes, graph)
        final_group.add(current_position)
        # Ignore duplicates in minimum stack, This income will not affect efficiency.
        while current_position in final_group and heap:
            current_position = heapq.heappop(heap)
    final_group.add(current_position)
    return current_position
