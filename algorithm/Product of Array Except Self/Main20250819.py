"""
문제링크:https://leetcode.com/problems/product-of-array-except-self/description/
제한시간:30분
사용시간: 48분
문제 해경방법:
answer[i] = nums 배열에서 i번째 원소를 제외한 모든 원소들의 곱
왼쪽 곱(prefix) 과 오른쪽 곱(suffix) 을 따로 계산하기


왼쪽 곱 배열:
left[i] = nums[0] * nums[1] * ... * nums[i-1]
→ i번째 원소의 왼쪽까지의 곱
오른쪽 곱 배열:
right[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
→ i번째 원소의 오른쪽부터 끝까지의 곱
최종 결과:
answer[i] = left[i] * right[i]
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    # Step 1: 왼쪽 곱 계산
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    # Step 2: 오른쪽 곱 계산 (answer에 곱해줌)
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))