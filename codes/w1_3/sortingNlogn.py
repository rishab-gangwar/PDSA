def merge(la,lb):
  m,n=len(la),len(lb)
  C,i,j,k=[],0,0,0
  while k<m+n:
    if i==m:
      C.extend(lb[j:])
      k+=(n-j)
    elif j==n:
      C.extend(la[i:])
      k+=(m-i)
    elif la[i]>lb[j]:
      C.append(lb[j])
      j,k=j+1,k+1
    else:
      C.append(la[i])
      i,k=i+1,k+1
  return C
def mergesort(list_):
  if len(list_)<=1:
    return list_
  L=mergesort(list_[:len(list_)//2])
  R=mergesort(list_[len(list_)//2:])
  ans=merge(L,R)
  return ans


def quicksort(L,l,r):
  if r-l<=1:
    return L
  pivot,lower,upper=L[l],l+1,l+1
  for i in range(l+1,r):
    if L[i]>pivot:
      upper+=1
    else:
      L[i],L[lower]=L[lower],L[i]
      upper,lower=upper+1,lower+1
  L[lower-1],L[l]=L[l],L[lower-1]
  lower-=1
  quicksort(L,l,lower)
  quicksort(L,lower+1,upper)
  return L