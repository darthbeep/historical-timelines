pdates = [[-1279, -1213], [1225, 1175], [1213, 1203], [1203, 1197], [1201, 1198], [1197, 1191], [1191, 1189], [1189, 1186], [1186, 1155], [1155, 1149], [1149, 1145], [1145, 1137], [1136, 1129], [1130, 1129], [1129, 1111], [1111, 1107], [1107, 1077]]
pdatesn = [[-1279, -1213], [-1225, -1175], [-1213, -1203], [-1203, -1197], [-1201, -1198], [-1197, -1191], [-1191, -1189], [-1189, -1186], [-1186, -1155], [-1155, -1149], [-1149, -1145], [-1145, -1137], [-1136, -1129], [-1130, -1129], [-1129, -1111], [-1111, -1107], [-1107, -1077]]
titlesp = ['Ramesses\nII', 'Earthquakes\n', 'Merneptah', 'Seti II', 'Amenmesse', 'Siptah', 'Twosret', 'Setnakhte', 'Ramesses\nIII', 'Ramesses\nIV', 'Ramesses V', 'Ramesses\nVI', 'Ramesses\nVII', 'Ramesses\nVIII', 'Ramesses\nIX', 'Ramesses X', 'Ramesses\nXI']
cdates = [[-1279, -1213], [-1203, -1197], [-1191, -1189], [-1186, -1155], [-1149, -1145], [-1136, -1129], [-1111, -1107]]
ctitles = ['Ramesses\nII', 'Seti II', 'Twosret', 'Ramesses\nIII', 'Ramesses V', 'Ramesses\nVII', 'Ramesses X']


from bokeh.plotting import figure, save
from bokeh.models import LabelSet, ColumnDataSource, CustomJSTickFormatter
from bokeh.core.properties import value

def get_source_from_event_dict(event_dict):
    return ColumnDataSource(data=event_dict)

def setup_figure(*args, **kwargs):
    if not "tools" in kwargs:
        kwargs["tools"] = "hover,pan,wheel_zoom,box_zoom,reset,save"
    #return figure(tools=TOOLS, title=title, x_axis_label=x_axis_label, y_axis_label=y_axis_label, height=height, width=width, y_range=["p1", "Event", "Person"])
    return figure(*args, **kwargs)
    

def render_events(plot, source, x, y, size):
    plot.scatter(x=x, y=y, size=size, source=source)
    
def event_tooltips(plot, tooltip_names):
    tooltips = []
    for tool in tooltip_names:
        tooltips.append((tool, "@" + tool))
    plot.hover.tooltips = tooltips
    
def event_labels(plot, source, x, y, text, y_offset=8,
                  text_font_size="11px", text_color="#555555", text_align='center'):
    labels = LabelSet(x=x, y=y, text=text, y_offset=y_offset,
                  text_font_size=text_font_size, text_color=text_color,
                  text_align=text_align, source=source)
    plot.add_layout(labels)
    
# TODO: More on periods
def render_periods(plot):
    for i in range(len(cdates)):
        dates = cdates[i]
        src = ColumnDataSource(data=dict(title=[ctitles[i]]))
        plot.hbar(right=dates[0], left=dates[1], y=value("p1"), source=src)

def format_xaxis(plot, scientific=False):
    code = ""
    if scientific:
        code = '''return tick < 0 ? Math.abs(tick) + " BCE" : tick +  " CE"'''
    else:
        code = '''return tick < 0 ? Math.abs(tick) + " BC" : tick +  " AD"'''
    plot.xaxis.formatter = CustomJSTickFormatter(code=code)
    
def render_timeline(title, event_dict):
    source = get_source_from_event_dict(event_dict)
    p = setup_figure(title=title, x_axis_label="year", y_axis_label="category", height=300, width=1600, y_range=["p1", "Event", "Person"])
    #p = setup_figure()
    event_tooltips(p, tooltip_names=["title", "description"])
    render_events(p, source, x='dates', y='label', size=20)
    event_labels(p, source, x="dates", y="label", text="title")
    render_periods(p)
    format_xaxis(p, False)
    save(p, "output.html", title=title)
    
    
if __name__ == "__main__":
    pass