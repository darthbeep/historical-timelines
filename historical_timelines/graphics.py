from bokeh.plotting import figure, save
from bokeh.models import LabelSet, ColumnDataSource, CustomJSTickFormatter
from bokeh.core.properties import value


def get_source_from_event_dict(event_dict: dict) -> ColumnDataSource:
    """Convert a dictionary into a ColumnDataSource

    Args:
        event_dict (dict): The dictionary input

    Returns:
        ColumnDataSource: The converted data
    """
    return ColumnDataSource(data=event_dict)


def setup_figure(*args, **kwargs) -> figure:
    """Create plot with which to create the timeline on.

    This function is essentially a wrapper for the bokeh function figure.
    See its documentation for more information.

    Returns:
        figure: A plot on which to create a timeline
    """
    if "tools" not in kwargs:
        kwargs["tools"] = "hover,pan,wheel_zoom,box_zoom,reset,save"
    return figure(*args, **kwargs)


def get_y_range(event_dict: dict, period_list: list) -> list[str]:
    """Get the labels that populate the y range

    Args:
        event_dict (dict): The event dictionary
        period_list (list): The period list

    Returns:
        list[str]: A list of labels to populate the dictionary
    """
    y_range = []
    for i in range(len(period_list)):
        y_range.append("p" + str(i))

    for label in event_dict['label']:
        if label not in y_range:
            y_range.append(label)

    return y_range


def render_events(plot: figure, source: ColumnDataSource, x: str, y: str, size: int) -> None:
    """Render events on the plot

    Args:
        plot (figure): The plot events are rendered on
        source (ColumnDataSource): The data to be rendered
        x (str): The name of the column of source that lists the event x axis
        y (str): The name of the column of source that lists the event y axis
        size (int): The size of the events
    """
    plot.scatter(x=x, y=y, size=size, source=source)


def event_tooltips(plot: figure, tooltip_names: list[str]) -> None:
    """Give the plot hoverable tooltips for events

    Args:
        plot (figure): The plot to be modified
        tooltip_names (list[str]): The categories to be shown in the tooltip
    """
    tooltips = []
    for tool in tooltip_names:
        tooltips.append((tool, "@" + tool))
    plot.hover.tooltips = tooltips


def event_labels(
    plot: figure,
    source: ColumnDataSource,
    x: str,
    y: str,
    text: str,
    y_offset: int = 0,
    text_font_size: str = "11px",
    text_color: str = "#555555",
    text_align: str = 'center',
) -> None:
    """Give events on the plot labels

    Args:
        plot (figure): The plot events are rendered on
        source (ColumnDataSource): The data to be rendered
        x (str): The name of the column of source that lists the event x axis
        y (str): The name of the column of source that lists the event y axis
        text (str): The name of the column of source that lists the event label text
        y_offset (int, optional): The y offset of the labels. Defaults to 0.
        text_font_size (str, optional): The font size of the labels. Defaults to "11px".
        text_color (str, optional): The color of the labels. Defaults to "#555555".
        text_align (str, optional): The text alignment of the labels. Defaults to 'center'.
    """
    labels = LabelSet(
        x=x,
        y=y,
        text=text,
        y_offset=y_offset,
        text_font_size=text_font_size,
        text_color=text_color,
        text_align=text_align,
        source=source,
    )
    plot.add_layout(labels)


def render_periods(plot: figure, period_list: list, height: float = 0.3) -> None:
    """Render the periods on the plot

    Args:
        plot (figure): The plot to be rendered on
        period_list (list): The list of periods to be rendered
        height (float, optional): The height of the rendered periods. Defaults to 0.3.
    """
    for i in range(len(period_list)):
        period_group = period_list[i]
        source = get_source_from_event_dict(period_group)
        plot.hbar(right='start', left='end', y=value("p" + str(i)), height=height, color='red', source=source)


def period_labels(
    plot: figure,
    period_list: list,
    text: str,
    y_offset: int = -8,
    text_font_size: str = "11px",
    text_color: str = "#555555",
    text_align: str = 'center',
) -> None:
    """Give labels to the periods on the plot

    Args:
        plot (figure): The plot events are rendered on
        period_list (list): The list of periods to be given labels
        text (str): The name of the column of source that lists the period label text
        y_offset (int, optional): The y offset of the labels. Defaults to -8.
        text_font_size (str, optional): The font size of the labels. Defaults to "11px".
        text_color (str, optional): The text color of the labels. Defaults to "#555555".
        text_align (str, optional): The text alignment of the labels. Defaults to 'center'.
    """
    for i in range(len(period_list)):
        period_group = period_list[i]
        source = get_source_from_event_dict(period_group)
        labels = LabelSet(
            x='mid',
            y=value("p" + str(i)),
            text=text,
            y_offset=y_offset,
            text_font_size=text_font_size,
            text_color=text_color,
            text_align=text_align,
            source=source,
        )
        plot.add_layout(labels)


def format_xaxis(plot: figure, scientific: bool = False) -> figure:
    """Modifies a plot to format the x axis as dates.

    Args:
        plot (figure): The plot to be modified
        scientific (bool, optional): If true, dates use BCE/CE, if false, dates use BC/AD.
        Defaults to False.

    Returns:
        figure: The modified plot
    """
    code = ""
    if scientific:
        code = '''return tick < 0 ? Math.abs(tick) + " BCE" : tick +  " CE"'''
    else:
        code = '''return tick < 0 ? Math.abs(tick) + " BC" : tick +  " AD"'''
    plot.xaxis.formatter = CustomJSTickFormatter(code=code)
    return plot


def render_timeline(output: str, title: str, event_dict: dict, period_list: list) -> None:
    """Render a timeline as an image

    Args:
        output (str): The filename to save the timeline as
        title (str): The title of the timeline
        event_dict (dict): The event dict generated by the timeline
        period_list (list): The period list generated by the timeline
    """
    source = get_source_from_event_dict(event_dict)
    y_range = get_y_range(event_dict, period_list)
    p = setup_figure(title=title, x_axis_label="year", y_axis_label="category", height=400, width=1600, y_range=y_range)
    event_tooltips(p, tooltip_names=["title", "description"])
    render_events(p, source, x='dates', y='label', size=20)
    render_periods(p, period_list)
    period_labels(p, period_list, text="title")
    event_labels(p, source, x="dates", y="label", text="title")
    format_xaxis(p, False)
    save(p, output, title=title)


if __name__ == "__main__":
    pass
