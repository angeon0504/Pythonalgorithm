"""
문제링크:https://leetcode.com/problems/valid-palindrome/description/
제한시간:30분
사용시간: 21분
문제 해경방법:
가장 직관적인 방법은 숫자의 모든 비트를 하나씩 확인하면서 1인지 세기
이 코드는 마지막 비트를 반복적으로 확인한 뒤, 숫자를 오른쪽으로 한 비트씩 이동(right-shift)시키는 방식으로 동작.
 이 과정을 숫자가 0이 될 때까지 반복
시간 복잡도: O(k)
공간 복잡도: O(1)
"""


def count_set_bits_simple(n: int) -> int:
    """
    각 비트를 하나씩 확인하여 1의 개수를 셉니다.
    """
    count = 0  # 1. count를 0으로 초기화
    while n > 0:  # 2. n이 0이 될 때까지 반복
        # 2-1. 마지막 비트가 1인지 확인
        if n & 1:
            count += 1  # 2-2. 1이면 count 증가

        # 2-3. 다음 비트를 확인하기 위해 오른쪽으로 시프트
        n = n >> 1

    return count  # 3. 최종 개수 반환