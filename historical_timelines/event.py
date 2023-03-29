from enum import Enum
from string import ascii_lowercase, digits
from random import choices, randint
from .date import HistoricalDate


class EventType(Enum):
    Event = 1
    Period = 2


class HistoricalEvent:
    title: str
    description: str
    label: str
    event_type: EventType
    start: HistoricalDate
    end: HistoricalDate

    def __init__(
        self,
        title: str,
        description: str,
        start: HistoricalDate,
        end: HistoricalDate = None,
        label: str = None,
    ) -> None:
        self.title = title
        self.description = description
        self.start = start
        self.end = end
        self.label = label
        if end and end < start:
            self.start = end
            self.end = start
        self.event_type = EventType.Period if end else EventType.Event

    def __str__(self) -> str:
        ret = "{}: {}\n".format(self.title, self.description)
        if self.event_type is EventType.Event:
            ret += "{}".format(self.start)
        elif self.event_type is EventType.Period:
            ret += "{} - {}".format(self.start, self.end)

        return ret

    # TODO: Make this a proper repr
    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: object) -> bool:
        return self.start < other.start

    def __le__(self, other: object) -> bool:
        return self.start <= other.start

    def __gt__(self, other: object) -> bool:
        return self.start > other.start

    def __ge__(self, other: object) -> bool:
        return self.start >= other.start

    def __eq__(self, other: object) -> bool:
        return self.start == other.start

    def __ne__(self, other: object) -> bool:
        return self.start != other.start

    def is_event(self) -> bool:
        """
        If an event is an event

        Checks an events event type to see if it is an event, as in a single point in time.
        """
        return self.event_type == EventType.Event

    def is_period(self) -> bool:
        """
        If an event is a period

        Checks an events event type to see if it is a period, as in a time period between two dates.
        """
        return self.event_type == EventType.Period

    def get_title_with_newlines(self, max_line_width: int = 10) -> str:
        """Get the event's title with newlines placed

        Newlines are inserted in the first word break after the max_line_width variable.
        Good for making sure timeline labels aren't cramped.

        Args:
            max_line_width (int, optional):
            The maximum length a line is allowed to be before a newline is inserted after the next word.
            Defaults to 10.

        Returns:
            str: The event's title, with newlines inserted.
        """
        title_words = self.title.split(" ")
        char_counter = 0
        stop_point = max_line_width
        prev_stop = 0
        ret_title = ""

        for word in title_words:
            next_break = char_counter + len(word)
            if next_break > stop_point:
                if char_counter == prev_stop:
                    ret_title += word
                    ret_title += "\n"
                    stop_point += max_line_width
                    char_counter = stop_point
                    prev_stop = char_counter
                else:
                    ret_title += "\n"
                    ret_title += word
                    prev_stop = stop_point
                    char_counter = stop_point + len(word)
                    stop_point += max_line_width
            else:
                if char_counter != prev_stop:
                    ret_title += " "
                ret_title += word
                char_counter = next_break + 1

        return ret_title

    def get_label_or_default(self, default='default'):
        if self.label:
            return self.label
        return default

    def get_adjusted_year(self):
        if self.event_type is EventType.Event:
            return self.start.get_adjudged_year()
        return [self.start.get_adjudged_year(), self.end.get_adjudged_year()]

    @staticmethod
    def event_from_dict(event_dict: object) -> "HistoricalEvent":
        start = HistoricalDate(event_dict["start"], era=event_dict["era"])
        label = None
        end = None
        if event_dict["label"]:
            label = event_dict["label"]
        if event_dict["end"]:
            end = HistoricalDate(event_dict["end"], era=event_dict["era"])
        return HistoricalEvent(event_dict["title"], event_dict["description"], start, end, label)

    @staticmethod
    def get_random_string(N: int = 7) -> str:
        """Generate a random string

        Args:
            N (int, optional): The length of the string. Defaults to 7.

        Returns:
            str: The random string
        """
        # Stolen from https://www.geeksforgeeks.org/python-generate-random-string-of-given-length/
        return "".join(choices(ascii_lowercase + digits, k=N))

    @staticmethod
    def get_random_event() -> "HistoricalEvent":
        """Generate a random event

        Returns:
            HistoricalEvent: A random event
        """
        title = HistoricalEvent.get_random_string()
        description = HistoricalEvent.get_random_string()
        start = HistoricalDate.get_random_date()
        end = HistoricalDate.get_random_date() if randint(0, 1) == 0 else None
        return HistoricalEvent(title, description, start, end)


if __name__ == "__main__":
    pass
