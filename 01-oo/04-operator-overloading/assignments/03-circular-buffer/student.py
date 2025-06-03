class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.count = 0

    def append(self, value):
        idx = (self.start + self.count) % self.size
        self.buffer[idx] = value
        
        if self.count < self.size:
            self.count += 1
        else:
            self.start = (self.start + 1) % self.size

    def add(self, value):
        self.append(value)

    def __getitem__(self, index):
        if not 0 <= index < self.count:
            raise IndexError("Index out of range")
        return self.buffer[(self.start + index) % self.size]
    
    def __setitem__(self, index, value):
        if not 0 <= index < self.count:
            raise IndexError("Index out of range")
        self.buffer[(self.start + index) % self.size] = value

    def __len__(self):
        return self.count
    
    def __str__(self):
        return str([self[i] for i in range(self.count)])