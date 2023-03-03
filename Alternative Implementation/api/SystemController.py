class SystemController:
    def __init__(self, app, api):
        self.CURRENT_USER = None
        self.CURRENT_MATCH = None
        self.CURRENT_TOURNAMENT = None
        self.GUI_ROOT = app

        self.app = app
        self.api = api

        self.api.setSystemController(self)
        self.app.setSystemController(self)

        self.app.startApp()
