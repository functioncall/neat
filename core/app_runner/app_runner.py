
from core.app.neat.neat import Neat


class AppRunner:

    def __init__(self):
        self.app = Neat()

    def run_application(self):
        self.app.execute()
