from queue import Queue
from graphrep import neighbour
def BFS(Amat,v):
  rows,cols=Amat.shape
  visited=[]
  for i in range(rows):
    visited.append(False)
  visited[v]=True
  q=Queue()
  q.addq(v)
  while(not q.empty()):
    i=q.delq()
    for j in neighbour(Amat,i):
      if visited[j]==False:
        visited[j]=True
        q.addq(j)
  return visited
import numpy as np
size=10
def BFSl(AList,v):
  parent,visited={},[]
  for i in AList.keys():
    parent[i]=-1
    visited.append(False)
  q=Queue()
  q.addq(v)
  while(not q.empty()):
    i=q.delq()
    for j in AList[i]:
      if visited[j]==False:
        visited[j]=True
        parent[j]=i
        q.addq(j)
  return parent,visited
graphmat=np.zeros((size,size))
edges = [(0,1),(0,4),(1,2),(2,0),
(3,4),(3,6),(4,0),(4,3),
(4,7),(5,3),(5,7),
(6,5),(7,4),(7,8),
(8,5),(8,9),(9,8)]
for i,j in edges:
  graphmat[i,j]=1
for i,j in edges:
  graphmat[i,j]=1
adjList={}
for i in range(size):
  adjList[i]=[]
for i,j in edges:
  adjList[i].append(j)
print(BFS(graphmat,0))
print(BFSl(adjList,7)[0])