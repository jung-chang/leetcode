# https://leetcode.com/problems/min-stack/


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    """

    def __init__(self):
        self.stack = {}
        self.top_index = -1
        self.min_index = -1

    def push(self, val: int) -> None:
        self.top_index += 1
        self.stack[self.top_index] = val
        if self.min_index < 0 or val < self.stack[self.min_index]:
            self.min_index = self.top_index

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop(self.top_index)
        if self.min_index == self.top_index:
            self.min_index = self._findMinIndex()
        self.top_index -= 1

    def top(self) -> int:
        return self.stack.get(self.top_index)

    def getMin(self) -> int:
        return self.stack.get(self.min_index)

    def _findMinIndex(self):
        if not self.stack:
            return -1
        kv = sorted([(k, v) for k, v in self.stack.items()], key=lambda x: x[1])
        return kv[0][0]


stack = MinStack()

stack.push(0)
stack.push(-1)
print(stack.top(), stack.getMin(), stack.top_index, stack.min_index)

stack.pop()
print(stack.top(), stack.getMin(), stack.top_index, stack.min_index)

stack.push(-2)
stack.push(-3)
print(stack.top(), stack.getMin(), stack.stack, stack.top_index, stack.min_index)

stack.pop()
print(stack.top(), stack.getMin(), stack.stack, stack.top_index, stack.min_index)
