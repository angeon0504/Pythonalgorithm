"""
문제링크:https://leetcode.com/problems/climbing-stairs/description/
제한시간:30분
사용시간: 28분
문제 해경방법:
점화식: dp[n] = dp[n-1] + dp[n-2]
초기값: dp[0] = 1(아무 것도 안 함), dp[1] = 1
"""

def climbStairs(n: int) -> int:
    a, b = 1, 1  # a=dp[0], b=dp[1]
    for _ in range(n):
        a, b = b, a + b
    return a  # dp[n]