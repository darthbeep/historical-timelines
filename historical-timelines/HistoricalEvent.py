from enum import Enum
from HistoricalDate import HistoricalDate
from string import ascii_lowercase, digits
from random import choices, randint

class EventType(Enum):
    Event = 1
    Period = 2

class HistoricalEvent:
    title: str
    description: str
    event_type: EventType
    start: HistoricalDate
    end: HistoricalDate

    def __init__(self, title: str, description: str, start: HistoricalDate, end: HistoricalDate = None) -> None:
        self.title = title
        self.description = description
        self.start = start
        self.end = end
        self.event_type = EventType.Period if end else EventType.Event

    def __str__(self) -> str:
        ret = "{}: {}\n".format(self.title, self.description)
        if self.event_type is EventType.Event:
            ret += "{}".format(self.start)
        elif self.event_type is EventType.Period:
            ret += "{} - {}".format(self.start, self.end)

        return ret

    def __lt__(self, other):
        return self.start < other.start
    
    def is_event(self) -> bool:
        return self.event_type == EventType.Event

    def is_period(self) -> bool:
        return self.event_type == EventType.Period

    @staticmethod
    def get_random_string(N = 7):
        # Stolen from https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
        return ''.join(choices(ascii_lowercase + digits, k=N))

    @staticmethod
    def get_random_event():
        title = HistoricalEvent.get_random_string()
        description = HistoricalEvent.get_random_string()
        start = HistoricalDate.get_random_date()
        end = HistoricalDate.get_random_date() if randint(0, 1) == 0 else None
        return HistoricalEvent(title, description, start, end)

def testEvent():
    h = HistoricalDate(1, 2, 3, -1)
    i = HistoricalDate(2, era=-1)
    j = HistoricalDate(3, 12, 3)

    e = HistoricalEvent("a", "b", h)
    f = HistoricalEvent("c", "d", i, j)
    print(e < f)

if __name__ == "__main__":
    testEvent()