from string import Formatter
from date import *

dates = [1210, 1207, 1200, 1198, 1197, 1185, 1179, 1177, 1175, 1174, 1161, 1152, 1141, 1107, 1092, 1088]
y_start = [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
datesn = [-1210, -1207, -1200, -1198, -1197, -1185, -1179, -1177, -1175, -1174, -1161, -1152, -1141, -1107, -1092, -1088]
labels = ['Event', 'Event', 'Event', 'Person', 'Person', 'Event', 'Event', 'Event', 'Person', 'Event', 'Event', 'Event', 'Event', 'Event', 'Event', 'Event']

titles = ['Merneptah Ships Grain', 'Sea Peoples', 'Drought in Italy', 'Neferhotep Dies', 'Heria Steals', 'Ugarit Destroyed', 'Unusual offering\nto the Nile', 'Sea Peoples', 'Paneb Dies', 'Sea Peoples', 'Wheat Rations Stop Coming', 'Strike', 'Work Cancelled', 'Tomb Robbers Punished', 'Tombs Examined', 'Grain Riot']
titlesn = ['Merneptah\nShips Grain', 'Sea\nPeoples', 'Drought in\nItaly', 'Neferhotep\nDies', 'Heria\nSteals', 'Ugarit\nDestroyed', 'Unusual\noffering to\nthe Nile', 'Sea\nPeoples', 'Paneb Dies', 'Sea\nPeoples', 'Wheat\nRations\nStop Coming', 'Strike', 'Work\nCancelled', 'Tomb\nRobbers\nPunished', 'Tombs\nExamined', 'Grain Riot']
desc = ['Merneptah donates grain to the Hittitles', 'Earlier wave of Sea Peoples', 'Massive drought in Europe', 'Neferhotep is killed by the enemy', "Heria steals tools from the Workmen's viilage", 'Ugarit is destroyed', 'Ramessess III makes an unual offering to the Nile in the hopes of getting it to cooperate', 'Sea Peoples invade Egypt and are fought off', 'Paneb is executed for theft', 'Ramesses III defeats sea peoples', 'Wheat rations begin to stop being properly paid', 'Workers strike due to nonayment of grain', 'Once instance of work being canceled due to violence', 'An itial set of tomb robbers are punished', 'Tombs are examined for robberies', 'People riot due to lack of food']

from bokeh.plotting import figure, save
from bokeh.models import LabelSet, ColumnDataSource, DatetimeTickFormatter, NumeralTickFormatter, PrintfTickFormatter,TickFormatter,CustomJSTickFormatter
from bokeh.transform import jitter
from bokeh.util.compiler import TypeScript
from bokeh.sampledata.commits import data
from bokeh.core.properties import (
    AnyRef,
    Auto,
    Bool,
    Dict,
    Either,
    Enum,
    Instance,
    Int,
    List,
    Nullable,
    String,
)
from bokeh.core.enums import (
    ContextWhich,
    LatLon,
    LocationType,
    NumeralLanguage,
    RoundingFunction,
)

source = ColumnDataSource(data=dict(x=dates, xn=datesn, y=y_start, title=titlesn, label=labels, description=desc))
TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

p = figure(tools=TOOLS, title="Simple line example", x_axis_label='tbd', y_axis_label='label', width=1600, height=400, y_range=["Event", "Person"])

p.hover.tooltips = [
    ("title", "@title"),
    ("description:", "@description")
]

#p.scatter(x='x', y=jitter('label', width=0.6, range=p.y_range), legend_label="Temp.", size=20, source=source)
p.scatter(x='xn', y='label', legend_label="Temp.", size=20, source=source)


labels = LabelSet(x="xn", y="label", text="title", y_offset=8,
                  text_font_size="11px", text_color="#555555",
                  source=source, text_align='center')
p.add_layout(labels)

class MyNumeralTickFormatter(TickFormatter):
    pass
    
class MyBasicTickFormatter(TickFormatter):
    ''' Display tick values from continuous ranges as "basic numbers",
    using scientific notation when appropriate by default.

    '''

    # explicit __init__ to support Init signatures
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    precision = Either(Auto, Int, help="""
    How many digits of precision to display in tick labels.
    """)

    use_scientific = Bool(True, help="""
    Whether to ever display scientific notation. If ``True``, then
    when to use scientific notation is controlled by ``power_limit_low``
    and ``power_limit_high``.
    """)

    power_limit_high = Int(5, help="""
    Limit the use of scientific notation to when::

        log(x) >= power_limit_high

    """)

    power_limit_low = Int(-3, help="""
    Limit the use of scientific notation to when::

        log(x) <= power_limit_low

    """)

p.xaxis.formatter = CustomJSTickFormatter(code = '''
return Math.abs(tick) + " BCE";
''')
save(p)