class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque(['0000'])
        steps = 0
        visited = set(deadends)
        while q:
            steps += 1
            for _ in range(len(q)):
                code = q.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        move = str((int(code[i]) + j + 10) % 10)
                        newCode = code[:i] + move + code[i+1:]
                        if newCode == target:
                            return steps
                        if newCode in visited:
                            continue
                        q.append(newCode)
                        visited.add(newCode)
        return -1



        