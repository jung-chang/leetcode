# https://leetcode.com/problems/path-crossing/


class Solution:
    """
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively.
    You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

    Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
    """

    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        cur = (0, 0)
        for direction in path:
            if direction == "N":
                cur = cur[0], cur[1] + 1
            elif direction == "S":
                cur = cur[0], cur[1] - 1
            elif direction == "E":
                cur = cur[0] + 1, cur[1]
            elif direction == "W":
                cur = cur[0] - 1, cur[1]

            print(visited, cur)

            if cur in visited:
                return True
            visited.add(cur)
        return False


i = "NESWW"
print(Solution().isPathCrossing(i))
