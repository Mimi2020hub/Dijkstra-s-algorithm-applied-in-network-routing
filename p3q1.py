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

    mgraph = [[0, 1, 12, inf, inf, inf],

              [inf, 0, 9, 3, inf, inf],

              [inf, inf, 0, inf, 5, inf],

              [inf, inf, 4, 0, 13, 15],

              [inf, inf, inf, inf, 0, 4],

              [inf, inf, inf, inf, inf, 0]]


    dis = startwith(0, mgraph, inf)
    task1 = open("Task1.txt", 'w+')
    for i in range(1, len(mgraph)):
        print("0->", i, ":", dis[i], file = task1)
    task1.close()

    
        