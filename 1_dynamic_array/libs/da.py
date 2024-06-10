class DynamicArray:
    def __init__(self):
        self.arr = None
        self.len = 0
        self.cap = 0

    def push(self, data):
        if self.arr == None:
            self.cap = 1
            self.arr = [data]
            self.len = 1
        elif self.len == self.cap:
            self.cap *= 2
            tmp_arr = [None] * self.cap
            for i in range(self.len):
                tmp_arr[i] = self.arr[i]
            tmp_arr[self.len] = data
            self.len += 1
            self.arr = tmp_arr
        elif self.len < self.cap:
            self.arr[self.len] = data
            self.len += 1

    def print(self):
        print(self.arr)
