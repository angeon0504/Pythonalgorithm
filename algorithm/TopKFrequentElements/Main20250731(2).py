"""
문제링크:https://leetcode.com/problems/top-k-frequent-elements/description/
제한시간:30분
사용시간: 30분
문제 내용: nums에 있는  숫자 중에 가장 많이 등장한 k개 숫자를 반환하기
조건 시간복잡도가O(n long n)보다 좋아야 한다.O(n) or O(n long k)
문제 해결 방법:숫자의 등장 빈도는 최대 nums.length (n)만큼 나올 수 있음
따라서 **빈도 수를 인덱스로 가지는 "버킷 배열"**을 만들어서 각 숫자를 해당 인덱스에 넣기
그리고 빈도가 높은 버킷부터 역순으로 탐색하며 k개를 모으기
"""
import heapq
from collections import Counter


def topKFrequent(nums, k):
    count = Counter(nums)

    buckt = [[]for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckt[freq].append(num)

    result = []
    for freq in range(len(buckt) - 1, 0, -1):
        for num in buckt[freq]:
            result.append(num)
            if len(result) == k:
                return result


print(topKFrequent([1,1,1,2,2,2,3],2))
print(topKFrequent([1],1))

