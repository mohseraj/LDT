import xlrd
import openpyxl
from abc import ABC, abstractmethod
from cfg import shared as cfg


class XLWrapper(ABC):
    @abstractmethod
    def sheet_names(self):
        pass

    @abstractmethod
    def valid_rows(self) -> list[dict]:
        pass


class XLSWrapper(XLWrapper):
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
            rowd = {'rowx': rowx+1}
            rowd.update({specname: row_values[colx] for specname, colx in cfg.colx_map.items()})
            res.append(rowd)

        return res


class XLSXWrapper(XLWrapper):
    def __init__(self, wb_path):
        self._book = openpyxl.load_workbook(wb_path)

    @property
    def sheet_names(self):
        return self._book.sheetnames

    @property
    def valid_rows(self):
        pass


def create_wbs(wb_path):
    if wb_path.suffix == '.xls':
        return XLSWrapper(wb_path)
    else:
        return XLSXWrapper(wb_path)