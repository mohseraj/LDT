import pytest
from os import chdir

chdir('..')

def test_create_wbs():
    from files_mgr import FilesMgr
    mgr = FilesMgr(folder_path='utests/files')
    sheet_names = [file.sheet_names[0] for file in mgr.wbs]
    assert 'SA-2824-ENG-xls' in sheet_names
    assert 'SA-2824-ENG-xlsm' in sheet_names
    assert 'SA-2824-ENG-xlsx' not in sheet_names


def test_is_pipeline_row():
    from vld import is_pipeline_row
    loaded_rows = [
        {'rowx': 1, 'seq': 100, 'size': '10"', 'class': '1CS1P', 'sch.': 40, 'service': 'PROCESS (P)', 'from': 'kladsfk', 'to': 'kasdfl'},
        {'rowx': 2, 'seq': '', 'size': '12"', 'class': '1CS1P', 'sch.': 40, 'service': 'PROCESS (P)', 'from': 'kladsfk', 'to': 'kasdfl'},
        {'rowx': 1, 'seq': 102, 'size': '10"', 'class': '', 'sch.': 40, 'service': 'PROCESS (P)', 'from': 'kladsfk', 'to': 'kasdfl'},
    ]
    assert is_pipeline_row(loaded_rows[0]) == True
    assert is_pipeline_row(loaded_rows[1]) == False


def test_xls_valid_rows():
    from wb_wrapper import XLSWrapper
    valid_rows = XLSWrapper('utests/files/YD736466002XC.xls').valid_rows
    assert len(valid_rows) == 3







