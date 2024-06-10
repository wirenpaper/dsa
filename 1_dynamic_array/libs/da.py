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

    def print(self):
        print(self.arr)
