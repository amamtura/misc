#!/usr/bin/env python

from Queue import Queue

# visits all the nodes of a graph (connected component) using BFS
def bfsConnectedComponent(graph, start):
    # keep track of nodes to be processed
    queue = Queue()
    queue.put(start)

    levels = { start: 0 }     # this dict keeps track of levels
                              # depth of start node is 0

    visited = [start]         # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be processed
    while not queue.empty():
        node = queue.get()
        neighbours = graph[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.put(neighbour)
                visited.append(neighbour)
                levels[neighbour] = levels[node] + 1

    return levels, visited

if __name__ == '__main__':

    # sample graph implemented as a dictionary
    graph = {
            'A': ['B', 'C', 'E'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']
            }

    levels, visited = bfsConnectedComponent(graph,'A') # ['A', 'B', 'C', 'E', 'D', 'F', 'G']

    print('graph as dict = %s' % graph)
    print('')
    print('visited %s' % visited)
    print('')
    formatPrintingByLevel = 0
    for k, v in levels.items():
        if v != formatPrintingByLevel:
            formatPrintingByLevel = v
            print('')
        print('%s: %s' % (k, v))
    print('')
    print('B is at level %s' % levels['B'])
    print('G is at level %s' % levels['G'])

