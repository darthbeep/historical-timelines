# historical-timelines
Python package for creating timelines of historical events.

[![Build Status](https://github.com/darthbeep/historical-timelines/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/darthbeep/historical-timelines/actions)
[![codecov](https://codecov.io/gh/darthbeep/historical-timelines/branch/main/graph/badge.svg)](https://codecov.io/gh/darthbeep/historical-timelines)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/darthbeep/historical-timelines)](https://github.com/darthbeep/historical-timelines/issues)
[![PyPI](https://img.shields.io/pypi/v/historical_timelines)](https://pypi.org/project/historical-timelines/)
 
## Overview

historical-timelines is a python package for creating nice looking timelines, specifically with historical data in mind. historical-timelines uses [bokeh](https://bokeh.org/) to create images.

## Install

Install with `pip install historical_timelines`

## Quick start

First, you'll need to import the `HistoricalTimeline` object.

```python
from historical_timelines import HistoricalTimeline
```

Then, you need to populate it. Here's how to populate and display a random timeline:

```python
from historical_timelines import HistoricalTimeline

timeline = HistoricalTimeline("Random Timeline")
timeline.populate_random_timeline()
timeline.render_timeline("timeline.html")
```

This will produce something that looks like this:

![Sample timeline](doc/_static/random_timeline.png)

If you have a csv that you want to convert to a timeline, you can do that too. Suppose you have a csv with the path `timeline.csv`, and five columns entitled `Name`, `Description`, `Label`, `Start`, and `End`. It would be imported like this.

```python
from historical_timelines import HistoricalTimeline

timeline = HistoricalTimeline("Timeline from my csv")
timeline_json = HistoricalTimeline.json_from_csv(
    "timeline.csv",
    "Name",
    "Description",
    "Label",
    "Start",
    "End",
)

timeline.populate_timeline_from_dict(timeline_json)
timeline.render_timeline("timeline.html")
```