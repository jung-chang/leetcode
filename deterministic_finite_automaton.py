class AtoiStateMachine:
    def __init__(self):
        self.states = {
            "initial": 1,
            "digit": 2,
            "end": 3,
        }
        self.state = 1

        self.min_int = -(2 ** 31)
        self.max_int = 2 ** 31 - 1

        self.result = 0
        self.positive = True

    def append_result(self, arg: str):
        num = int(arg)
        if not self.positive and -1 * self.result < (self.min_int + num) / 10:
            self.result = -1 * self.min_int
            self.state = self.states["end"]
        elif self.positive and self.result > (self.max_int - num) / 10:
            self.result = self.max_int
            self.state = self.states["end"]
        else:
            self.result *= 10
            self.result += num

    def transition(self, arg: str):
        if self.state == self.states["initial"]:
            if arg == "-":
                self.positive = False
                self.state = self.states["digit"]
            elif arg == "+":
                self.positive = True
                self.state = self.states["digit"]
            elif arg.isdigit():
                self.append_result(arg)
            else:
                self.state = self.states["end"]
        elif self.state == self.states["digit"]:
            if arg.isdigit():
                self.append_result(arg)
            else:
                self.state = self.states["end"]
        else:
            pass

    def get_result(self) -> int:
        return self.result if self.positive else -1 * self.result


class Solution:
    def myAtoi(self, input: str) -> int:
        state_machine = AtoiStateMachine()
        for char in input.strip():
            state_machine.transition(char)
            if state_machine.state == state_machine.states["end"]:
                break
        return state_machine.get_result()


print(Solution().myAtoi("-91283472332"))


# class StateMachine:
#     STATE1 = 0
#     STATE2 = 1
#     def __init__(self):
#         self.state = self.STATE1

#     def mutate_result(arg: str):
#         pass

#     def transition(self, arg: str):
#         if self.state == self.STATE1:
#             if arg == "":
#                 self.mutate_result(arg)
#         elif self.state == self.STATE2:
#             if arg == "":
#                 self.mutate_result(arg)

# state_machine = StateMachine()
# for arg in input:
#     state_machine.transition(arg)
#     if state_machine.state == state_machine.STATE2:
#         break
