from HistoricalDate import Era
from HistoricalEvent import HistoricalEvent
from csv import DictReader

class HistoricalTimeline:
    events: list[HistoricalEvent]
    periods: list[HistoricalEvent]

    def __init__(self) -> None:
        """Initialization function
        """
        self.events = []
        self.periods = []

    def __str__(self) -> str:
        """To string function

        Returns:
            str: A representation of the function as a string
        """
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

    def __len__(self) -> int:
        """Length function

        Returns:
            int: The number of all events in the timeline
        """
        return len(self.events) + len(self.periods)

    def add_event(self, event: HistoricalEvent) -> None:
        """Add a singular event

        Args:
            event (HistoricalEvent): The event to be added
        """
        if event.is_event():
            self.events.append(event)
        elif event.is_period():
            self.periods.append(event)
    
    def add_events(self, events: list[HistoricalEvent]) -> None:
        """Add a list of events

        Args:
            events (list[HistoricalEvent]): A list of events to be added
        """
        for event in events:
            self.add_event(event)

    def sort(self):
        """Sorts the timeline
        """
        self.events.sort()
        self.periods.sort()

    def collision_sort(self) -> list[list[HistoricalEvent]]:
        """Generates lists of subsets of periods such that no periods overlap

        Returns:
            list[list[HistoricalEvent]]: A list of a list of non overlapping periods
        """
        pds = []
        if len(self.periods) == 0:
            return pds
        for period in self.periods:
            placed = False
            for i in range(len(pds)):
                if period.start > pds[i][-1].end:
                    pds[i].append(period)
                    placed = True
                    break
            if not placed:
                pds.append([period])

        return pds
        
    def populate_timeline_from_dict(self, timeline_dict: object):
        events = []
        for dict_event in timeline_dict:
            event = HistoricalEvent.event_from_dict(dict_event)
            events.append(event)
        self.add_events(events)
        self.sort()

    def populate_random_timeline(self, N: int = 10) -> None:
        """Populate the timeline with random events

        Args:
            N (int, optional): The number of events to populate the timeline with. Defaults to 10.
        """
        events = []
        for _ in range(N):
            events.append(HistoricalEvent.get_random_event())
        self.add_events(events)
        
    @staticmethod
    def json_from_csv(path: str, title_name: str = "title", description_name: str = "description",
                      start_name: str = "start", end_name: str = "end", csv_era: Era = Era.CE) -> list[dict]:
        dates = []
        with open(path) as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                event = {}
                event["title"] = row[title_name]
                event["description"] = row[description_name]
                event["start"] = int(row[start_name])
                if row[end_name] == "":
                    event["end"] = None
                else:
                    event["end"] = int(row[end_name])
                event["era"] = csv_era
                dates.append(event)
        return dates


def testTimeline():
    r = HistoricalTimeline()
    r.populate_random_timeline()
    r.sort()
    #print(r)
    #print(r.collision_sort())
    
    c = HistoricalTimeline()
    d = HistoricalTimeline.json_from_csv("/tmp/timeline.csv", "Event", "Description", "Start", "End", Era.BCE)
    c.populate_timeline_from_dict(d)
    print(c)
    print(c.collision_sort())

if __name__ == "__main__":
    testTimeline()