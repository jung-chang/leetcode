# https://leetcode.com/problems/interleaving-string/


class Solution:
    """
    TODO
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Use 2 pointers, each for s1 and s2. Increment as such.

        aab
        aac

        aabaac
        """
        if len(s3) != len(s1) + len(s2):
            return False

        i = 0
        ip = 0

        j = 0
        jp = 0

        for k in range(len(s3)):
            letter = s3[k]
            if ip > i or jp > j:
                if s1[ip] == letter and s2[jp] == letter:
                    ip += 1
                    jp += 1
                elif ip < len(s1) and s1[ip] == letter:
                    jp = j
                    i = ip
                    i += 1
                elif jp < len(s2) and s2[jp] == letter:
                    ip = i
                    j = jp
                    j += 1
            else:
                if s1[i] == letter and s2[j] == letter:
                    ip += 1
                    jp += 1
                elif i < len(s1) and s1[i] == letter:
                    i = ip
                    i += 1
                    ip = i
                elif s2[j] == letter:
                    j = jp
                    j += 1
                    jp = j
                else:
                    return False
            print(s3[k:])
            print(i, ip, s1[i:], s1[ip:])
            print(j, jp, s2[j:], s2[jp:])
            print()
        return i == len(s1) - 1 and j == len(s2) - 1


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))
