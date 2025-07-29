"""
문제링크:https:https://school.programmers.co.kr/learn/courses/30/lessons/181932?language=python3
제한시간:30분
사용시간: 20분
문제 해결 방법:,처음에 mode = 0으로 시작
글자가 '1'이면 mode를 전환 시키고 글자가 1이 아니면 0은 짝수 1은 홀수로 결과를 만들기
결과 문자열이 비어 있으면 EMPTY로 반환하기
"""
def solution(code):
    mode = 0
    ret = []

    for idx, ch in enumerate(code):
        if ch == "1":
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(ch)
            elif mode == 1 and idx % 2 == 1:
                ret.append(ch)

    return ''.join(ret) if ret else "EMPTY"

    print(solution("abc1abc1abc"))