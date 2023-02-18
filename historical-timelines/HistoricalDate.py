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
    BCE = 1
    CE = 2

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

    @staticmethod
    def assign_month(month):
        if not month:
            return None
        if type(month) is int and month > 0 and month < 13:
            return Month(month)
        return None

def testDate():
    h = HistoricalDate(1, 2, 3, 2)
    i = HistoricalDate(2)
    j = HistoricalDate(3, 12, 3)
    print(h, i, j)

if __name__ == "__main__":
    testDate()