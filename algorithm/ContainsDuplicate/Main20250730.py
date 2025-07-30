"""
문제링크:https://leetcode.com/problems/contains-duplicate/description/
제한시간:30분
사용시간: 20분
문제 해결 방법:배열을 하나씩 돌면서 그 숫자가 set안에 있다면 중복된 숫자이기 때문에 True 반환하고
없으면 set 안에 추가시키고 다음 숫자를 확인
다돌았는데도 중복이 없으면 Fales 반환
"""
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

