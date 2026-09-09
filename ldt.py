from cfg import shared as cfg
import vld
from ldt_line import LDTLine


class LDT:
    def __init__(self, wb, row_validator=vld):
        self._wb = wb
        self._active_sheet = wb.sheet_by_index(0)
        self._row_validator = row_validator

    @property
    def valid_rows(self):
        res = []
        for rowx in range(self._active_sheet.nrows):
            row_values = self._active_sheet.row_values(rowx)
            rowd = {'rowx': rowx+1}
            rowd.update({specname: row_values[colx] for specname, colx in cfg.colx_map.items()})
            if not self._row_validator.is_pipeline_row(rowd):
                continue
            res.append(LDTLine(rowd))

        return res
