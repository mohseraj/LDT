import xlrd
from ldt import LDT


class LDTMgr:
    EXCEL_SUFFIX = '*.xls*'

    def __init__(self, folder_path):
        self._folder_path = folder_path
        self.ldts = []
        self.combined_ldt = None

    def load(self):
        self.ldts = [LDT(xlrd.open_workbook(path)) for path in self._folder_path.glob(self.EXCEL_SUFFIX)]

    def combine_wbs(self):
        pass