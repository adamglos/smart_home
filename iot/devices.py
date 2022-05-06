from iot.device import Device
from iot.message import MessageType


class HueLight(Device):
    def connect(self):
        print("Connecting hue light")

    def disconnect(self):
        print("Disconnecting hue light")

    def send_message(self, message_type, data):
        print(
            f"Hue light handling message of type {message_type.name} with data [{data}]."
        )

    def status_update(self):
        print("hue_light_status_ok")


class SmartSpeaker(Device):
    def connect(self):
        print("Connecting smart speaker")

    def disconnect(self):
        print("Disconnecting smart speaker")

    def send_message(self, message_type, data):
        print(
            f"Smart speaker handling message of type {message_type.name} with data [{data}]."
        )

    def status_update(self):
        print("smart_speaker_status_ok")


class Curtains(Device):
    def connect(self):
        print("Connecting curtains")

    def disconnect(self):
        print("Disconnecting curtains")

    def send_message(self, message_type, data):
        print(
            f"Curtains handling message of type {message_type.name} with data [{data}]."
        )

    def status_update(self):
        print("curtains_status_ok")
