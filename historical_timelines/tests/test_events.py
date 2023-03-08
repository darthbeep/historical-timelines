from historical_timelines import *


def test_assert():
    assert 1 == 1


def test_event_string():
    d0 = HistoricalDate(1, 2, 3)
    d1 = HistoricalDate(4, era=Era.BCE)
    d2 = HistoricalDate(5, era=Era.BCE)

    e0 = HistoricalEvent("a", "b", d0)
    e1 = HistoricalEvent("c", "d", d1, d2)
    assert str(e0) == "a: b\nFebruary 3, 1 CE"
    assert str(e1) == "c: d\n5 BCE - 4 BCE"


def test_event_operators():
    d0 = HistoricalDate(1, era=Era.CE)
    d1 = HistoricalDate(1, era=Era.BCE)

    e0 = HistoricalEvent("a", "b", d0)
    e1 = HistoricalEvent("c", "d", d1)

    assert e0 > e1
    assert e0 >= e1
    assert not (e0 == e1)
    assert e0 != e1
    assert e1 <= e0
    assert e1 < e0
