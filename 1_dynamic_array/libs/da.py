import sys
import inspect

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0


class DynamicArray:
    def __init__(self):
        self.arr = None
        self.len = 0
        self.cap = 0

    def add(self, data):
        if self.arr == None:
            self.cap = 1
            self.arr = [data]
            self.len = 1
        elif self.len < self.cap:
            self.arr[self.len] = data
            self.len += 1
        else:
            self.cap *= 2
            tmp_arr = [None] * self.cap
            for i in range(self.len):
                tmp_arr[i] = self.arr[i]
            tmp_arr[self.len] = data
            self.len += 1
            self.arr = tmp_arr

    def remove_at(self, idx):
        if self.arr == None:
            return None

        if idx < 0 or idx >= self.len:
            raise IndexError("Index out of bounds")

        if self.len-1 == 0:
            data = self.arr[idx]
            self.arr = None
            self.cap = 0
            self.len = 0
            return data

        if is_power_of_2(self.len-1):
            self.cap = int(self.cap / 2)
        data = self.arr[idx]
        tmp_arr = [None] * (self.cap)
        for i in range(self.len):
            if i < idx:
                tmp_arr[i] = self.arr[i]
            if i > idx:
                tmp_arr[i-1] = self.arr[i]
        self.arr = tmp_arr
        self.len -= 1
        return data

    def print(self):
        print(self.arr)
