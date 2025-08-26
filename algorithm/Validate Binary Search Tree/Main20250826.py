"""
문제링크:https://leetcode.com/problems/validate-binary-search-tree/description/
제한시간:30분
사용시간: 51분
문제 해경방법:
문제 핵심
모든 왼쪽 서브트리의 값은 부모 노드보다 작아야 함.
모든 오른쪽 서브트리의 값은 부모 노드보다 커야 함.
이 조건이 모든 노드에 대해 만족해야 함.

재귀 방식 (DFS + 범위 확인)
각 노드를 순회하면서 "이 노드의 값이 유효한 범위(min < val < max) 안에 있는가?"를 확인하기
왼쪽 자식은 max를 현재 노드 값으로 업데이트,
오른쪽 자식은 min을 현재 노드 값으로 업데이트.
👉 BST의 정의를 그대로 코드로 옮길 수 있는 방식.


시간 복잡도: O(n) (모든 노드를 한 번씩 방문)
공간 복잡도: O(h) (재귀 스택, h는 트리 높이 → 최악 O(n))
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            # 현재 노드 값이 유효 범위 밖이면 False
            if not (low < node.val < high):
                return False
            # 왼쪽/오른쪽 서브트리도 검증
            return (helper(node.left, low, node.val) and
                    helper(node.right, node.val, high))

        return helper(root)
