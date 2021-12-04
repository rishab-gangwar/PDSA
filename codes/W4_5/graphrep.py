edges = [(0,1),(0,4),(1,2),(2,0),
(3,4),(3,6),(4,0),(4,3),
(4,7),(5,3),(5,7),
(6,5),(7,4),(7,8),
(8,5),(8,9),(9,8)]
#Adjacency matrix representation
import numpy as np
size=10


graphmat=np.zeros((size,size))
def neighbour(mat,i):
  ngbr=[]
  for j in range(size):
    if mat[i,j]==1:
      ngbr.append(j)
  return ngbr
for i,j in edges:
  graphmat[i,j]=1


#Adjacency List representation

adjList={}
for i in range(size):
  adjList[i]=[]
for i,j in edges:
  adjList[i].append(j)
print(adjList)
print(graphmat)