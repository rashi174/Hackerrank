#Topological Sort

#According to Introduction to Algorithms, given a directed acyclic graph (DAG), a topological sort is a linear ordering of all vertices such that 
#for any edge (u, v), u comes before v.Another way to describe it is that when you put all vertices horizontally on a line, all of the edges are 
#pointing from left to right.  if u->v h to u will come before v in the traversal

from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph=defaultdict(list)
  
  def addEdge(self,u,v):
    self.graph[u].append(v)

  def TopologicalSort(self):
    V=6 #total number of vertices
    visited=[False]*V
    stack=[]
    for node in range(V):
      if visited[node]==False:
        self.dfs(visited,node,stack)
    return stack

  def dfs(self,visited,node,stack):
    visited[node]=True
    for nei in self.graph[node]:
      if visited[nei]==False:
        self.dfs(visited,nei,stack)
    stack.insert(0,node)

g= Graph()
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
print ("Following is a Topological Sort of the given graph")

g.TopologicalSort()
