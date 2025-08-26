"""
문제링크:https://leetcode.com/problems/3sum/
제한시간:30분
사용시간: 48분
문제 해경방법:
1. 정렬 (Sorting)
배열을 먼저 정렬. (O(n log n))
정렬하면 중복을 쉽게 처리할 수 있고, 투 포인터 접근이 가능

2. 첫 번째 숫자 고정

i 번째 원소를 기준으로 두 번째, 세 번째 숫자를 투 포인터로 탐색
nums[i] 가 이전 숫자와 같다면, 중복 방지를 위해 건너뛰기

3. 투 포인터 탐색

left = i+1, right = n-1 로 두 포인터를 두기
합 s = nums[i] + nums[left] + nums[right] 를 계산
s < 0 → 합을 키워야 하므로 left++
s > 0 → 합을 줄여야 하므로 right--
s == 0 → 정답! triplet을 결과에 넣고, 중복 제거 위해 left, right를 조정

4. 중복 제거
같은 값이 반복되면, 같은 triplet이 다시 나올 수 있으므로 left와 right가 이동할 때 중복된 값들을 건너뛰기


⏱시간 복잡도
정렬: O(n log n)
탐색: O(n^2) (고정된 i마다 투 포인터 탐색)
최종: O(n^2)
"""



def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # 1. 정렬
    res = []
    n = len(nums)

    for i in range(n - 2):
        # 중복 제거: 같은 값이면 스킵
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])


                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1


                left += 1
                right -= 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2], [-1,0,1]]
print(threeSum([0,1,1]))           # []
print(threeSum([0,0,0]))           # [[0,0,0]]
