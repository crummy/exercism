from __future__ import annotations

class Clock:
    mins_on_clock = 60 * 24

    def __init__(self, hour, minute):
        self.minutes = hour * 60 + minute

    def __repr__(self):
        hours = self.minutes // 60 % 24
        mins = self.minutes % 60
        return f"{hours:02}:{mins:02}"

    def __eq__(self, other):
        return (self.minutes % self.mins_on_clock) == (other.minutes % self.mins_on_clock)

    def __add__(self, minutes: int):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes) -> Clock:
        return Clock(0, self.minutes - minutes)
