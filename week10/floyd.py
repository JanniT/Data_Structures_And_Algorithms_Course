# Floyd's Algorithm which finds the shortest distance between all pair of vertices

from graph import Graph

def floyd(graph):
     
    N = len(graph.graph_MF)
    INF = 99999                 # Making a huge number that indicates the infinite   
    
    # Making a new list filled with INF
    new_list = [[INF for i in range(N)] for i in range(N)]
    
    # Going through the matrix and getting the weights 
    for i in range(N):
        row = dict(graph.graph_MF[i])       # Getting the rows of matrix from the graph.py
        for j in range(N):                  
            new_list[i][j] = 0 if i == j else row.get(j, INF)   
            # Adding zeros to the list as the distance of node1 to node1 (itself) is zero, else adding INF to the place

    # Floyd's algorithm is presented here
    for k in range(N):
        for i in range(N):
            for j in range(N):
                new_list[i][j] = min(new_list[i][j], new_list[i][k] + new_list[k][j])

    # Changing all the infinite numbers (INF's) to zeros if there's them 
    # after the algorithm
    for i in range(1, N*N):                 # Lenght * lenght (N*N) is the whole matrix to be gone through
        if new_list[int(i/N)][i % N] == INF: 
            new_list[int(i/N)][i % N] = 0

    return new_list

if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]

    graph = Graph(matrix)
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()

    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 