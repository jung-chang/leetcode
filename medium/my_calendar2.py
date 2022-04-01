# https://leetcode.com/problems/my-calendar-ii/


class MyCalendarTwo:
    """
    You are implementing a program to use as your calendar.
    We can add a new event if adding the event will not cause a triple booking.

    A triple booking happens when three events have some non-empty intersection
    (i.e., some moment is common to all the three events.).
    """

    def __init__(self):
        self.first = []
        self.second = []

    def book(self, start: int, end: int) -> bool:
        for fstart, fend in self.second:
            if start < fend and end > fstart:
                return False
        for fstart, fend in self.first:
            if start < fend and end > fstart:
                self.second.append((max(fstart, start), min(fend, end)))
        self.first.append((start, end))
        return True
