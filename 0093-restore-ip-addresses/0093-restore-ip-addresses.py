from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(index, path):
            # If we have 4 parts
            if len(path) == 4:
                if index == len(s):
                    ans.append(".".join(path))
                return

            # Try taking 1, 2, or 3 digits
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # No leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                # Must be <=255
                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(index + length, path)
                path.pop()

        backtrack(0, [])
        return ans