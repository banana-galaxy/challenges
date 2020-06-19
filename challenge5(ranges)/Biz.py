class erange:
    def __init__(self, *args):
        if any([arg for arg in args if not isinstance(arg, int)]): raise TypeError("Input must be int and Alex is a weeb")
        if len(args) == 0:
            raise Exception("you gave no arguments and Alex killed my one liner streak")
        elif len(args) == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
        else:
            raise Exception("Too many arguments given and Alex is a weeb")
        self._start = self.start
        if self.step == 0: raise ValueError("step of 0 given and Alex ruined my lambdas")
    def __iter__(self):
        return self
    def __next__(self):
        if self.step > 0:
            condition = self.start < self.stop
        else:
            condition = self.start > self.stop
        if not condition:
            self.start = self._start
            raise StopIteration
        self.start += self.step
        return self.start - self.step
    def __str__(self):
        return f'range({self.start}, {self.stop})'
    def __getitem__(self, item):
        result = (item * self.step) + self.start
        if self.step > 0:
            condition = result < self.stop
        else:
            condition = result > self.stop
        if condition:
            return result
        else:
            raise IndexError("Invalid index given and Alex is weeb who killed my one liners")
    def __len__(self):
        # if it is evenly divisible, return value, else return value + 1
        if ((self.stop - self.start) // self.step) == ((self.stop - self.start) / self.step):
            return (self.stop - self.start) // self.step
        else:
            return ((self.stop - self.start) // self.step) + 1
    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop and self.step == other.step if isinstance(other, erange) else False
    __repr__ = __str__



def numerate(iterable, start=0):
    for item in iterable: yield start, item; start += 1