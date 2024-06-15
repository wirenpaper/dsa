from libs.list import List

def test_add_first():
    mlist = List()
    assert mlist.head == None
    assert mlist.tail == None

    mlist.add_first(3)
    assert mlist.head.data == 3
    assert mlist.tail.data == 3
    assert mlist.head.next == None
    assert mlist.tail.next == None
    assert mlist.head.prev == None
    assert mlist.tail.prev == None

    mlist.add_first(4)
    assert mlist.head.data == 4
    assert mlist.tail.data == 3
    assert mlist.head.next.data == 3
    assert mlist.head.next.prev.data == 4
    assert mlist.tail.prev.data == 4

    mlist.add_first(5)
    assert mlist.head.data == 5
    assert mlist.tail.data == 3

    assert mlist.head.prev == None
    assert mlist.tail.next == None

    assert mlist.head.next.next.data == 3
    assert mlist.tail.prev.prev.data == 5

    assert mlist.head.next.prev.data == 5
    assert mlist.tail.prev.next.data == 3

def test_add_last():
    mlist = List()
    assert mlist.head == None
    assert mlist.tail == None

    mlist.add_last(3)
    assert mlist.head.data == 3
    assert mlist.head.next == None
    assert mlist.tail.data == 3
    assert mlist.tail.prev == None

    mlist.add_last(4)
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next == None
    assert mlist.tail.data == 4
    assert mlist.tail.prev.data == 3
    assert mlist.tail.prev.prev == None

    mlist.add_last(5)
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next.data == 5
    assert mlist.head.next.next.next == None
    assert mlist.tail.data == 5
    assert mlist.tail.prev.data == 4
    assert mlist.tail.prev.prev.data == 3
    assert mlist.tail.prev.prev.prev == None

    mlist.add_last(6)
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next.data == 5
    assert mlist.head.next.next.next.data == 6
    assert mlist.head.next.next.next.next == None
    assert mlist.tail.data == 6
    assert mlist.tail.prev.data == 5
    assert mlist.tail.prev.prev.data == 4
    assert mlist.tail.prev.prev.prev.data == 3
    assert mlist.tail.prev.prev.prev.prev == None


def test_remove_last():
    mlist = List()
    res = mlist.remove_last()
    assert res == None

    mlist.add_last(3)
    mlist.add_last(4)
    mlist.add_last(5)
    mlist.add_last(6)
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next.data == 5
    assert mlist.head.next.next.next.data == 6
    assert mlist.head.next.next.next.next == None
    assert mlist.tail.data == 6
    assert mlist.tail.prev.data == 5
    assert mlist.tail.prev.prev.data == 4
    assert mlist.tail.prev.prev.prev.data == 3
    assert mlist.tail.prev.prev.prev.prev == None

    res = mlist.remove_last()
    assert res == 6
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next.data == 5
    assert mlist.head.next.next.next == None
    assert mlist.tail.data == 5
    assert mlist.tail.prev.data == 4
    assert mlist.tail.prev.prev.data == 3
    assert mlist.tail.prev.prev.prev == None

    res = mlist.remove_last()
    assert res == 5
    assert mlist.head.data == 3
    assert mlist.head.next.data == 4
    assert mlist.head.next.next == None
    assert mlist.tail.data == 4
    assert mlist.tail.prev.data == 3
    assert mlist.tail.prev.prev == None

    res = mlist.remove_last()
    assert res == 4
    assert mlist.head.data == 3
    assert mlist.head.next == None
    assert mlist.tail.data == 3
    assert mlist.tail.prev == None

    res = mlist.remove_last()
    assert res == 3
    assert mlist.head == None 
    assert mlist.tail == None

    res = mlist.remove_last()
    assert res == None
