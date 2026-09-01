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

def test_xls_valid_rows():
    from wb_wrapper import XLSWrapper
    expected = {'rowx': 7, 'seq': 4772, 'class': '3CS2P', 'dp': 300, 'ot': 125}
    first_valid_row = XLSWrapper('utests/files/YD736466002XC.xls').valid_rows[1]
    assert first_valid_row['rowx'] == expected['rowx']
    assert first_valid_row['seq'] == expected['seq']
    assert first_valid_row['class'] == expected['class']
    assert first_valid_row['dp'] == expected['dp']
    assert first_valid_row['ot'] == expected['ot']


def test_root_vld():
    from wb_wrapper import XLSWrapper
    from vld import RootValidator as rvld
    rows_before_validation = XLSWrapper('utests/files/YD736466002XC.xls').valid_rows
    assert rvld.is_valid(rows_before_validation[4]) == True
    assert rvld.is_valid(rows_before_validation[5]) == False
    assert rvld.is_valid(rows_before_validation[37]) == False
    assert rvld.is_valid(rows_before_validation[39]) == False






