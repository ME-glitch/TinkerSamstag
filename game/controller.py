from .viewModel import ViewModel
from .model import Model


class Controller:

    def __init__(self):
        self.view = ViewModel()
        self.model = Model()
        pass