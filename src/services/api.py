from .base import ServiceBase
class API(ServiceBase):
    def __init__(self) -> None:
        super().__init__(200)
        print('='*50)
        print("API connected")
        print('='*50)

    def getHi(self):
        return 'Hi!'