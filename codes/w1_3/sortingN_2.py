def selectionsort(list_):
  if len(list_)<=1:
    return list_
  for i in range(len(list_)):
    miN=i
    for j in range(i,len(list_)):
      if list_[miN]>list_[j]:
        miN=j
    list_[i],list_[miN]=list_[miN],list_[i]
  return list_

def insertionsort(list_):
  if len(list_)<=1:
    return list_
  for i in range(len(list_)):
    j=i
    while( j >0 and list_[j-1]>list_[j]):
      list_[j],list_[j+1] = list_[j+1],list_[j]
      j-=1
  return list_
def insert(list_,v):
  if len(list_)==0:
    return [v]
  if v>=list_[-1]:
    return list_+[v]
  else:
    return insert(list_[:-1],v)+l[-1]
def Isort(list_):
  n = len(list_)
  if n<=1:
    return list_
  else:
    return insert(Isort(list_[:-1]),list_[-1])