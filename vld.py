from cfg import shared as cfg
from abc import ABC, abstractmethod
from numbers import Number

class RowValuesValidator(ABC):
    @staticmethod
    @abstractmethod
    def is_valid(row_values: dict) -> bool:
        pass


class RootValidator(RowValuesValidator):
    @staticmethod
    def is_valid(row_values: dict) -> bool:
        root_values = [isinstance(row_values['seq'], Number), row_values['size'], row_values['class'], row_values['service']]
        return all(root_values)