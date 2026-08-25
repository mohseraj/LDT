import xlrd
import openpyxl
from abc import ABC, abstractmethod
from cfg import shared as cfg


class WBWrapper(ABC):
    @abstractmethod
    def sheet_names(self):
        pass

    @abstractmethod
    def valid_rows(self) -> list[dict]:
        pass


class SWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = xlrd.open_workbook(wb_path)
        self._active_sheet = self._book.sheet_by_index(0)

    @property
    def sheet_names(self):
        return self._book.sheet_names()

    @property
    def valid_rows(self) -> list[dict]:
        res = []
        for rowx in range(cfg.start_rowx, cfg.end_rowx):
            row_values = self._active_sheet.row_values(rowx)
            rowd = {'rowx': rowx}
            rowd.update({specname: row_values[colx] for specname, colx in cfg.colx_map.items()})
            res.append(rowd)

        return res



class SXWBWrapper(WBWrapper):
    def __init__(self, wb_path):
        self._book = openpyxl.load_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheetnames

    @property
    def valid_rows(self):
        pass


def load_wbs(wb_path):
    if wb_path.suffix == '.xls':
        return SWBWrapper(wb_path)
    else:
        return SXWBWrapper(wb_path)