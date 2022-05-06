from abc import abstractmethod


class Device:
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self) -> None:
        pass

    @abstractmethod
    def status_update(self) -> str:
        pass
