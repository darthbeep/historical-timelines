from bokeh.plotting import figure, save
from bokeh.models import LabelSet, ColumnDataSource, CustomJSTickFormatter
from bokeh.core.properties import value


def get_source_from_event_dict(event_dict):
    return ColumnDataSource(data=event_dict)


def setup_figure(*args, **kwargs):
    if "tools" not in kwargs:
        kwargs["tools"] = "hover,pan,wheel_zoom,box_zoom,reset,save"
    return figure(*args, **kwargs)


def get_y_range(event_dict, period_list):
    y_range = []
    for i in range(len(period_list)):
        y_range.append("p" + str(i))

    for label in event_dict['label']:
        if label not in y_range:
            y_range.append(label)

    return y_range


def render_events(plot, source, x, y, size):
    plot.scatter(x=x, y=y, size=size, source=source)


def event_tooltips(plot, tooltip_names):
    tooltips = []
    for tool in tooltip_names:
        tooltips.append((tool, "@" + tool))
    plot.hover.tooltips = tooltips


def event_labels(
    plot, source, x, y, text, y_offset=0, text_font_size="11px", text_color="#555555", text_align='center'
):
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


def render_periods(plot, period_list, height=0.3):
    for i in range(len(period_list)):
        period_group = period_list[i]
        source = get_source_from_event_dict(period_group)
        plot.hbar(right='start', left='end', y=value("p" + str(i)), height=height, color='red', source=source)


def period_labels(
    plot, period_list, text, y_offset=-8, text_font_size="11px", text_color="#555555", text_align='center'
):
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


def format_xaxis(plot, scientific=False):
    code = ""
    if scientific:
        code = '''return tick < 0 ? Math.abs(tick) + " BCE" : tick +  " CE"'''
    else:
        code = '''return tick < 0 ? Math.abs(tick) + " BC" : tick +  " AD"'''
    plot.xaxis.formatter = CustomJSTickFormatter(code=code)


def render_timeline(output, title, event_dict, period_list):
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
