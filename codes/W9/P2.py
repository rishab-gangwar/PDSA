#Print All Paths With Minimum Jumps

"""1. You are given a number N representing number of elements.
2. You are given N space separated numbers (ELE : elements).
3. Your task is to find & print  
    3.1) "MINIMUM JUMPS" need from 0th step to (n-1)th step.
    3.2) all configurations of "MINIMUM JUMPS".
NOTE: Checkout sample question/solution video inorder to have more insight.

Input Format

A number N (representing "NUMBER OF ELEMENTS").
ELE1 ,ELE2 ,ELE3 ,ELE4 .... ELEn (N space separated numbers represnting numbers).

Output Format

1) A number representing "MINIMUM JUMPS" need from 0th step to (n-1)th step.
2) Strings representing configurations of "MINIMUM JUMPS"."""
n=int(input())
ques=[]
dp=[]
for i in range(n):
  q=int(input())
  ques.append(q)
  dp.append(None)
dp[n-1]=0
print(dp,ques)
for i in range(n-2,-1,-1):
  mini=1000000000
  for j in range(1,ques[i]+1):
    if j+i<n and dp[i+j] !=None:
      mini=min(dp[i+j],mini)
  if mini!=1000000000:
    dp[i]=mini+1

print(dp,ques)
print(dp[0])

