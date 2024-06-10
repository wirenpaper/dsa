from libs.da import DynamicArray

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
    da = DynamicArray();
    da.push(3)
    da.push(4)
    da.push(5)
    da.push(6)
    da.push(7)
