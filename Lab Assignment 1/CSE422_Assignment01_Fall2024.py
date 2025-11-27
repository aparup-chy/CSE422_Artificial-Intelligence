
import heapq

graph = {}
heuristic_vals = {}

def heuristic_update(info):
    heuristic_vals[info[0]] = int(info[1])

def create_graph(allinfo):
    parent = allinfo[0]
    graph[parent] = {}
    for i in range(2, len(allinfo), 2):
        leaf_node = allinfo[i]
        weight = int(allinfo[i + 1])
        graph[parent][leaf_node] = weight

def A_star_Algo(source, dest):
    heap_q = []
    heapq.heappush(heap_q, (int(heuristic_vals[source]), 0, source, [source]))
    visited = []
    while heap_q:
        _, weight, city, path = heapq.heappop(heap_q)
        if city in visited:
            continue
        visited.append(city)
        if city == dest:
            return weight, path
        for leaf, cost in graph[city].items():
            total_weight = weight + cost
            p_value = total_weight + heuristic_vals[leaf]
            heapq.heappush(heap_q, (p_value, total_weight, leaf, path + [leaf]))
    return None

with open('input.txt') as file:
    n = file.readlines()
    #print(n)
    for i in n:
        infos = i.split()
        #print(infos)
        heuristic_update(infos)
        create_graph(infos)

start = input("Start Node : ")
end = input("Destination : ")
algo = A_star_Algo(start, end)
out = open('output.txt', "w")

if algo:
    print(f"\nPath: {' -> '.join(algo[1])}")
    print(f"Total distance: {algo[0]} km")
    out.write(f"Path: {' -> '.join(algo[1])}\nTotal Distance: {algo[0]}km")
else:
    print("NO PATH FOUND")
