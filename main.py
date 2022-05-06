from time import sleep
from iot.devices import Curtains, HueLight, SmartSpeaker

from iot.service import IOTService

iot = IOTService()

hue_light_1 = iot.register_device(HueLight)
smart_speaker_1 = iot.register_device(SmartSpeaker)
curtains_1 = iot.register_device(Curtains)

sleep(10)
