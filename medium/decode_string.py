# https://leetcode.com/problems/decode-string/


class Solution:
    """
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
    Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
    For example, there will not be input like 3a or 2[4].
    """

    def decodeString(self, s: str) -> str:
        """
        3[a2[c]] -> 3[acc]
        """
        stack = []
        for symbol in s:
            if symbol == "[":
                stack.append(symbol)
            elif symbol == "]":
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()  # pops [
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                stack.append(int(num_str) * substring)
            else:
                stack.append(symbol)
        return "".join(stack)


print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("100[leetcode]"))
