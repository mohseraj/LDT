import xlrd
import openpyxl
from abc import ABC, abstractmethod


class WBWrapper(ABC):
    @abstractmethod
    def sheet_names(self):
        pass

class _SWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = xlrd.open_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheet_names()


class _SXWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = openpyxl.load_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheetnames


def load_wbs(wb_path):
    if wb_path.suffix == '.xls':
        return _SWBWrapper(wb_path)
    else:
        return _SXWBWrapper(wb_path)