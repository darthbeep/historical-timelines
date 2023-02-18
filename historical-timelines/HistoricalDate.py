from enum import Enum

class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class Era(Enum):
    BCE = -1
    CE = 1

class HistoricalDate:
    year: int
    month: Month
    day: int
    era: Era

    def __init__(self, year: int, month: Month = None, day: int = None, era: Era = Era.CE) -> None:
        self.year = year
        self.month = self.assign_month(month)
        self.day = day
        self.era = Era(era)

    def __str__(self) -> str:
        if self.day and self.month:
            return "{} {}, {} {}".format(self.month.name, self.day, self.year, self.era.name)
        if self.month:
            return "{}, {} {}".format(self.month.name, self.year, self.era.name)
        return "{} {}".format(self.year, self.era.name)

    def __lt__(self, other):
        year = self.get_adjudged_year(self.year, self.era)
        other_year = self.get_adjudged_year(other.year, other.era)
        if year != other_year:
            return year < other_year
        if not self.month and not other.month:
            return False
        if self.month and not other.month:
            return False
        if not self.month and other.month:
            return True
        if self.month != other.month:
            return self.month.value < other.month.value
        if not self.day and not other.day:
            return False
        if self.day and not other.day:
            return False
        if not self.day and other.day:
            return True
        return self.day < other.day

    @staticmethod
    def assign_month(month: int) -> Month:
        if not month:
            return None
        if type(month) is int and month > 0 and month < 13:
            return Month(month)
        return None

    @staticmethod
    def get_adjudged_year(year: int, era: Era) -> int:
        if era is Era.BCE:
            return year * -1
        elif era is Era.CE:
            return year


def testDate():
    h = HistoricalDate(1, 8, 3, 1)
    i = HistoricalDate(1, day=7, era=1)
    j = HistoricalDate(1, 8, 2)
    a = sorted([h, i, j])
    print(a[0], a[1], a[2])

if __name__ == "__main__":
    testDate()