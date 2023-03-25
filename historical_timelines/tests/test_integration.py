from historical_timelines import *
import pytest


def csv_timeline():
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
    return t0


def test_csv_timeline_creation():
    t0 = csv_timeline()
    assert (
        str(t0)
        == """Events:
Merneptah Ships Grain: Merneptah donates grain to the Hittitles
1210 BCE
Sea Peoples: Earlier wave of Sea Peoples
1207 BCE
Drought in Italy: Massive drought in Europe
1200 BCE
Neferhotep Dies: Neferhotep is killed by the enemy
1198 BCE
Heria Steals: Heria steals tools from the Workmen's viilage
1197 BCE
Ugarit Destroyed: Ugarit is destroyed
1185 BCE
Unusual offering to the Nile: Ramessess III makes an unual offering to the Nile in the hopes of getting it to cooperate
1179 BCE
Sea Peoples: Sea Peoples invade Egypt and are fought off
1177 BCE
Paneb Dies: Paneb is executed for theft
1175 BCE
Sea Peoples: Ramesses III defeats sea peoples
1174 BCE
Wheat Rations Stop Coming: Wheat rations begin to stop being properly paid
1161 BCE
Strike: Workers strike due to nonayment of grain
1152 BCE
Work Cancelled: Once instance of work being canceled due to violence
1141 BCE
Tomb Robbers Punished: An itial set of tomb robbers are punished
1107 BCE
Tombs Examined: Tombs are examined for robberies
1092 BCE
Grain Riot: People riot due to lack of food
1088 BCE
-----
Periods:
Ramesses II: Reign of Ramesses II
1279 BCE - 1213 BCE
Earthquakes: Earthquakes in mainlaind Greece
1225 BCE - 1175 BCE
Merneptah: Reign of Merneptah
1213 BCE - 1203 BCE
Seti II: Reign of Seti II
1203 BCE - 1197 BCE
Amenmesse: Reign of Amenmesse
1201 BCE - 1198 BCE
Siptah: Reign of Siptah
1197 BCE - 1191 BCE
Twosret: Reign of Twosret
1191 BCE - 1189 BCE
Setnakhte: Reign of Setnakhte
1189 BCE - 1186 BCE
Ramesses III: Reign of Ramesses III
1186 BCE - 1155 BCE
Ramesses IV: Reign of Ramesses IV
1155 BCE - 1149 BCE
Ramesses V: Reign of Ramesses V
1149 BCE - 1145 BCE
Ramesses VI: Reign of Ramesses VI
1145 BCE - 1137 BCE
Ramesses VII: Reign of Ramesses VII
1136 BCE - 1129 BCE
Ramesses VIII: Reign of Ramesses VIII
1130 BCE - 1129 BCE
Ramesses IX: Reign of Ramesses IX
1129 BCE - 1111 BCE
Ramesses X: Reign of Ramesses X
1111 BCE - 1107 BCE
Ramesses XI: Reign of Ramesses XI
1107 BCE - 1077 BCE
"""
    )


# TODO: Probably do a better job testing this one
def test_random_timelines():
    t0 = HistoricalTimeline()
    t0.populate_random_timeline(5)

    assert len(t0) == 5
