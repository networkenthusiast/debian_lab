import pytest
from Auth_vManage import authenticate_vmanage

def test_cred():
    assert authenticate_vmanage()
