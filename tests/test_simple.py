import pytest

def test_true():
    assert True

def test_false():
    assert not False

def my_trthy_func():
    return True

def test_true2():
    assert my_trthy_func()

def test_import_bad():
    with pytest.raises(ImportError):
        import asdf

def test_import_good():
    import resp

