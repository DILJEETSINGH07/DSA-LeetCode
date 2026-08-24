class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, current_combination: list[str]):
            # Base case: reached the end of the input digits
            if index == len(digits):
                result.append("".join(current_combination))
                return

            # Explore all possible letters for the current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  # Backtrack step

        backtrack(0, [])
        return result