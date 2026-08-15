import xlrd
import openpyxl
from abc import ABC, abstractmethod


class WBWrapper(ABC):
    @abstractmethod
    def sheet_names(self):
        pass

class SWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = xlrd.open_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheet_names()


class SXWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = openpyxl.load_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheetnames


def load_wbs(wb_path):
    if wb_path.suffix == '.xls':
        return SWBWrapper(wb_path)
    else:
        return SXWBWrapper(wb_path)