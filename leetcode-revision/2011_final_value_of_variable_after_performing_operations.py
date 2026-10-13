class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X = 0

        for i in operations:
            if "+" in i:
                X += 1
            else:
                X -= 1

        return X