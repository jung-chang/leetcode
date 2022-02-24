# https://leetcode.com/problems/simplify-path/


class StateMachine:
    DEFAULT = 1
    DOT = 2
    TWO_DOT = 3
    SLASH = 4

    def __init__(self):
        self.state = self.DEFAULT
        self.result = "/"

    def up_level(self) -> None:
        i = self.result[: self.result.rfind("/")].rfind("/")
        self.result = self.result[:i] + "/"

    def transition(self, symbol: str) -> None:
        print(self.state, end=" ")
        if self.state == self.DEFAULT:
            if symbol == ".":
                if self.result[-1] == "/":
                    self.state = self.DOT
                else:
                    self.result += "."
            elif symbol == "/":
                self.state = self.SLASH
            else:
                self.result += symbol
        elif self.state == self.DOT:
            if symbol == ".":
                self.state = self.TWO_DOT
            elif symbol == "/":
                self.state = self.SLASH
            else:
                self.result += "." + symbol
                self.state = self.DEFAULT
        elif self.state == self.TWO_DOT:
            if symbol == ".":
                self.result += "..."
            elif symbol == "/":
                self.up_level()
                self.state = self.SLASH
            else:
                self.result += ".." + symbol
            self.state = self.DEFAULT
        elif self.state == self.SLASH:
            if symbol == ".":
                if self.result[-1] != "/":
                    self.result += "/"
                self.state = self.DOT
            elif symbol == "/":
                pass
            else:
                if self.result[-1] != "/":
                    self.result += "/"
                self.result += symbol
                self.state = self.DEFAULT
        print(self.state, self.result, symbol)

    def get_result(self):
        print("get", self.state)
        if self.state == self.TWO_DOT:
            self.up_level()

        if len(self.result) > 1 and self.result.endswith("/"):
            return self.result[: len(self.result) - 1]
        elif not self.result:
            return "/"

        return self.result


class Solution:
    """
    Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

    In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
    For this problem, any other format of periods such as '...' are treated as file/directory names.

    The canonical path should have the following format:
        The path starts with a single slash '/'.
        Any two directories are separated by a single slash '/'.
        The path does not end with a trailing '/'.
        The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

    Return the simplified canonical path.
    """

    def simplifyPath(self, path: str) -> str:
        machine = StateMachine()
        for char in path:
            machine.transition(char)
        return machine.get_result()


# print("home/foo", Solution().simplifyPath("home/foo"))
# print("/home/foo", Solution().simplifyPath("/home/foo"))
# print("/home/../foo", Solution().simplifyPath("/home/../foo"))
# print("/home/.///foo", Solution().simplifyPath("/home/.///foo"))
# print("/home/..///foo", Solution().simplifyPath("/home/..///foo"))
# print("/a//b////c/d//././/..", Solution().simplifyPath("/a//b////c/d//././/.."))
print("/hello../world", Solution().simplifyPath("/hello../world"))
