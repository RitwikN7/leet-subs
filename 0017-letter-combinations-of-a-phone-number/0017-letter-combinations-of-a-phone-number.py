class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(s: str, digits: str):
            if len(digits) == 0:
                res.append(s)
            else:
                for c in phone[digits[0]]:
                    backtrack(s + c, digits[1:])

        if digits:
            backtrack('', digits)

        return res