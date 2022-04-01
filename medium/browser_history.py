# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:
    """
    You have a browser of one tab where you start on the homepage and you can
    visit another url, get back in the history number of steps or move forward
    in the history number of steps.
    """

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.cur = -1
        self.history = []

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        self.history = self.history[: self.cur + 1] + [url]
        self.cur += 1
        print(history.cur, history.history)

    def back(self, steps: int) -> str:
        """
        Move steps back in history.
        If you can only return x steps in the history and steps > x,
        you will return only x steps. Return the current url after moving back in
        history at most steps
        """
        self.cur = max(-1, self.cur - steps)
        print(history.cur, history.history)
        if self.cur == -1:
            return self.homepage
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history.
        If you can only forward x steps in the history and steps > x,
        you will forward only x steps. Return the current url after forwarding in
        history at most steps.
        """
        self.cur = min(len(self.history) - 1, self.cur + steps)
        print(history.cur, history.history)
        if self.cur == -1:
            return self.homepage
        return self.history[self.cur]


history = BrowserHistory("home")
print(history.back(100))
print(history.forward(100))

# history.visit("1")
# history.visit("2")
# history.visit("3")
# print(history.back(100))
# history.visit("4")
# print(history.forward(100))
# history.visit("4")
