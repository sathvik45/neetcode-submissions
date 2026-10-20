"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash = {}
        seen = set()
        start = node
        if not node:
            return
        def dfs(node):
            hash[node] = Node(node.val)
            seen.add(node)
            for nei in node.neighbors:
                if nei not in seen:
                    dfs(nei)
        dfs(node)
        for node, new_node in hash.items():
            for nei in node.neighbors:
                new_node.neighbors.append(hash[nei])
        return hash[start]
            
        print(hash)

        