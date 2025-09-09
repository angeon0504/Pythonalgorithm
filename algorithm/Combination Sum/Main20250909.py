"""
문제링크:https://leetcode.com/problems/combination-sum/description/

제한시간:30분

사용시간: 61분

문제 해경방법:
1.숫자 선택: 후보(candidates) 목록에서 숫자 하나를 고른다
2.재귀 탐색:
고른 숫자를 현재 조합에 추가하기
목표 합계(target)에서 그 숫자를 뺀 값을 새로운 목표로 설정하고, 다시 1번 과정부터 반복
3.되돌아가기 (백트랙):
만약 합계가 target을 초과하면, 더 이상 진행하지 않고 마지막에 추가한 숫자를 빼기.
합계가 정확히 target이 되면, 성공적인 조합이므로 결과 목록에 추가한 뒤 마지막 숫자를 빼기.

시간 복잡도: O(NT/M+1)
N은 후보 숫자 개수, T는 목표 합계, M은 가장 작은 후보 숫자
재귀 트리의 깊이가 최대 T/M이고 각 노드에서 N개의 후보를 탐색할 수 있으므로 시간 복잡도는 지수적(exponential). 문제의 제약 조건이 작기 때문에 이 방법으로 해결할 수 있음

공간 복잡도: O(T/M)
재귀 호출의 최대 깊이에 비례하는 공간이 필요합니다. 가장 작은 숫자로만 조합을 만들 때 재귀가 가장 깊어짐
"""

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    results = []  # 최종 결과를 저장할 리스트

    def backtrack(remaining_target, current_combination, start_index):
        # 종료 조건 1: 남은 합계가 0이면 유효한 조합을 찾은 것
        if remaining_target == 0:
            # 현재 조합의 복사본을 결과에 추가
            results.append(list(current_combination))
            return

        # 종료 조건 2: 남은 합계가 0보다 작으면 더 이상 탐색할 필요 없음
        if remaining_target < 0:
            return

        # 재귀 탐색
        for i in range(start_index, len(candidates)):
            candidate = candidates[i]

            # 1. 선택: 현재 숫자를 조합에 추가
            current_combination.append(candidate)

            # 2. 탐색: 다음 숫자를 찾기 위해 재귀 호출
            # start_index를 'i'로 넘겨주어 현재 숫자를 다시 사용할 수 있도록 함
            backtrack(remaining_target - candidate, current_combination, i)

            # 3. 선택 취소 (백트래킹): 다른 조합을 위해 마지막에 추가한 숫자 제거
            current_combination.pop()

    # 초기 호출: 남은 합계는 target, 조합은 비어있고, 0번 인덱스부터 시작
    backtrack(target, [], 0)

    return results


# 예제 사용법:
candidates1 = [2, 3, 6, 7]
target1 = 7
print(f"입력: candidates={candidates1}, target={target1}")
print(f"출력: {combinationSum(candidates1, target1)}")  # 출력: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(f"\n입력: candidates={candidates2}, target={target2}")
print(f"출력: {combinationSum(candidates2, target2)}")  # 출력: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]