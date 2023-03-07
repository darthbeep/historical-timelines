from historical_timelines import *

def test_assert():
    assert 1 == 1
    
def test_date_string():
    d0 = HistoricalDate(1, 2, 3)
    d1 = HistoricalDate(4, era= Era.BCE)
    assert str(d0) == "February 3, 1 CE"
    assert str(d1) == "4 BCE"
    
def test_date_operators():
    d0 = HistoricalDate(1, era=Era.CE)
    d1 = HistoricalDate(1, era=Era.BCE)
    d2 = HistoricalDate(1, 2)
    d3 = HistoricalDate(1, 3)
    d4 = HistoricalDate(1, 2, 3)
    d5 = HistoricalDate(1, 2, 4)
    
    assert d0 > d1
    assert d0 >= d1
    assert not(d0 == d1)
    assert d0 != d1
    assert d1 <= d0
    assert d1 < d0
    assert d2 < d3
    assert d4 < d5