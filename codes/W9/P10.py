#Min Squares
"""
1. You are given a number N.
2. You have to find the minimum number of squares that sum to N.
3. You can always represent a number as a sum of squares of other numbers.
   For eg -> In worst case N can be represented as (1*1) + (1*1) + (1*1)..... N times.

Input Format

An integer N
"""
n=int(input())
dp=[]
dp.append(0)
dp.append(1)
for i in range(2,n+1):
    dp.append(0)
for i in range(2,n+1):
    mini=1000
    for j in range(1,int(i**.5)+1):
        if i-(j**2)>=0:
            mini=min(dp[i-(j**2)],mini)
    dp[i]=mini+1
print(dp[n])


"""
Solution one: DP

dp[i] represents how many squares number i needs at least
transmisson is dp[i] = min(dp[i],dp[i-j*j]+1)

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i ** 0.5) + 1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]

Solution Two: BFS
If we use BFS directly, (I mean in my method without have_been_put array), the memory limit will exceeds. This is becasue some values we have already visited and if it has been visited before, it must have fewer steps to reach there.

Here is my solution:

    Create a queue to record the current num and have many steps have been already taken
    While the queue is not empty, pop the value and put all the possible values = num- j*j (j is square samller than num)
    If the current num is equal to 0, we got the correct answer! Otherwise keep looking.

from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        """:type n: int
        :rtype: int"""
        """
        q=deque([[n,0]])
        have_been_put = [0 for i in range(n+1)]
        while q:
            num,res = q.popleft()
            if num==0:
                break
            for j in range(1,int(num**0.5)+1):
                if(have_been_put[num-j*j] !=1):
                    q.append([num-j*j,res+1])
                have_been_put[num-j*j] = 1
        return res
        

"""
