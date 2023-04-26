import pytest
from mod.hello import Hello

def test_hello(capfd):
    me = Hello("John")
    me.hello()
    out, err = capfd.readouterr()
    assert out == "Hello John."