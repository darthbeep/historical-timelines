from historical_timelines import *


def test_get_y_range():
    fake_labels = {'label': ['a', 'a', 'b', 'a', 'c', 'd', 'c']}
    fake_periods = [[], []]

    y = get_y_range(fake_labels, fake_periods)

    assert y == ['p0', 'p1', 'a', 'b', 'c', 'd']
