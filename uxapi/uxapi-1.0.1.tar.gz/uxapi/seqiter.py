class seqiter:
    def __init__(self, seq):
        self.seq = seq
        self.cursor = 0 if seq else -1
        self.saved_cursor = -1

    def has_next(self):
        return 0 <= self.cursor < len(self.seq)

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_next():
            self.cursor += 1
            return self.seq[self.cursor - 1]
        raise StopIteration

    def rewind(self):
        if self.cursor > 0:
            self.cursor = 0
        self.saved_cursor = -1

    def mark(self):
        if self.cursor >= 0:
            self.saved_cursor = self.cursor
        else:
            raise RuntimeError('invalid state')

    def reset(self):
        if self.saved_cursor < 0:
            raise RuntimeError('mark not set')
        self.cursor = self.saved_cursor

    def prepend(self, elem):
        self.seq.insert(0, elem)
        self.cursor += 1

    def append(self, elem):
        self.seq.append(elem)
        if self.cursor < 0:
            self.cursor = 0

    def add(self, elem):
        i = max(self.cursor, 0)
        self.seq.insert(i, elem)
        self.cursor += 1

    def remove(self, elem=None):
        if elem is None:
            i = self.cursor - 1
        else:
            i = self.seq.index(elem)

        if i < 0:
            raise IndexError('no previous element')

        self.seq.pop(i)
        if self.cursor > 0:
            if i < self.cursor:
                self.cursor -= 1
        else:
            if not self.seq:
                self.cursor = -1

    def set(self, new_elem):
        if self.cursor > 0:
            self.seq[self.cursor - 1] = new_elem
        raise IndexError('no previous element')
