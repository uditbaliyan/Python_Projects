class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     answer = ""
    #     size = len(s)
    #     for i in range(0,size):
    #         for j in range(i,size):
    #             temp = s[i:j+1]
    #             if temp == temp[::-1]:
    #                 if len(answer)<len(temp):
    #                     answer = temp
    #     return answer

    def longestPalindrome(self, s: str, *args):
        """Docstring"""

        def find_palindrome(s: str, center: int, *args):
            """Docstring"""
            size = len(s)
            start, end = center, center
            start_1, end_1 = 0, 0
            while (0 <= start) and (end < size):
                if s[start] == s[end]:
                    start -= 1
                    end += 1
                else:
                    break
            start += 1
            end -= 1
            if (0 < start) and (end < size):
                end_1 = center
                start_1 = center - 1
                while (0 <= start_1) and (end_1 < size):
                    if s[start_1] == s[end_1]:
                        start_1 -= 1
                        end_1 += 1
                    else:
                        break
                start_1 += 1
                end_1 -= 1
            if abs(start - end) < abs(start_1 - end_1):
                print(s[start_1 : end_1 + 1])
                return s[start_1 : end_1 + 1]
            print(s[start : end + 1])

            return s[start : end + 1]

        answer = ""
        start = 0
        size = len(s)
        if size == 1:
            return s
        while start < size:
            temp = find_palindrome(s, start)
            if len(answer) < len(temp):
                answer = temp
            start += 1
        return answer
