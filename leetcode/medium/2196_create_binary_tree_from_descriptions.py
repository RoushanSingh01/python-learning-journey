from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for p, c, is_left in descriptions:
            children.add(c)

            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

        for p, _, _ in descriptions:
            if p not in children:
                return nodes[p]

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

if __name__ == "__main__":
    descriptions = [
        [20,15,1],
        [20,17,0],
        [15,10,1]
    ]

    root = Solution().createBinaryTree(descriptions)
    print(preorder(root))