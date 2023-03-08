from historical_timelines import *


def test_timeline_csv():
    t0 = HistoricalTimeline()
    j0 = HistoricalTimeline.json_from_csv(
        "historical_timelines/tests/timeline_egypt.csv",
        "Event",
        "Description",
        "Start",
        "End",
        Era.BCE,
    )

    assert (
        str(j0)
        == "[{'title': 'Amenmesse', 'description': 'Reign of Amenmesse', 'start': 1201, 'end': 1198, 'era': <Era.BCE: -1>}, {'title': 'Drought in Italy', 'description': 'Massive drought in Europe', 'start': 1200, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Earthquakes', 'description': 'Earthquakes in mainlaind Greece', 'start': 1225, 'end': 1175, 'era': <Era.BCE: -1>}, {'title': 'Grain Riot', 'description': 'People riot due to lack of food', 'start': 1088, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Heria Steals', 'description': \"Heria steals tools from the Workmen's viilage\", 'start': 1197, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Merneptah', 'description': 'Reign of Merneptah', 'start': 1213, 'end': 1203, 'era': <Era.BCE: -1>}, {'title': 'Merneptah Ships Grain', 'description': 'Merneptah donates grain to the Hittitles', 'start': 1210, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Neferhotep Dies', 'description': 'Neferhotep is killed by the enemy', 'start': 1198, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Paneb Dies', 'description': 'Paneb is executed for theft', 'start': 1175, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Ramesses II', 'description': 'Reign of Ramesses II', 'start': 1279, 'end': 1213, 'era': <Era.BCE: -1>}, {'title': 'Ramesses III', 'description': 'Reign of Ramesses III', 'start': 1186, 'end': 1155, 'era': <Era.BCE: -1>}, {'title': 'Ramesses IV', 'description': 'Reign of Ramesses IV', 'start': 1155, 'end': 1149, 'era': <Era.BCE: -1>}, {'title': 'Ramesses IX', 'description': 'Reign of Ramesses IX', 'start': 1129, 'end': 1111, 'era': <Era.BCE: -1>}, {'title': 'Ramesses V', 'description': 'Reign of Ramesses V', 'start': 1149, 'end': 1145, 'era': <Era.BCE: -1>}, {'title': 'Ramesses VI', 'description': 'Reign of Ramesses VI', 'start': 1145, 'end': 1137, 'era': <Era.BCE: -1>}, {'title': 'Ramesses VII', 'description': 'Reign of Ramesses VII', 'start': 1136, 'end': 1129, 'era': <Era.BCE: -1>}, {'title': 'Ramesses VIII', 'description': 'Reign of Ramesses VIII', 'start': 1130, 'end': 1129, 'era': <Era.BCE: -1>}, {'title': 'Ramesses X', 'description': 'Reign of Ramesses X', 'start': 1111, 'end': 1107, 'era': <Era.BCE: -1>}, {'title': 'Ramesses XI', 'description': 'Reign of Ramesses XI', 'start': 1107, 'end': 1077, 'era': <Era.BCE: -1>}, {'title': 'Sea Peoples', 'description': 'Ramesses III defeats sea peoples', 'start': 1174, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Sea Peoples', 'description': 'Sea Peoples invade Egypt and are fought off', 'start': 1177, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Sea Peoples', 'description': 'Earlier wave of Sea Peoples', 'start': 1207, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Seti II', 'description': 'Reign of Seti II', 'start': 1203, 'end': 1197, 'era': <Era.BCE: -1>}, {'title': 'Setnakhte', 'description': 'Reign of Setnakhte', 'start': 1189, 'end': 1186, 'era': <Era.BCE: -1>}, {'title': 'Siptah', 'description': 'Reign of Siptah', 'start': 1197, 'end': 1191, 'era': <Era.BCE: -1>}, {'title': 'Strike', 'description': 'Workers strike due to nonayment of grain', 'start': 1152, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Tomb Robbers Punished', 'description': 'An itial set of tomb robbers are punished', 'start': 1107, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Tombs Examined', 'description': 'Tombs are examined for robberies', 'start': 1092, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Twosret', 'description': 'Reign of Twosret', 'start': 1191, 'end': 1189, 'era': <Era.BCE: -1>}, {'title': 'Ugarit Destroyed', 'description': 'Ugarit is destroyed', 'start': 1185, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Unusual offering to the Nile', 'description': 'Ramessess III makes an unual offering to the Nile in the hopes of getting it to cooperate', 'start': 1179, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Wheat Rations Stop Coming', 'description': 'Wheat rations begin to stop being properly paid', 'start': 1161, 'end': None, 'era': <Era.BCE: -1>}, {'title': 'Work Cancelled', 'description': 'Once instance of work being canceled due to violence', 'start': 1141, 'end': None, 'era': <Era.BCE: -1>}]"
    )

    t0.populate_timeline_from_dict(j0)


def test_timeline_len():
    t0 = HistoricalTimeline()
    j0 = HistoricalTimeline.json_from_csv(
        "historical_timelines/tests/timeline_egypt.csv",
        "Event",
        "Description",
        "Start",
        "End",
        Era.BCE,
    )

    t0.populate_timeline_from_dict(j0)

    assert len(t0) == 33
