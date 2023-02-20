from HistoricalDate import HistoricalDate
from HistoricalEvent import HistoricalEvent

class HistoricalTimeline:
    events: list[HistoricalEvent]
    periods: list[HistoricalEvent]

    def __init__(self) -> None:
        self.events = []
        self.periods = []

    def __str__(self) -> str:
        ret = ""
        if len(self.events) > 0:
            ret += "Events:\n"
            for event in self.events:
                ret += str(event)
                ret += "\n"
        if len(self.events) > 0 and len(self.periods) > 0:
            ret += "-----\n"
        if len(self.periods) > 0:
            ret += "Periods:\n"
            for period in self.periods:
                ret += str(period)
                ret += "\n"
        return ret

    def __len__(self):
        return len(self.events) + len(self.periods)

    def add_event(self, event: HistoricalEvent):
        if event.is_event():
            self.events.append(event)
        elif event.is_period():
            self.periods.append(event)
    
    def add_events(self, events: list[HistoricalEvent]):
        for event in events:
            self.add_event(event)

    def sort(self):
        self.events.sort()
        self.periods.sort()


def testTimeline():
    h = HistoricalDate(1, 2, 3, -1)
    i = HistoricalDate(2, era=-1)
    j = HistoricalDate(3, 12, 3)

    e = HistoricalEvent("a", "b", h)
    f = HistoricalEvent("c", "d", i, j)
    g = HistoricalEvent("e", "f", j)
    
    t = HistoricalTimeline()
    t.add_event(e)
    t.add_event(f)
    t.add_event(g)
    t.add_events([e, f])

    t.sort()
    print(len(t))
    print(t)

if __name__ == "__main__":
    testTimeline()