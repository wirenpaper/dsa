from libs.node import Node

def test_push():
    n1 = Node(3)
    assert n1.data == 3
    assert n1.next == None
    n1.push(4)
    assert n1.next != None
    assert n1.data == 3
    assert n1.next.data == 4
    n1.push(5)
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    n1.push(6)
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    assert n1.next.next.next.data == 6

def test_pop():
    n1 = Node(3)
    assert n1.data == 3
    _, res = n1.pop()
    assert res == 3
    n1 = None
    assert n1 == None

    n1 = Node(3)
    n1.push(4)
    _, res = n1.pop()
    assert res == 4
    assert n1.next == None
    assert n1.data == 3

    n1 = Node(3)
    n1.push(4)
    n1.push(5)
    n1.push(6)
    n1.push(7)
    _, res = n1.pop()
    assert n1.data == 3
    assert n1.next.data == 4
    assert n1.next.next.data == 5
    assert n1.next.next.next.data == 6
    assert n1.next.next.next.next == None
    assert res == 7
