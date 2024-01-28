
from enum import Enum

class DeviceType(Enum):
    "設備類型"
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3

class DeviceItem:
    "設備項"
    def __init__(self, id, name, type, isDefault = False) -> None:
        self._id = id
        self._name = name
        self._type = type
        self._isDefault = isDefault
    def __str__(self) -> str:
        return "type:" + str(self._type) + "id:" + str(self._id) \
            + "name:" + str(self._name) + "isDefault:" + str(self._isDefault)
    def getId(self):
        return self._id
    def getName(self):
        return self._name
    def getType(self):
        return self._type
    def isDefault(self):
        return self._isDefault
    
class DeviceList:
    "設備清單"
    def __init__(self) -> None:
        self._devices = []
    def add(self, deviceItem):
        self._devices.append(deviceItem)
    def getCount(self):
        return len(self._devices)
    def getByIdx(self, idx):
        if idx < 0 or idx >= self.getCount():
            return None
        return self._devices[idx]
    def getById(self, id):
        for item in self._devices:
            if(item.getId() == id):
                return item
        return None