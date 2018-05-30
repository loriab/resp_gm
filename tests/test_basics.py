import pytest

def test_true():
    assert True

def test_true2():
    assert a_truth_telling_fn()

def test_false():
    #assert False
    assert not False

def test_badimport():
    #import asdf

    with pytest.raises(ImportError):
        import asdf

def test_import():
    import resp

def a_truth_telling_fn():
    return True

