

class AppRunner:

    def __init__(self, app):
        self.app = app

    def run_application(self):
        self.app.execute()
