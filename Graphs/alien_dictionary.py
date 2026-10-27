from collections import deque

class Solution:
    def findOrder(self, words):
        # Step 1: Create graph for all unique characters
        chars = set("".join(words))
        adj = {ch: set() for ch in chars}
        indegree = {ch: 0 for ch in chars}

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Find first different character
            limit = min(len(w1), len(w2))

            for j in range(limit):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
            else:
                # Invalid prefix order, e.g. "abcd" before "ab"
                if len(w1) > len(w2):
                    return ""

        # Step 3: Start with characters having indegree 0
        queue = deque([ch for ch in chars if indegree[ch] == 0])
        order = []

        # Step 4: Perform BFS topological sort
        while queue:
            ch = queue.popleft()
            order.append(ch)

            for neighbor in adj[ch]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If a cycle exists, no valid order
        if len(order) != len(chars):
            return ""

        return "".join(order)