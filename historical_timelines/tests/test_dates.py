from historical_timelines import *


def test_assert():
    assert 1 == 1


def test_date_string():
    d0 = HistoricalDate(1, 2, 3)
    d1 = HistoricalDate(1, 2)
    d2 = HistoricalDate(4, era=Era.BCE)
    assert str(d0) == "February 3, 1 CE"
    assert str(d1) == "February, 1 CE"
    assert str(d2) == "4 BCE"


def test_date_operators():
    d0 = HistoricalDate(1, era=Era.CE)
    d1 = HistoricalDate(1, era=Era.BCE)
    d2 = HistoricalDate(1, 2)
    d3 = HistoricalDate(1, 3)
    d4 = HistoricalDate(1, 2, 3)
    d5 = HistoricalDate(1, 2, 4)

    assert d0 > d1
    assert d0 >= d1
    assert not (d0 == d1)
    assert d0 != d1
    assert d1 <= d0
    assert d1 < d0
    assert d2 < d3
    assert d4 < d5
    assert d0 > d1
    assert d3 > d2
    assert d5 > d4
    assert d0 != d1
    assert d3 != d2
    assert d5 != d4
    
def test_assign_month():
    m0 = HistoricalDate.assign_month(False)
    m1 = HistoricalDate.assign_month(3)
    m2 = HistoricalDate.assign_month(13)
    
    assert m0 == None
    assert m1 == Month.March
    assert m2 == None