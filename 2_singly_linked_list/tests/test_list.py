from libs.list import List

def test_add_item():
    list1 = List()
    list1.push(3)
    assert list1.head.data == 3
    list1.push(4)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    list1.push(5)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    assert list1.head.next.next.data == 5
    list1.push(6)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    assert list1.head.next.next.data == 5
    assert list1.head.next.next.next.data == 6
