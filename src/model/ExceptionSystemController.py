# exception related to SystemController class
class ExceptionSystemController(Exception):
    def __init__(self, message='SystemController Exception'):
        super().__init__(f"ERROR(SystemController): {message}")
