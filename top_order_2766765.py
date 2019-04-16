import sys  # For command line argument parsing
import re   # For input file parsing

# @ Name : Lane Gramling
# @ Due Date : April 4, 2019
# @ Brief: Generates a Topological Ordering for a given DAG provided its adjacency list structure
#  		Usage: python top_order_2766765.py input.txt > output.txt

ordering = []

# Read in an adjacency list from a text file
def readAdjacencyList(filename):
    edges = []      # Contains all edges, size |E|
    graph = {}      # Contains the graph structure, constructed from edges
    for line in open(filename, 'r').read().split('\n'):                                  # Read in file
        if line: edges.append(tuple(list(map(int, re.sub(r'\s', '', line).split(','))))) # Collect edges
    nodes = list(set([v for outgoing in list(edges) for v in outgoing]))                 # Generate list of nodes to create
    for u in nodes: graph[u] = []                                                        # Create all nodes 1..n
    for (u, v) in edges: graph[u].append(v)                                              # Add all edges to all nodes
    return (edges, graph)

# Compute a topological ordering, given an an adjacency list of edges describing a DAG
def top_order(graph):
    if graph:
        for node in graph:                                                             # Check every remaining node...
            if node not in [v for outgoing in list(graph.values()) for v in outgoing]: # if node has no incoming edges from any other node
                ordering.append(node)                                                  # Append v to ordering
                graph.pop(node)                                                        # Delete v from G
                top_order(graph)                                                       # Recurse on G - {v}
                break

# Execution on runtime
if len(sys.argv) < 2:
    print("[Usage]: python top_order_2766765.py <input-file> > <output-file>")
else:
    edges, graph = readAdjacencyList(sys.argv[1])       # Generate the edges list and graph structure (only need graph though)
    top_order(graph)                                    # Compute topological ordering
    for node in ordering: print(node, end=" ")          # Print output