import sys  # For command line argument parsing
import re   # For input file parsing

# @ Name : Lane Gramling
# @ Due Date : April 14, 2019
# @ Brief: Generates a Minimum Spanning Tree for a given weighted graph, using
#           Kruskal's Algorithm.
#  		Usage: python msp_2766765.py input.txt > output.txt

graph = {}      # Contains Graph structure
component = []  # Contains set names (array implementation for Union-Find [pg. 152])

# Read in weighted graph
def generateGraph(filename):
    matrix = [weight_list.split(' ') for weight_list in open(filename, 'r').read().split('\n')] # Read & structure input
    for row in matrix: row.remove('')                                                           # Clean input
    matrix = [list(map(int, x)) for x in matrix]                                                # Format input
    component = [s for s in range(len(matrix))]                                                 # Populate Component array
    for v_i, weight_list in enumerate(matrix):                                                  # Generate graph vertices
        if weight_list:                                                                         # ...
            graph[v_i] = {}                                                                     # ...
            for v_j, weight in enumerate(weight_list): graph[v_i][v_j] = weight                 # ... Assign weights to vertices
        else: matrix.pop(v_i)                                                                   # (Final input cleaning)

# Find operation of Union-Find structure
def FIND_SET(u):
    if component[u] != u:
        component[u] = FIND_SET(component[u])
    return component[u]

# Union definition
def union(A, B):
    pass # DEBUG

# Perform Kruskal's Algorithm to compute MST
def kruskal(graph):
    VERTEX_COUNT = range(len(graph))                                 # (Number of Vertices)
    MST = set()                                                      # Stores resulting MST
    edges = set()                                                    # Stores Edge set

    for u in VERTEX_COUNT:
        for v in VERTEX_COUNT:                                       # Build edge set from graph
            if graph[u][v] != 0 and (u, v) not in edges:                 # Generate edges list
                edges.add((u, v))
    edges = sorted(edges, key=lambda edge: graph[edge[0]][edge[1]])      # Sort edges (by weight)
    for edge in edges:                                               # Perform Union-Find operations in MST generation
        u, v = edge
        if FIND_SET(u) != FIND_SET(v):                               # Determine whether connected
            MST.add((u, v))                                             # Append edge to resulting MST set
            union(u, v)                                                 # Perform Union operation on (u, v) edge pairing










# Execution on runtime
if len(sys.argv) < 2:
    print("[Usage]: python msp_2766765.py <input-file> > <output-file>")
else:
    generateGraph(sys.argv[1])                # Generate graph structure
    MST = kruskal(graph)                           # Compute MST
