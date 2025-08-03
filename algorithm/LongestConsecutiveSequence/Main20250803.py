"""
문제링크:https://leetcode.com/problems/longest-consecutive-sequence/description/
제한시간:30분
사용시간: 41분
문제 내용:1.모든 숫자를 Set에 저장합니다.
2.각 숫자에 대해, 해당 숫자가 연속된 수열의 시작인지 확인
(num - 1)이 Set에 없다면, num이 수열의 시작임.
3.수열의 길이를 하나씩 증가시키며 연속된 숫자를 찾기
4.최대 길이를 저장해서 반환합니다.
"""

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # num - 1이 없으면 num은 시작 숫자
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest
nums1 = [100, 4, 200, 1, 3, 2]
print("Example 1 Input:", nums1)
print("Output:", longestConsecutive(nums1))

# 예제 2
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print("\nExample 2 Input:", nums2)
print("Output:", longestConsecutive(nums2))

# 예제 3
nums3 = [1, 0, 1, 2]
print("\nExample 3 Input:", nums3)
print("Output:", longestConsecutive(nums3))


