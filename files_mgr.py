from pathlib import Path
import wb_wrapper


class FilesMgr:
    EXCEL_SUFFIX = '*.xls*'

    def __init__(self, folder_path):
        self._folder_path = Path(folder_path)

    @property
    def wbs(self):
        return [wb_wrapper.create_wbs(path) for path in self._folder_path.glob(self.EXCEL_SUFFIX)]
       