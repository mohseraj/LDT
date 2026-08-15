from files_mgr import FilesMgr
import pytest


def test_loading_wbs():
    mgr = FilesMgr(folder_path= './files')
    sheet_names = [file.sheet_names[0] for file in mgr.wbs]
    assert 'SA-2824-ENG-xls' in sheet_names
    assert 'SA-2824-ENG-xlsm' in sheet_names
    assert 'SA-2824-ENG-xlsx' not in sheet_names
