from collections import deque
import heapq

def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    #The output depends on whether the search_node is provided or not:
        #1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
        #2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.
    visited = set()
    queue = deque([start_node])
    path = []

    visited.add(start_node)

    while queue:
        node = queue.popleft()
        path.append(node)

        #if searching for a node
        if search_node is not None and node == search_node:
            return 1

        #traverse neighbors
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    #if search_node was provided but not found
    if search_node is not None:
        return 0

    #otherwise return traversal order
    return path
    

def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)

    # Note1: The optional parameters “visited” and “path” are initially not required to be passed as inputs but needs to be
            # updated recursively during the search implementation. If not required for your implementation purposes they can
            # be ignored and can be removed from the parameters.

    # Note2: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    # The function returns:
        # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
        # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start_node)
    path.append(start_node)

    #if search_node is provided, return boolean
    if search_node is not None:
        if start_node == search_node:
            return 1

        for neighbor in graph.get(start_node, {}):
            if neighbor not in visited:
                if dfs(graph, neighbor, visited, path, search_node) == 1:
                    return 1

        return 0

    #if not provided, return list
    for neighbor in graph.get(start_node, {}):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path, None)

    return path


def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.

    # Return the shortest path and distances
    #return [path, distance, hop_count]
    pq = [(0, start_node, [start_node])]  # (dist, node, path)
    visited = {}

    while pq:
        dist, node, path = heapq.heappop(pq)

        #reached target
        if node == end_node:
            hop_count = len(path) - 1
            return [path, dist, hop_count]

        #skip if better path has been seen before
        if node in visited and visited[node] <= dist:
            continue

        visited[node] = dist

        for neighbor, weight in graph.get(node, {}).items():
            heapq.heappush(pq, (dist + weight, neighbor, path + [neighbor]))

    return 0

# (strongly connected components)
def kosaraju(graph):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.

    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    #return components
    pass


def required_edges(graph):
    """
    Function to find all the required edges in a graph.

    Required_Edge : A required edge is an edge in a graph that, if deleted, would result in a node being
                    unable to reach another node in the graph from any of the remaining nodes in the graph.

    Input Parameter:
        Graph in dictionary format.

    Returns:
        list: A list of required edges in the graph, represented as tuples of nodes.
    """
    components = kosaraju(graph)
    #In these components take the component which have highest number of nodes (highest number of nodes = 206).
    #Filter the nodes from graph which have these components as keys in the graph (dictionary datastructure) and store in filtered_graph variable.
    #example: components = ['1', '6', '9']
    #   then filtered_graph = {
    #   '1':{'6':5, '9': 2},
    #   '6':{'9':3}
    #   '9':{}
    #   }
    #filtered_graph =
    #by using this filtered_graph find list of required_edges, represented as tuples of nodes
    #example

    #return result
    pass


# Tarjan's Algorithm

def strongconnect(graph, node, index, stack, on_stack, indices, lowlinks, scc):
    """
    Inputs:
        - graph: adjacency list representation (dictionary)
        - node: current node being processed (node identifier, e.g., string/int)
        - index: integer tracking discovery order of nodes
        - stack: list used as a stack for current DFS path
        - on_stack: set tracking nodes currently on the stack
        - indices: dictionary mapping nodes to their discovery indices
        - lowlinks: dictionary mapping nodes to the lowest reachable indices
        - scc: list collecting strongly connected components (each component is a list)

    What to Implement:
        - Perform DFS traversal to identify strongly connected components (SCCs)
        - Use indices and lowlinks to detect SCC roots and collect nodes forming each SCC

    Outputs:
        - None (updates `scc` list in-place)

    Example SCC output format:
        scc = [['A', 'B', 'C'], ['D'], ['E', 'F']]
    """
    pass  # Implement DFS logic here

def tarjan(graph):
    """
    Inputs:
        - graph: adjacency list representation (dictionary)
                 e.g., {'A': ['B'], 'B': ['C'], 'C': ['A'], 'D': []}

    What to Implement:
        - Initialize structures for tracking DFS traversal
        - Call `strongconnect` for each unvisited node to find all SCCs

    Outputs:
        - Returns a list of strongly connected components
        - Each component is represented as a list of nodes

    Example output:
        [['A', 'B', 'C'], ['D']]

    """
    pass  # Implement initialization and loop logic here


# A* Algorithm

def heuristic(a, b, graph):
    """
    Inputs:
        - a: starting node (node identifier)
        - b: goal node (node identifier)
        - graph: adjacency list with weights or additional data (dictionary)

    What to Implement:
        - A heuristic function estimating the cost from node `a` to node `b`
        - The heuristic should return a numeric value (integer or float)
        - A simple heuristic is provided as example (e.g., number of shared movies, distance, etc.)

    Outputs:
        - Numeric heuristic value indicating estimated cost from node `a` to node `b`

    Example:
        heuristic('Actor1', 'Actor2', graph) -> 3
    """
    pass  # Implement heuristic calculation here

class PriorityQueue:
    """
    Implements a priority queue data structure.

    What to Implement:
        - Initialization method to set up internal data structures
        - Method to push items onto the queue with priority values
        - Method to pop the item with the lowest priority value
        - Method to check if the priority queue is empty

    Methods and Expected behaviors:

        push(item, priority):
            Inputs:
                - item: data to store (e.g., node identifier)
                - priority: numeric value determining order (smaller number = higher priority)
            Output:
                - None (updates internal queue)

            Example usage:
                pq.push('Node1', 5)

        pop():
            Inputs:
                - None
            Output:
                - Item with lowest priority value

            Example usage/output:
                pq.pop() -> 'Node1'

        is_empty():
            Inputs:
                - None
            Output:
                - Boolean indicating if queue is empty

            Example:
                pq.is_empty() -> False
    """
    def __init__(self):
        pass  # Implement initialization logic here

    def push(self, item, priority):
        pass  # Implement item insertion logic here

    def pop(self):
        pass  # Implement item removal logic here

    def is_empty(self):
        pass  # Implement empty check logic here

def a_star(graph, start, goal):
    """
    Inputs:
        - graph: adjacency list representation with edge weights
                 e.g., {'A': {'B': 2, 'C': 1}, 'B': {'C': 2}, 'C': {'D': 3}}
        - start: starting node identifier
        - goal: goal node identifier

    What to Implement:
        - Use A* search to find the shortest path from `start` to `goal`
        - Leverage the heuristic function to optimize search
        - Manage open-set using a priority queue to prioritize exploration of nodes

    Outputs:
        - List of nodes representing the shortest path from `start` to `goal` (inclusive)
        - Return `None` if no path exists

    Example output (path from 'A' to 'D'):
        ['A', 'C', 'D']
    """
    pass  # Implement A* logic here
