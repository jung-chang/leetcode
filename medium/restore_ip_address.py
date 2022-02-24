# https://leetcode.com/problems/restore-ip-addresses/

from typing import List


class Solution:
    """
    A valid IP address consists of exactly four integers separated by single dots.
    Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.

    You are not allowed to reorder or remove any digits in s.
    You may return the valid IP addresses in any order.
    """

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        123412345 -> 123.41.23.45 and others
        """

        result = []

        def helper(s: str, ip: str):
            nonlocal result
            if not s and ip.count(".") == 4:
                result.append(ip[1:])

            for j in range(1, len(s) + 1):
                num = s[:j]
                if len(num) > 1 and num[0] == "0":
                    continue
                if 0 <= int(s[:j]) <= 255:
                    helper(s[j:], ip + "." + s[:j])

        helper(s, "")
        return result


print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("0000"))
print(Solution().restoreIpAddresses("101023"))
