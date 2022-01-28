import string

from queue import PriorityQueue

def startwith(start, mgraph, inf) :
    num_of_nodes = len(mgraph)
    dist = {node:inf for node in range(num_of_nodes)}
    dist[start] = 0
    visited = []
    shortest_dist = PriorityQueue()
    shortest_dist.put((0, start))

    while not shortest_dist.empty():
        (distant, node_now) = shortest_dist.get()
        visited.append(node_now)

        for node_next in range(num_of_nodes):
            if mgraph[node_now][node_next] != inf:
                if node_next not in visited:
                    dist_by_now = dist[node_now] + mgraph[node_now][node_next]
                    if dist_by_now < dist[node_next]:
                        shortest_dist.put((dist_by_now, node_next))
                        dist[node_next] = dist_by_now    
    
    return dist

if __name__ == "__main__":

    inf = 10086

    mgraph = [[0, 7, 2, inf, inf, inf],

              [7, 0, 7, 1, 2, inf],

              [2, 7, 0, inf, 8, 1],

              [inf, 1, inf, 0, inf, 1],

              [inf, 2, 8, inf, 0, 6],

              [inf, inf, 1, 1, 6, 0]]

    s=string.ascii_uppercase
    num_of_nodes = len(mgraph)
    task2 = open("Task2.txt", 'w+')
    for n in range(0, num_of_nodes):
        dis = startwith(n, mgraph, inf)
        for i in range(0, num_of_nodes):
            if i != n:
                print(s[n], "->", s[i], ":", dis[i], file = task2)
    task2.close()
        