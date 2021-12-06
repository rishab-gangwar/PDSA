"""
Longest Increasing Subsequence
medium
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the length of longest increasing subsequence of array.

Input Format

A number n
.. n more elements

Output Format

A number representing the length of longest increasing subsequence of array."""


n=int(input())
ques=[]
dp=[]
for i in range(n):
  q=int(input())
  ques.append(q)
  dp.append(None)
dp[0]=1
for i in range(1,n):
  maxi=0
  for j in range(i):
    if(ques[i]>ques[j]):
      maxi=max(maxi,dp[j])
  dp[i]=maxi+1
print(dp)