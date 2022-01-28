# Dijkstra's-algorithm-applied-in-network-routing
Dijkstra's algorithm applied in network routing

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. When it is applied in network routing, it calculates and finds the shortest paths from the source node to all other nodes in the network based on the node connection and the cost/distance between any connected nodes. It keeps track of the currently known cost/distance from the source node to the rest of the nodes and dynamically updates these values if a shorter path is found.

In Project3-ShortestPathAlg.py, mgraph is the 2D matrix representing the network graph, where mgraph[i, j] denotes the cost/distance from i to j. If there is no connection between any two nodes, mgraph[i, j] = inf. Your job in this task is to complete the function startwith in the python file, which implements the Dijkstra's algorithm. In startwith function, the parameter “start” denotes the source node 0 and the return “dis” is the minimum cost/distance from the source node to all the other nodes in the network.

Find the shortest path from each source node to all other nodes by revising and running your completed code in Task 1.
