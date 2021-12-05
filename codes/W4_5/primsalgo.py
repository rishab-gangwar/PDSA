def prim(WList):
  infinity=1+max([d for u in WList.keys() for v,d in WList[u]])*
  visited,distance,TreeEdges={},{},[]
  for v in WList.keys():
    distance[v]=False,infinity
  visited[0]=True
  for v,d in WList[0]:
    distance[v]=d
  for i in WList.keys():
    mindist,nextv=infinity,None
    for u in WList.keys():
      for v,d in WList[u]:
        if visited[u] and not visited[v] and d<mindist:
          mindist,nextv,nexte=d,v,(u,v)
    if nextv==None:
      break
    visited[nextv]=True
    TreeEdges.append(nexte)
    for v,d in WList[nextv]:
      if not visited[v]:
        distance[v]=min(distance[v],d)
  return TreeEdges


def prim2(WList):
  infinity=1+max([d for u in WList.keys() for v,d in WList[u]])*
  visited,distance,TreeEdges,nbr={},{},[],{}
  for v in WList.keys():
    distance[v],visited[v],nbr[v]=False,infinity,-1
  visited[0]=True
  for v,d in WList[0]:
    distance[v],nbr[v]=d,0
  for i in range(1,len(WList.keys())):
    nextd=min([distance[v] for v in WList.keys() if not visited[v]])
    nextvlist=[v for v in WList.keys() if not visited[v] and distance[v]==nextd)
    if nextv==None:
      break
    nextv=min(nextvlist)
    visited[nextv]=True
    for v,d in WList[nextv]:
      if not visited[v]:
        distance[v],nbr[v]=min(distance[v],d),nextv
  return nbr