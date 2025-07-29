"""
문제링크:https://leetcode.com/problems/two-sum/description/
제한시간:30분
사용시간: 20분
문제 해결 방법:enumerate(nums)를 사용해 숫자와 인덱스를 함께 탐색
target - 현재 숫자가 기존에 저장된 숫자 중에 있는지 확인
있다면 [이전 인덱스, 현재 인덱스] 반환
"""
def two_sum(num, target):
    num_map = {}

    for i, num in enumerate(num):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

        print(two_sum([2, 7, 11 ,15],9))
        print(two_sum([3, 2, 4],6))
        print(two_sum([3, 3],6))

