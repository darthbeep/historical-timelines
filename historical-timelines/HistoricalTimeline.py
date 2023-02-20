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

    def populate_random_timeline(self, N = 10):
        events = []
        for _ in range(N):
            events.append(HistoricalEvent.get_random_event())
        self.add_events(events)


def testTimeline():
    r = HistoricalTimeline()
    r.populate_random_timeline()
    r.sort()
    print(r)

if __name__ == "__main__":
    testTimeline()