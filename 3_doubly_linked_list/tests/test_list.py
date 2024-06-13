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