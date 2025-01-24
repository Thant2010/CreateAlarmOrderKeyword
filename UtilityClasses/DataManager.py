import json


class DataManager:

    @staticmethod
    def saveData(category: str, keyword: str, data: dict):
        fullData = DataManager.getFullData()

        if category not in fullData:
            fullData[category] = {}

        if keyword not in fullData[category]:
            fullData[category][keyword] = {}

        fullData[category][keyword] = data

        DataManager.__saveFullData(fullData)

    @staticmethod
    def getBaseData() -> dict:
        file = open("json/AAO Basic.json", "r")
        baseData = json.loads(file.read())
        file.close()
        return baseData

    @staticmethod
    def getKeywordData(category: str, keyword: str, group: str) -> dict:
        fullData = DataManager.getFullData()

        return fullData[category][keyword][group]

    @staticmethod
    def getFullData() -> dict:
        file = open("json/AAO.json", "r")
        fullData = json.loads(file.read())
        file.close()
        return fullData

    @staticmethod
    def __saveFullData(data: dict):
        file = open("json/AAO.json", "w")
        file.write(json.dumps(data))
        file.close()