"""
문제링크:https://leetcode.com/problems/valid-anagram/description/
제한시간:30분
사용시간: 20분
문제 내용:1두 문자열 s, t가 주어짐.
t가 s의 아나그램(anagram)이면 true, 아니면 false.
아나그램 = 문자열의 구성 문자가 같고, 순서만 다름.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    #
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    # 3. 모두 소진되었으면 아나그램
    return len(count) == 0

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))