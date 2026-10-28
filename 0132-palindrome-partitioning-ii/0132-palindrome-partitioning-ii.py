
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        palindrome = [[False] * n for _ in range(n)]

        cuts = [i for i in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (
                    end - start <= 2 or palindrome[start + 1][end - 1]
                ):
                    palindrome[start][end] = True

                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(
                            cuts[end], cuts[start - 1] + 1
                        )

        return cuts[n - 1]
