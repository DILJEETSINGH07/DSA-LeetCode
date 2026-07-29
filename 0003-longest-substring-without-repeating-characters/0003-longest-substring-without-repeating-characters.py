class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len