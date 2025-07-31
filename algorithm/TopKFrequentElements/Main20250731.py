"""
문제링크:https://leetcode.com/problems/top-k-frequent-elements/description/
제한시간:30분
사용시간: 30분
문제 내용: nums에 있는  숫자 중에 가장 많이 등장한 k개 숫자를 반환하기
조건 시간복잡도가O(n long n)보다 좋아야 한다.O(n) or O(n long k)
문제 해결 방법:1.빈도 수 계산: conlletions.Counter를 사용하여 각 숫자의 등상횟수를 센다.
2.최댓값 기준  우선순위 큐 사용:heapq.nlargest()를 사용해 가장 빈도 높은 k개 요소를 빠르게 가져온다.
내부적으로heapq.nlargest는 O(n long k)로 조건보다 빠름
"""
import heapq
from collections import Counter
from itertools import count


def topKFrequent(nums, k):
    count = Counter(nums)
    return  heapq.nlargest(k, count.keys(), key=count.get)

print(topKFrequent([1,1,1,2,2,2,3],2))
print(topKFrequent([1],1))

