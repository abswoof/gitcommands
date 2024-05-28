def is_safe(graph,node,colors,color_nodes):
    for neighbour in graph[node]:
        if neighbour in color_nodes and color_nodes[neighbour]==colors:
            return False
        return True

def graph_coloring(graph,node,colors,color_nodes):

    if node==len(graph):
        return True
    for color in colors:
        if is_safe(graph,node,color,color_nodes):
            color_nodes[node]=color
            if graph_coloring(graph,node+1,colors,color_nodes):
                return True
            color_nodes[color]=None
    return False

graph={
    0:[1,2],
    1:[0,3,4],
    2:[1,2,5],
    3:[0,5]
}
colors=['red','green','blue']
color_nodes={}
graph_coloring(graph,0,colors,color_nodes)

for node,color in color_nodes.items():
    print(f"{node}:{color}")
    print('changed by git')
