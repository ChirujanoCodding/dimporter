from .base import ServiceBase
class ServiceProvider(ServiceBase):
    def __init__(self) -> None:
        super().__init__(200)
        print('='*50)
        print("ServiceProvider Hosted")
        print('='*50)