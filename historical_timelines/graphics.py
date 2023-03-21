dates = [1210, 1207, 1200, 1198, 1197, 1185, 1179, 1177, 1175, 1174, 1161, 1152, 1141, 1107, 1092, 1088]
y_start = [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
datesn = [-1210, -1207, -1200, -1198, -1197, -1185, -1179, -1177, -1175, -1174, -1161, -1152, -1141, -1107, -1092, -1088]
labels = ['Event', 'Event', 'Event', 'Person', 'Person', 'Event', 'Event', 'Event', 'Person', 'Event', 'Event', 'Event', 'Event', 'Event', 'Event', 'Event']

titles = ['Merneptah Ships Grain', 'Sea Peoples', 'Drought in Italy', 'Neferhotep Dies', 'Heria Steals', 'Ugarit Destroyed', 'Unusual offering\nto the Nile', 'Sea Peoples', 'Paneb Dies', 'Sea Peoples', 'Wheat Rations Stop Coming', 'Strike', 'Work Cancelled', 'Tomb Robbers Punished', 'Tombs Examined', 'Grain Riot']
titlesn = ['Merneptah\nShips Grain', 'Sea\nPeoples', 'Drought in\nItaly', 'Neferhotep\nDies', 'Heria\nSteals', 'Ugarit\nDestroyed', 'Unusual\noffering to\nthe Nile', 'Sea\nPeoples', 'Paneb Dies', 'Sea\nPeoples', 'Wheat\nRations\nStop Coming', 'Strike', 'Work\nCancelled', 'Tomb\nRobbers\nPunished', 'Tombs\nExamined', 'Grain Riot']
desc = ['Merneptah donates grain to the Hittitles', 'Earlier wave of Sea Peoples', 'Massive drought in Europe', 'Neferhotep is killed by the enemy', "Heria steals tools from the Workmen's viilage", 'Ugarit is destroyed', 'Ramessess III makes an unual offering to the Nile in the hopes of getting it to cooperate', 'Sea Peoples invade Egypt and are fought off', 'Paneb is executed for theft', 'Ramesses III defeats sea peoples', 'Wheat rations begin to stop being properly paid', 'Workers strike due to nonayment of grain', 'Once instance of work being canceled due to violence', 'An itial set of tomb robbers are punished', 'Tombs are examined for robberies', 'People riot due to lack of food']

pdates = [[-1279, -1213], [1225, 1175], [1213, 1203], [1203, 1197], [1201, 1198], [1197, 1191], [1191, 1189], [1189, 1186], [1186, 1155], [1155, 1149], [1149, 1145], [1145, 1137], [1136, 1129], [1130, 1129], [1129, 1111], [1111, 1107], [1107, 1077]]
pdatesn = [[-1279, -1213], [-1225, -1175], [-1213, -1203], [-1203, -1197], [-1201, -1198], [-1197, -1191], [-1191, -1189], [-1189, -1186], [-1186, -1155], [-1155, -1149], [-1149, -1145], [-1145, -1137], [-1136, -1129], [-1130, -1129], [-1129, -1111], [-1111, -1107], [-1107, -1077]]
titlesp = ['Ramesses\nII', 'Earthquakes\n', 'Merneptah', 'Seti II', 'Amenmesse', 'Siptah', 'Twosret', 'Setnakhte', 'Ramesses\nIII', 'Ramesses\nIV', 'Ramesses V', 'Ramesses\nVI', 'Ramesses\nVII', 'Ramesses\nVIII', 'Ramesses\nIX', 'Ramesses X', 'Ramesses\nXI']
cdates = [[-1279, -1213], [-1203, -1197], [-1191, -1189], [-1186, -1155], [-1149, -1145], [-1136, -1129], [-1111, -1107]]
ctitles = ['Ramesses\nII', 'Seti II', 'Twosret', 'Ramesses\nIII', 'Ramesses V', 'Ramesses\nVII', 'Ramesses X']


from bokeh.plotting import figure, save
from bokeh.models import LabelSet, ColumnDataSource, CustomJSTickFormatter
from bokeh.core.properties import value

def get_source_from_timeline():
    return ColumnDataSource(data=dict(x=dates, xn=datesn, y=y_start, title=titlesn, label=labels, description=desc))

def setup_figure():
    TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"
    return figure(tools=TOOLS, title="Simple line example", x_axis_label='tbd', y_axis_label='label', width=1600, height=400, y_range=["p1", "Event", "Person"])

def render_events(plot, source):
    plot.scatter(x='xn', y='label', legend_label="Temp.", size=20, source=source)
    
def event_tooltips(plot):
    plot.hover.tooltips = [
        ("title", "@title"),
        ("description:", "@description")
    ]
    
def event_labels(plot, source):
    labels = LabelSet(x="xn", y="label", text="title", y_offset=8,
                  text_font_size="11px", text_color="#555555",
                  source=source, text_align='center')
    plot.add_layout(labels)
    
def render_periods(plot):
    for i in range(len(cdates)):
        dates = cdates[i]
        src = ColumnDataSource(data=dict(title=[ctitles[i]]))
        plot.hbar(right=dates[0], left=dates[1], y=value("p1"), source=src)

def format_xaxis(plot):
    plot.xaxis.formatter = CustomJSTickFormatter(code = '''
    return Math.abs(tick) + " BCE";
    ''')
    
    
def chart_timeline():
    source = get_source_from_timeline()
    p = setup_figure()
    event_tooltips(p)
    render_events(p, source)
    event_labels(p, source)
    render_periods(p)
    format_xaxis(p)
    save(p)
    
chart_timeline()