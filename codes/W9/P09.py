#Russian Doll Envelopes
"""
1. You are given a number n, representing the number of envelopes.
2. You are given n pair of numbers, representing the width and height of each envelope.
3. You are required to print the count of maximum number of envelopes that can be nested inside each other.
Note -> Rotation is not allowed.

Input Format

A number n
.. n pair of number each on a separate line (and pair separated by space)

Output Format

A number representing the count of maximum number of envelopes that can be nested inside each other.
"""
n=int(input())
ques=[]
dp=[]
for i in range(n):
  q=(input().split())
  q1=int(q[0])
  q2=int(q[1])
  ques.append((q1,q2))
  dp.append(0)
ques.sort()
omax=0

for i in range(1,n):
  mini=0
  for j in range(i):
    if ques[j][1]<ques[i][1]:
      mini=max(mini,dp[j])
  dp[i]=mini+1
  omax=max(omax,dp[i])
print(omax,dp)