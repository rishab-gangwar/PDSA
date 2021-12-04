def toposort(Amat):
  (r,c)=mat.shape
  toposortlist,indegree=[],{}
  for col in range(c):
    indegree[col]=0
    for row in range(r):
      if Amat[row,col]==1:
        indegree[col]+=1
  for i in range(r):
    j=min([k for k in range(c) if indegree[k]==0])
    toposortlist.append(j)
    indegree[j]-=1
    for k in range(c):
      if Amat[j,k]==1:
        indegree[k]-=1
  return toposortlist


def toposortL(AList):
  indegree,toposortlist={},[]
  lpath={}
  for u in AList.keys():
    indegree[u]=0
    lpath[u]=0
  for u in AList.keys():
    for v in AList[u]:
      indegree[v]+=1
  zerodegreeq=Queue()
  for u in AList.keys():
    if indegree[u]==0:
      zerodegreeq.addq(u)
  while (not zerodegreeq.isempty()):
    j=zerodegreeq.delq()
    toposortlist.append(j)
    indegree[j]-=1
    for k in AList[j]:
      indegree[k]-=1
      lpath[k]=max(lpath[k],lpath[j]+1)
      if indegree[k]==0:
        zerodegreeq.addq(k)
  return(toposortlist,lpath)