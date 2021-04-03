# Python program for connected
# components in an undirected graph
import sys

class Graph:
 
    # init function to declare class variables
    # Assumption here is that data is a non empty dictionary
    def __init__(self, data:dict):
        self.data = data
        self.graph_nodes = list(data.keys())
        # create adjacency list for every node
        self.adj = [[] for i in self.graph_nodes]

    # Recursive depth first search method
    def DFSUtil(self, idx, visited):
        # Mark the current node as visited
        visited[idx] = True
        # Recur for all the nodes adjacent to this node
        for i in self.adj[idx]:
            try:
                # Get the index of the adjacent node from the graph nodes
                new_idx = self.graph_nodes.index(str(i))
                if (not visited[new_idx]):
                    self.DFSUtil(new_idx,visited)
            except ValueError:
                pass

    """ Method to add an undirected edge.
    Assumption here is that this is used in a loop with an adjacency list,
    where if v is in the adjacency list of w, then w will be in the adjacency list of v"""
    def addEdge(self, v, w):
        self.adj[v].append(w)
    
    """ Function to return the number of
    connected components in an undirected graph """
    def NumberOfconnectedComponents(self):
        # Add graph edges, 'keys' represent the nodes and 'values' the adjacent nodes
        # Assumption: every item is a string of an integer
        for key, value in self.data.items():
            if value != []:
                for item in value:
                    self.addEdge(self.graph_nodes.index(key),int(item)) 
        
        # Mark all the nodes as not visited
        visited = [False for i in self.graph_nodes]
         
        # To count the number of connected components
        count = 0
        for idx,v in enumerate(self.graph_nodes):
            if (visited[idx] == False):
                self.DFSUtil(idx,visited)
                count += 1         
        return count
 