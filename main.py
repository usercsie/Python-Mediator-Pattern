
from DeviceItem import DeviceType # import Device Class from DeviceItem Module
from DeviceManager import SpeakerMgr

class DeviceUtil:
    """設備工具類別"""
    def __init__(self) -> None:
        self._mgrs = {}
        self._mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
    def _getDeviceMgr(self, type):
        return self._mgrs[type]
    def getDeviceList(self, type):
        return self._getDeviceMgr(type).enumerate()
    def active(self, type, deviceId):
        self._getDeviceMgr(type).active(deviceId)
    def getCurDeviceId(self, type):
        return self._getDeviceMgr(type).getCurDeviceId()


def testDevices():
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print("麥克風設清單:")
    if deviceList.getCount() > 0:
        deviceUtil.active(DeviceType.TypeSpeaker, deviceList.getByIdx(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)
    print("當前使的設備:" + deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName())


testDevices() 