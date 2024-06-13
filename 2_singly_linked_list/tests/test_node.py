from libs.node import Node

def test_add_last():
    n1 = Node(3)
    assert n1.data == 3
    assert n1.next == None
    n1.add_last(4)
    assert n1.next != None
    assert n1.data == 3
    assert n1.next.data == 4
    n1.add_last(5)
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    n1.add_last(6)
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    assert n1.next.next.next.data == 6

def test_remove_last():
    n1 = Node(3)
    assert n1.data == 3
    _, res = n1.remove_last()
    assert res == 3
    n1 = None
    assert n1 == None

    n1 = Node(3)
    n1.add_last(4)
    _, res = n1.remove_last()
    assert res == 4
    assert n1.next == None
    assert n1.data == 3

    n1 = Node(3)
    n1.add_last(4)
    n1.add_last(5)
    n1.add_last(6)
    n1.add_last(7)
    _, res = n1.remove_last()
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    assert n1.next.next.next.data == 6
    assert n1.next.next.next.next == None
    assert res == 7

def test_add_first():
    n1 = Node(3)
    n1 = n1.add_first(4)
    assert n1.data == 4
    assert n1.next.data == 3
    assert n1.next.next == None

    n1 = n1.add_first(5)
    assert n1.data == 5
    assert n1.next.data == 4
    assert n1.next.next.data == 3
    assert n1.next.next.next == None

    n1 = n1.add_first(6)
    assert n1.data == 6
    assert n1.next.data == 5
    assert n1.next.next.data == 4
    assert n1.next.next.next.data == 3
    assert n1.next.next.next.next == None
