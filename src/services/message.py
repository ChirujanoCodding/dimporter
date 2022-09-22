from .base import ServiceBase
class MessageService(ServiceBase):
    def __init__(self) -> None:
        super().__init__(200)
        print('='*50)
        print("MessageService connected")
        print('='*50)