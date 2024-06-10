from libs.da import DynamicArray

da = DynamicArray()
da.add(3)
da.add(4)
da.add(5)
da.add(6)
da.add(7)
da.add(8)

print(da.arr)
da.remove_at(2)
print(da.arr)
da.remove_at(2)
print(da.arr)
da.remove_at(0)
print(da.arr)
da.remove_at(2)
print(da.arr)
da.remove_at(0)
print(da.arr)
da.remove_at(0)
print(da.arr)

