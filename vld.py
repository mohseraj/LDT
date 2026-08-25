from cfg import shared as cfg
from abc import ABC, abstractmethod

class RowValuesValidator(ABC):
    def __init__(self, row_values):
        self.row_values = row_values

    @abstractmethod
    def is_valid(self):
        pass


class RootValidator(RowValuesValidator):
    def is_valid(self):
        pass



''' what do you want to validate?
    1. the row has seq, size, service
'''