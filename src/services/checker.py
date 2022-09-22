
class Checker:

    def __init__(self) -> None:
        print('='*50)
        print('Checker Auditioning...')
        print('='*50)
    @classmethod
    def check_status(cls, _=None) -> int:
        return _.status  # type: ignore