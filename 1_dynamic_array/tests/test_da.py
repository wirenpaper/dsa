from libs.da import DynamicArray
import pytest

def test_add():
    da = DynamicArray()
    assert da.arr == None
    assert da.cap == 0
    assert da.len == 0
    da.add(3)
    assert da.arr == [3]
    assert da.cap == 1
    assert da.len == 1
    da.add(4)
    assert da.arr == [3, 4]
    assert da.cap == 2
    assert da.len == 2
    da.add(5)
    assert da.arr == [3, 4, 5, None]
    assert da.cap == 4
    assert da.len == 3
    da.add(6)
    assert da.arr == [3, 4, 5, 6]
    assert da.cap == 4
    assert da.len == 4
    da.add(7)
    assert da.arr == [3, 4, 5, 6, 7, None, None, None]
    assert da.cap == 8
    assert da.len == 5

def test_remove_at():
    da = DynamicArray()
    da.add(3)
    da.add(4)
    da.add(5)
    da.add(6)
    da.add(7)
    res = da.remove_at(2)
    assert res == 5

    with pytest.raises(IndexError, match="Index out of bounds"):
        da.remove_at(-1)
        pytest.fail("Expected IndexError was not raised")

    with pytest.raises(IndexError, match="Index out of bounds"):
        da.remove_at(4)
        pytest.fail("Expected IndexError was not raised")

    res = da.remove_at(2)
    assert res == 6

    da = DynamicArray()

    res = da.remove_at(0)
    assert res == None

    res = da.remove_at(5)
    assert res == None

    da = DynamicArray()
    da.add(3)

    with pytest.raises(IndexError, match="Index out of bounds"):
        res = da.remove_at(2)
        pytest.fail("Expected IndexError was not raised")

    res = da.remove_at(0)
    assert res == 3
    assert da.cap == 0
    assert da.len == 0
    assert da.arr == None
