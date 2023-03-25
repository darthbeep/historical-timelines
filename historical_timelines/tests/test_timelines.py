from historical_timelines import *


def test_timeline_csv():
    t0 = HistoricalTimeline()
    j0 = HistoricalTimeline.json_from_csv(
        "historical_timelines/tests/timeline_egypt.csv",
        "Event",
        "Description",
        "Label",
        "Start",
        "End",
        Era.BCE,
    )

    assert (
        "{'title': 'Amenmesse', 'description': 'Reign of Amenmesse', 'label': 'Ruler', 'start': 1201, 'end': 1198, 'era': <Era.BCE: -1>}" in str(j0)
    )

    t0.populate_timeline_from_dict(j0)


def test_timeline_len():
    t0 = HistoricalTimeline()
    j0 = HistoricalTimeline.json_from_csv(
        "historical_timelines/tests/timeline_egypt.csv",
        "Event",
        "Description",
        "Label",
        "Start",
        "End",
        Era.BCE,
    )

    t0.populate_timeline_from_dict(j0)

    assert len(t0) == 33
