"""
Number of paths With Minimum Cost

1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
4. You are standing in top-left cell and are required to move to bottom-right cell.
5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
7. You are required to traverse through the matrix and print the cost of the path which is least costly.
8. Also, you have to print all the paths with minimum cost.

Input Format

A number n
A number m
e11
e12..
e21
e22..
.. n * m number of elements
"""
m=int(input())
n=int(input())
import numpy as np
ques=np.zeros((m,n))
dp=np.zeros((m,n))
for i in range(m):
    z=input().split()
    for j in range(len(z)):
        dp[i][j]=0
        ques[i][j]=int(z[j])
print(dp,ques)
dp[m-1][n-1]=ques[m-1][n-1]
for i in range(n-2,-1,-1):
  dp[i][m-1]+=dp[i+1][m-1]+ques[i][m-1]
for j in range(m-2,-1,-1):
  dp[n-1][j]+=dp[n-1][j+1]+ques[n-1][j]
for i in range(m-2,-1,-1):
  for j in range(n-2,-1,-1):
    dp[i][j]=ques[i][j]+min(dp[i+1][j],dp[i][j+1])
print(dp[0][0])
print(dp,ques)