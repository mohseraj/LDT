from cfg import shared as cfg
from abc import ABC, abstractmethod

class RowValuesValidator(ABC):
    @staticmethod
    @abstractmethod
    def is_valid(row_values: dict) -> bool:
        pass


class RootValidator(RowValuesValidator):
    @staticmethod
    def is_valid(row_values: dict) -> bool:
        root_values = [row_values['seq'], row_values['size'], row_values['class'], row_values['service']]
        return all(root_values)




''' what do you want to validate?
    1. the row has seq, size, service
'''