## Word Ladder 2

from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # child -> list of parents
        parents = defaultdict(list)

        queue = deque([beginWord])

        visited = {beginWord}
        found = False

        while queue and not found:

            level_visited = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word not in wordSet:
                            continue

                        # First time discovering this word
                        if new_word not in visited:
                            visited.add(new_word)
                            level_visited.add(new_word)
                            queue.append(new_word)
                            parents[new_word].append(word)

                        # Another shortest parent
                        elif new_word in level_visited:
                            parents[new_word].append(word)

                        if new_word == endWord:
                            found = True

            # Remove words only after the whole level
            wordSet -= level_visited

        if not found:
            return []

        # Build all shortest paths using DFS
        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result