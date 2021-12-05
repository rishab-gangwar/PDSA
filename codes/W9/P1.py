"""Largest Square Sub-matrix With All 1's


Input Format

A number N, which represents number of rows in matrix
A number M, which represents number of columns in matrix
arr1
arr2...N*M numbers

Output Format

Check the sample output and question video."""

m,n=input().split()
m=int(m)
n=int(n)
import numpy as np
ques=np.zeros((m,n))
dp=np.zeros((m,n))
for i in range(m):
    z=input().split()
    for j in range(len(z)):
        dp[i][j]=int(z[j])
        ques[i][j]=int(z[j])
ma=0
for i in range(m-2,-1,-1):
  for j in range(n-2,-1,-1):
    if i==m-1 or j==n-1:
      ma=max((dp[i][j]),ma)
    if ques[i][j]==1:
      dp[i][j]=1+min(min(dp[i+1][j],dp[i][j+1]),dp[i+1][j+1])
      ma=max(dp[i][j],ma)
print(ma)

    