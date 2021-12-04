def binarysearch(lis,element):
  if lis==[]:
    return False
  mid=len(lis)//2
  if lis[mid]==element:
    return True
  elif lis[mid]>element:
    return binarysearch(lis[:mid],element)
  else:
    return binarysearch(lis[mid+1:],element)

