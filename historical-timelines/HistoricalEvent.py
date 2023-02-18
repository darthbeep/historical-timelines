from enum import Enum
from HistoricalDate import HistoricalDate

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

def testEvent():
    h = HistoricalDate(1, 2, 3, 2)
    i = HistoricalDate(2)
    j = HistoricalDate(3, 12, 3)

    e = HistoricalEvent("a", "b", h)
    f = HistoricalEvent("c", "d", i, j)
    print(e, f)

if __name__ == "__main__":
    testEvent()