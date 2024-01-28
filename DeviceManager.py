from abc import ABCMeta, abstractmethod
from DeviceItem import DeviceType, DeviceItem, DeviceList # import DeviceType, DeviceItem, DeviceList Class from DeviceItem Module

class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        "枚舉要使用的設備清單"
        pass
    @abstractmethod
    def active(self, deviceId):
        pass
    @abstractmethod
    def getCurDeviceId(self):
        pass

class SpeakerMgr(DeviceMgr):
    "揚聲器設備管理類別"
    def __init__(self) -> None:
        self._curDeviceId = None
    def enumerate(self):
        devices = DeviceList()
        devices.add(DeviceItem("369dd760-893b-4fe0-89b1-671eca0f0224", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357639-6a43-4b79-8184-f79aed9a0dfc", "NVIDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices
    def active(self, deviceId):
        self._curDeviceId = deviceId
    def getCurDeviceId(self):
        return self._curDeviceId