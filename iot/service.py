import random
import string


def generate_id():
    id = ""
    for i in range(1, 11):
        id += random.choice(string.ascii_uppercase)
    return id


class IOTService:
    def register_device(self, device):
        self.device_id = generate_id()

    def unregister_device(self, id):
        pass

    def get_device():
        pass

    def run_program():
        print("=====RUNNING PROGRAM======")
        print("...")
        print("=====END OF PROGRAM======")

    def test_devices():
        print("Start test devices")
