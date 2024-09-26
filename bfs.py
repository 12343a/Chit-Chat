from collections import deque
def BFS(visited,graph,node):
    visited.append(node)
    q.append(node)

    while q:
        m = q.pop(0)
        print(m,end=" ")

        for n1 in graph.get(m):
            if n1 not in visited:
                visited.append(n1)
                q.append(n1)

graph={
    '5':[3,7],
    '3':[2,4],
    '7':[8],
    '2':[],
    '4':[8],
    '8':[],
}

visited=[]
q=[]
BFS(visited,graph,'5')




# from collections import deque

# def BFS(visited, graph, node):
#     visited.add(node)
#     q.append(node)

#     while q:
#         m = q.popleft()  
#         print(m, end=" ") 

#         for n1 in graph.get(m, []):
#             if n1 not in visited:
#                 visited.add(n1)  
#                 q.append(n1)     


# graph = {
#     '5': [3, 7],
#     '3': [2, 4],
#     '7': [8],
#     '2': [],
#     '4': [8],
#     '8': [],
# }

# visited = set() 
# q = deque()  


# BFS(visited, graph, '5')
