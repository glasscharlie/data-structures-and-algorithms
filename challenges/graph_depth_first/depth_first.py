def DFSUtil(graph, v, visited): 
    visited[v] = True
    print(v, end = ' ') 
    for i in graph.graph[v]: 
        if visited[i] == False: 
            graph.DFSUtil(i, visited) 

def DFS(graph, v): 
    visited = [False] * (len(graph.graph)) 
    return graph.DFSUtil(v, visited)