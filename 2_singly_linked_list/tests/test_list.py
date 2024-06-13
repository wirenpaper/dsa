from libs.list import List

def test_add_last():
    list1 = List()
    list1.add_last(3)
    assert list1.head.data == 3
    list1.add_last(4)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    list1.add_last(5)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    assert list1.head.next.next.data == 5
    list1.add_last(6)
    assert list1.head.data == 3
    assert list1.head.next.data == 4
    assert list1.head.next.next.data == 5
    assert list1.head.next.next.next.data == 6

def test_remove_last():
    list1 = List()
    assert list1.head == None
    res = list1.remove_last()
    assert res == None

    list1 = List()
    list1.add_last(3)
    res = list1.remove_last()
    assert res == 3
    assert list1.head == None

    list1 = List()
    list1.add_last(3)
    list1.add_last(4)
    res = list1.remove_last()
    assert res == 4
    assert list1.head.data == 3
    assert list1.head.next == None

def test_add_first():
    list1 = List()
    assert list1.head == None

    list1.add_first(3)
    assert list1.head.data == 3
    assert list1.head.next == None
    list1.add_first(4)
    assert list1.head.data == 4
    assert list1.head.next.data == 3
    list1.add_first(5)
    assert list1.head.data == 5
    assert list1.head.next.data == 4
    assert list1.head.next.next.data == 3
    assert list1.head.next.next.next == None
