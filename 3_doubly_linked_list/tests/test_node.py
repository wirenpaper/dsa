from libs.node import Node

def test_add_first():
    node = Node(3)

    node = node.add_first(4)
    assert node.data == 4
    assert node.next.data == 3
    assert node.next.prev.data == 4
    assert node.prev == None
    assert node.next.prev.prev == None

    node = node.add_first(5)
    assert node.data == 5
    assert node.next.data == 4
    assert node.next.prev.data == 5
    assert node.next.next.data == 3
    assert node.next.next.prev.data == 4
    assert node.prev == None


def test_add_last():
    node = Node(3)
    assert node.data == 3
    assert node.next == None
    assert node.prev == None

    tail = node
    tail = node.add_last(tail, 4)
    assert node.data == 3
    assert node.next.data == 4
    assert tail.data == 4
    assert tail.prev.data == 3
    assert node.next.prev.data == 3
    assert tail.next == None
    assert node.prev == None

    tail = node.add_last(tail, 5)
    assert node.data == 3
    assert node.next.data == 4
    assert node.next.next.data == 5
    assert node.next.next.next == None
    assert tail.data == 5
    assert tail.prev.data == 4
    assert tail.prev.prev.data == 3
    assert tail.prev.prev.prev == None

    tail = node.add_last(tail, 6)
    assert node.data == 3
    assert node.next.data == 4
    assert node.next.next.data == 5
    assert node.next.next.next.data == 6
    assert node.next.next.next.next == None
    assert tail.data == 6
    assert tail.prev.data == 5
    assert tail.prev.prev.data == 4
    assert tail.prev.prev.prev.data == 3
    assert tail.prev.prev.prev.prev == None

def test_remove_last():
    node1 = Node(3)
    tail = node1
    tail = node1.add_last(tail, 4)
    tail = node1.add_last(tail, 5)
    tail = node1.add_last(tail, 6)

    assert node1.data == 3
    assert node1.next.data == 4
    assert node1.next.next.data == 5
    assert node1.next.next.next.data == 6

    _, tail, res = node1.remove_last()
    assert res == 6

    assert node1.prev == None
    assert node1.data == 3
    assert node1.next.data == 4
    assert node1.next.next.data == 5
    assert node1.next.next.next == None
    assert tail.next == None
    assert tail.data == 5
    assert tail.prev.data == 4
    assert tail.prev.prev.data == 3
    assert tail.prev.prev.prev == None
