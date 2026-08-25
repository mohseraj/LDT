import pytest
from os import chdir

chdir('..')

def test_loading_wbs():
    from files_mgr import FilesMgr
    mgr = FilesMgr(folder_path='utests/files')
    sheet_names = [file.sheet_names[0] for file in mgr.wbs]
    assert 'SA-2824-ENG-xls' in sheet_names
    assert 'SA-2824-ENG-xlsm' in sheet_names
    assert 'SA-2824-ENG-xlsx' not in sheet_names

def test_xls_valid_rows():
    from wb_wrapper import SWBWrapper
    expected = {'rowx': 6, 'seq': 4772, 'class': '3CS2P', 'dp': 300, 'ot': 125}
    first_valid_row = SWBWrapper('utests/files/YD736466002XC.xls').valid_rows[1]
    assert first_valid_row['rowx'] == expected['rowx']
    assert first_valid_row['seq'] == expected['seq']
    assert first_valid_row['class'] == expected['class']
    assert first_valid_row['dp'] == expected['dp']
    assert first_valid_row['ot'] == expected['ot']




