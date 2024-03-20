from typing import Dict,List 
def short(graph,node1,node2):
    path_list = [[node1]]
    path_index = 0
    previous_nodes = {node1}
    print(previous_nodes)
    if node1 == node2 :
        return path_list[0]
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if node2 in next_nodes :
            current_path.append(node2)
            return current_path
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index +=1
    return []
graph = {
    0: {1, 2, 3},
    1: {0, 4, 5},
    2: {0},
    3: {0, 6},
    4: {1},
    5: {1},
    6: {3}
}
s = short(graph,6,0)
print(s)
