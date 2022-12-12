# Implementing a graph

from queue import Queue

class Graph:
    
    def __init__(self, matrix):
        self.graph_matrix = matrix
        self.graph_list = []
    
    # Converting the adjacency matrix to a adjacency list
    def convertion(self): 
        matrixc = self.graph_matrix
        adjlist = {}

        for i in range(len(matrixc)):    # Creating the structure of the adjacency list
            adjlist[i] = []

        for index, row in enumerate(matrixc):
            for j, column in enumerate(row):
                if column != 0:
                    adjlist[index].append(j)

        # print(adjlist)
        return adjlist

    # Depth-first search via recursion
    def dj_print_help(self, startig_vertex, path = []):
        adjlist = self.convertion()

        if startig_vertex not in path:
            path += [startig_vertex]

        for neighbor in adjlist[startig_vertex]:
            if neighbor not in path:
                path = self.dj_print_help(neighbor, path)
        return path

    def df_print(self, startig_vertex):
        path = []
        path2 = self.dj_print_help(startig_vertex, path)
        for item in path:
            print(item, end=" ")
        print("")
        #print(*path2)
        return 

    # Breadth-first search via pythons Queue() function
    def bf_print(self, startig_vertex):
        adjlist = self.convertion()

        Que = Queue()
        visited_vertices = []

        Que.put(startig_vertex)

        while not Que.empty():

            vertex = Que.get()

            if vertex not in visited_vertices: 
                visited_vertices.append(vertex)

            else: 
                continue

            for number in adjlist[vertex]:
                if number not in visited_vertices:
                    Que.put(number)

        for item in visited_vertices:
            print(item, end=" ")
        print("")
        return 

    def weight(self, vertex1, vertex2):
        # vertex1 is the x cordinate and vertex2 is y cordinate
        # rows = len(matrixc)
        # columns = len(matrixc[0])
        matrixc = self.graph_matrix 
        
        row = matrixc[vertex1] 

        if row[vertex2] != 0: 
            return row[vertex2]
        else: 
            return -1

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

    graph.df_print(0)           # 0 2 1 3 5 4 
    graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1

     # matrix = [
    # #    0  1  2  3  4  5
    #     [0, 1, 0, 0, 2, 0], # 0
    #     [1, 0, 0, 0, 0, 2], # 1
    #     [0, 0, 0, 0, 4, 0], # 2
    #     [0, 0, 0, 0, 4, 5], # 3
    #     [2, 0, 4, 4, 0, 1], # 4
    #     [0, 2, 0, 5, 1, 0]  # 5   
    # ]

    # graph = Graph(matrix)     
    # print(graph.weight(4, 2))  
    # print(graph.weight(5, 2))  
    
    # print(graph.weight(5, 4))
    # print(graph.weight(0, 3))
    # print(graph.weight(1, 0))