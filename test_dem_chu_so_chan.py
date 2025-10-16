import pytest
from dem_chu_so_chan import dem_chu_so_chan

# Test case 1: số âm, có chữ số chẵn
def test_so_am_chu_so_chan():
    assert dem_chu_so_chan(-246) == 3  # -246 có 3 chữ số chẵn

# Test case 2: số dương, tất cả chữ số lẻ
def test_tat_ca_chu_so_le():
    assert dem_chu_so_chan(13579) == 0

# Test case 3: số dương, vừa chữ số chẵn vừa chữ số lẻ
def test_chu_so_chan_va_le():
    assert dem_chu_so_chan(1234) == 2

# Test case 4: số 0
def test_so_khong():
    assert dem_chu_so_chan(0) == 1

# Test case 5: số có 1 chữ số chẵn
def test_chu_so_chan_don():
    assert dem_chu_so_chan(7) == 0
    assert dem_chu_so_chan(8) == 1

# Test case fail ( fail)
# def test_fail_so_am_tat_ca_le():
#     assert dem_chu_so_chan(-1357) == 1  # thuc te = 0 test case fail
