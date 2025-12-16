from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_cnt, close_cnt):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_cnt < n:
                backtrack(current + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(current + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return result


# -------- VS / VS Code Test --------
if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
