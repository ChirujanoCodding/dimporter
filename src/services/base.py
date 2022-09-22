import abc



class ServiceBase(abc.ABC):
    
    def __init__(self, status: int) -> None:
        self.__status = status

    @property
    def status(self):
        return self.__status

    def __str__(self) -> str:
        return f"{self.__class__.__name__} [{self.status}]"