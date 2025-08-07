"""
문제링크:https://leetcode.com/problems/house-robber/description/
제한시간:30분
사용시간: 53분
문제 내용: 도둑들이 집을 털려고 한
인접한 집은 동시에 털 수 없음
각집마다 훔칠 수 있는 집이 정해져 있음

문제 해결방법: 선택은 두가지다
1. 이번집을 털기:그전 집을 못텀  nums[i] + dp [i-2]
2. 이번집을  안털기: 다음집을 털 수 있음   dp[i=1]

"""

def  rob(nums : list[int]) -> int:
    n = len(nums)

    if n ==0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in  range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    return dp[-1]

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))


