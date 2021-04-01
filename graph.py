# Python program to print connected
# components in an undirected graph
import json
import sys

class Graph:
 
    # init function to declare class variables
    # Assumption here is that data should not be an empty dictionary
    def __init__(self, data:dict):
        self.graph_nodes = list(data.keys())
        # Add the value of first node to the length of the keys we have, 
        # if not 0 it will ensure indexes are properly bounded
        self.V = len(data.keys()) + int(next(iter(data)))
        self.adj = [[] for i in range(self.V)]

    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.adj[v]:
            if (not visited[i]):
                self.DFSUtil(i, visited)

    """ Method to add an undirected edge.
    Assumption here is that this is used in a loop with an adjacency list,
    where if v is in the adjacency list of w, then w will be in the adjacency list of v"""
    def addEdge(self, v, w):
        self.adj[v].append(w)
    
    """ Function to return the number of
    connected components in an undirected graph """
    def NumberOfconnectedComponents(self):
         
        # Mark all the vertices as not visited
        visited = [False for i in range(self.V)]
         
        # To store the number of connected
        # components
        count = 0
        for v in range(self.V):
            if (str(v) in self.graph_nodes and visited[v] == False):
                self.DFSUtil(v, visited)
                count += 1         
        return count
 