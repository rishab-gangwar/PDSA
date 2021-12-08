# Maximum Sum Increasing Subsequence
"""
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the sum of elements of the increasing subsequence with maximum sum for the array.

Input Format

A number n
.. n more elements

Output Format

A number representing the sum of elements of the increasing subsequence with maximum sum for the array.
Constraints

0 <= n <= 20
0 <= n1, n2, .. <= 100

Sample Input

10
10
22
9
33
21
50
41
60
80
1

Sample Output

255
"""
n=int(input())
ques=[]
dp=[]
for i in range(n):
  q=int(input())
  ques.append(q)
  dp.append(None)
dp[0]=ques[0]
ans=0
for i in range(1,n):
  mini=0
  for j in range(i):
    if(ques[j]<ques[i]):
      mini=max(mini,dp[j])
  dp[i]=mini+ques[i]
  ans=max(ans,dp[i])
print(dp,ans)
