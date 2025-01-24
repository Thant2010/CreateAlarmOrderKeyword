import json


file = open("json/global.json", "r", encoding="utf-8")

globalVariables = json.loads(file.read())

alarmCategorys = globalVariables["alarmCategorys"]
vehicles = globalVariables["vehicles"]
staffs = globalVariables["staffs"]
iconButtons = globalVariables["iconButtons"]
