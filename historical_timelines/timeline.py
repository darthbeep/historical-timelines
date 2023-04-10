from .date import Era
from .event import HistoricalEvent
from .graphics import render_timeline
from csv import DictReader


class HistoricalTimeline:
    title: str
    events: list[HistoricalEvent]
    periods: list[HistoricalEvent]

    def __init__(self, title: str = "") -> None:
        """Initialization function"""
        self.title = title
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
        """Sorts the timeline"""
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

    def populate_timeline_from_dict(self, timeline_dict: list, sort: bool = True) -> None:
        """Populate a timeline from from an array of timeline compatible dictionaries

        Args:
            timeline_dict (list): An array of timeline compatible objects
            sort (bool, optional): Whether or not to sort the timeline after populating. Defaults to True.
        """
        events = []
        for dict_event in timeline_dict:
            event = HistoricalEvent.event_from_dict(dict_event)
            events.append(event)
        self.add_events(events)

        if sort:
            self.sort()

    def populate_random_timeline(self, N: int = 10, sort: bool = True) -> None:
        """Populate the timeline with random events

        Args:
            N (int, optional): The number of events to populate the timeline with. Defaults to 10.
            sort (bool, optional): Whether or not to sort the timeline after populating it. Defaults to True.
        """
        events = []
        for _ in range(N):
            events.append(HistoricalEvent.get_random_event())
        self.add_events(events)

        if sort:
            self.sort()

    def create_event_dict(self) -> dict[str, list]:
        """Create a dictionary that describes events to help with graphics

        Returns:
            dict[str, list]: An event dict for the graphics generator
        """
        dates = []
        titles = []
        descriptions = []
        labels = []

        for event in self.events:
            dates.append(event.get_adjusted_year())
            titles.append(event.get_title_with_newlines())
            descriptions.append(event.description)
            labels.append(event.get_label_or_default())

        event_dict = {"dates": dates, "title": titles, "description": descriptions, "label": labels}

        return event_dict

    def create_period_list(self) -> list[dict]:
        """Create a list of periods that can be turned into a timeline image

        Returns:
            list[dict]: A list of dictionaries that can be turned into a timeline image
        """
        period_list = []
        period_groups = self.collision_sort()
        for period_group in period_groups:
            starts = []
            ends = []
            mids = []
            titles = []
            descriptions = []
            labels = []

            for event in period_group:
                start, end = event.get_adjusted_year()
                starts.append(start)
                ends.append(end)
                mids.append((start + end) / 2)
                titles.append(event.get_title_with_newlines())
                descriptions.append(event.description)
                labels.append(event.label)

            event_dict = {
                "start": starts,
                "end": ends,
                "mid": mids,
                "title": titles,
                "description": descriptions,
                "label": labels,
            }

            period_list.append(event_dict)

        return period_list

    def render_timeline(self, output: str) -> None:
        """Render the timeline as an image

        Args:
            output (str): The output filename
        """
        event_dict = self.create_event_dict()
        period_list = self.create_period_list()
        render_timeline(output, self.title, event_dict, period_list)

    @staticmethod
    def json_from_csv(
        path: str,
        title_name: str = "title",
        description_name: str = "description",
        label_name: str = "label",
        start_name: str = "start",
        end_name: str = "end",
        csv_era: Era = Era.CE,
    ) -> list[dict]:
        """Create a json from a csv that can be used to populate a timeline

        This is the function that allows you to take a csv and turn it into a timeline object.
        The output can be used as an input for `populate_timeline_from_dict`.

        Args:
            path (str): The path to the csv
            title_name (str, optional): THe name of the title column. Defaults to "title".
            description_name (str, optional): The name of the description column. Defaults to "description".
            label_name (str, optional): The name of the label column. Defaults to "label".
            start_name (str, optional): The name of the start date column. Defaults to "start".
            end_name (str, optional): The name of the end date column. Defaults to "end".
            csv_era (Era, optional): Which era the timeline is in (CE or BCE). Defaults to Era.CE.

        Returns:
            list[dict]: A json that can be used to populate a timeline
        """
        dates = []
        with open(path) as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                event = {}
                event["title"] = row[title_name]
                event["description"] = row[description_name]
                event["label"] = row[label_name]
                event["start"] = int(row[start_name])
                if row[end_name] == "":
                    event["end"] = None
                else:
                    event["end"] = int(row[end_name])
                event["era"] = csv_era
                dates.append(event)
        return dates


if __name__ == "__main__":
    pass
