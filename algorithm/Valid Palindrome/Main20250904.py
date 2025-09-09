"""
문제링크:https://leetcode.com/problems/valid-palindrome/description/
제한시간:30분
사용시간: 30분
문제 해경방법:
포인터 초기화: left 포인터는 문자열의 시작(인덱스 0)에, right 포인터는 문자열의 끝(s.length - 1)에 설정
반복 및 비교: left 포인터가 right 포인터보다 왼쪽에 있는 동안 아래 과정을 반복
유효한 문자 찾기 (왼쪽): left 포인터가 영문자나 숫자를 가리킬 때까지 오른쪽으로 이동하기
유효한 문자 찾기 (오른쪽): right 포인터가 영문자나 숫자를 가리킬 때까지 왼쪽으로 이동하기
대소문자 무시하고 비교: left와 right 포인터가 가리키는 문자를 모두 소문자로 변경하여 비교하기
만약 두 문자가 다르다면, 이 문자열은 회문이 아니므로 즉시 false를 반환허기
포인터 이동: 두 문자가 같다면, left 포인터를 오른쪽으로 한 칸, right 포인터를 왼쪽으로 한 칸 이동하여 다음 문자를 비교 준비
결과 반환: 반복문이 끝날 때까지 문자가 모두 일치했다면, 이 문자열은 회문이므로 true를 반환 빈 문자열이나 영문자/숫자가 없는 문자열도 이 과정을 통해 올바르게 true로 처리


시간 복잡도: O(n) (모든 노드를 한 번씩 방문)
공간 복잡도: O(h) (재귀 스택, h는 트리 높이 → 최악 O(n))
"""


def isPalindrome(s: str) -> bool:

    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1


        while left < right and not s[right].isalnum():
            right -= 1


        if s[left].lower() != s[right].lower():
            return False


        left += 1
        right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))  # 출력: True
print(isPalindrome("race a car"))  # 출력: False
print(isPalindrome(" "))  # 출력: True