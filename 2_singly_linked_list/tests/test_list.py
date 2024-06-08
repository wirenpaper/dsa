from libs.list import List

def test_add_item():
    list1 = List()
    list1.push(3)
    assert list1.head.data == 3
