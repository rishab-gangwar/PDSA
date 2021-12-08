# Longest Bitonic Subsequence
"""
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the length of longest bitonic subsequence of array.
Note -> bitonic subsequence begins with elements in increasing order, followed by elements in decreasing order.

Input Format

A number n
.. n more elements

Output Format

A number representing the length of longest bitonic subsequence of array.
"""
n=int(input())
ques=[]
lis,lds=[],[]
for i in range(n):
  q=int(input())
  ques.append(q)
  lis.append(None)
  lds.append(None)
lis[0]=1
lds[n-1]=1
for i in range(1,n):
  mini=0
  for j in range(i):
    if ques[j]<ques[i]:
      mini=max(mini,lis[j])
  lis[i]=mini+1
for i in range(n-2,-1,-1):
  mini=0
  for j in range(i+1,n):
    if ques[j]<=ques[i]:
      mini=max(mini,lds[j])
  lds[i]=mini+1
print(lis,lds)
ans=[]
for i in range(n):
  ans.append(lis[i]+lds[i])
print(ans)
print(max(ans)-1)