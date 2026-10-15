from queue import Queue as que


#====================================================
# Breadth First Search (BFS) graph search algorithm
#====================================================

#================================
# PSUEDOCODE (Python) DESCRIPTION
#================================

"""
    nodes = dict of the graph below
    
    Graph:
        A: [B, C]
        B: [A, D, E]
        C: [A, F]
        D: [B]
        E: [B, F]
        F: [C, E]
        
    start_Node = A

    start each at 0
    line = que()
    already_traveled.append(start_node)
    line.put(start_node)
 
    while not line.empty():
        current_node = line.get()
        for each neighbor in node[current_node]:
            if neighbor is not in already_traveled:
                distance[neighbor] = distance[current_node] + 1
                parent[neighbor] = current_node
                line.put(neighbor)
                already_traveled.append(neighbor)
                
"""

#=======================
#   Definitions
#=======================

nodes: dict[list[str]] = {'A': ['B','C'], 
                     'B': ['A','D','E'], 
                     'C': ['A','F'], 
                     'D': ['B'], 
                     'E': ['B','F'],
                     'F': ['C','E']}

distance: dict[int] = {'A':0,
                       'B':0,
                       'C':0,
                       'D':0,
                       'E':0,
                       'F':0}
parent: dict[str | None ] = {'A': None,
                       'B': None,
                       'C': None,
                       'D': None,
                       'E': None,
                       'F': None}

#=======================
#  BFS Function
#=======================

def bfs(nodes: dict[list[str]]):
    start_node = 'A'
    line = que()
    already_traveled: list[str] = []
    already_traveled.append(start_node)
    line.put(start_node)


    while not line.empty():
        current_node = line.get()
        for neighbor in nodes[current_node]:
            if neighbor not in already_traveled:
                distance[neighbor] = distance[current_node] + 1
                parent[neighbor] = current_node
                line.put(neighbor)
                already_traveled.append(neighbor)
        
    return already_traveled, distance, parent


if __name__ == "__main__":
    print(bfs(nodes))