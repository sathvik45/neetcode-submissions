class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {
            c: set() for w in words for c in w
        }
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > minLen and w1[:minLen] == w2:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)

        seen = {}
        res = []
        def dfs(i):
            if i in seen:
                return seen[i]
            
            seen[i] = True

            for nei in adj[i]:
                if dfs(nei):
                    return True
            seen[i] = False
            res.append(i)
        
        for i in adj:
            print(i)
            if dfs(i):
                return ""
        return "".join(res[::-1])
