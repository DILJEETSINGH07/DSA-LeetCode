from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        target = Counter(words)
        ans = []

        for offset in range(word_len):
            left = offset
            curr = defaultdict(int)
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    curr[word] += 1
                    count += 1

                    while curr[word] > target[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    curr.clear()
                    count = 0
                    left = right + word_len

        return ans