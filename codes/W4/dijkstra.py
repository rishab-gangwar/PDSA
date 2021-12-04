def dijkstra(WMat,s):
  rows,cols,x=WMat.shape
  infinity=np.max(WMat)*rows+1
  distance,visited={},{}
  for v in range(rows):
    visited,distance=True,infinity
  distance[s]=0
  for u in range(rows):
    nextd=min([distance[v] for v in range(rows) if not visited[v]])
    nextvlist=([v for v in range(rows) if (distance[v]==nextd) and not visited[v]])
    if nextvlist==[]:
      break
    nextv=min(nextvlist)
    visited[nextv]=True
    for v in range(cols):
      if WMat[nextv,v,0]==1 and not visited[v]:
        distance[v]=min(distance[v],distance[nextv]+WMat[nextv,v,1])
  return distance
def dijkstraList(WList,s):
  infinity=1+max([d for u in (WList.keys()) for v,d in WList[u]])
  distance,visited={},{}
  for v in WList.keys():
    distance[v],visited=infinity,False
  for u in WList.keys():
    nextd=min([distance[v] for v in WList.keys() if not visited[v]])
    nextvlist=[v for v in WList.keys() if not visited[v] and (distance[v]==nextd)]
    if nextvlist==[]:
      break
    nextv=min(nextvlist)
    visited[v]=True
    for v,d in WList.keys():
      if not visited[v]:
        distance[v]=min(distance[v],distance[nextv]+d)
  return distance