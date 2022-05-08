"""

"""


class MyRangeIterator:
    def __init__(self, stop):
        self.number = -1
        self.stop = stop

    def __next__(self):
        if self.number >= self.stop - 1:
            raise StopIteration()
        self.number += 1
        return self.number


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)


# for number in MyRange(5):
#     print(number)  # 0 1 2 3 4

my_range = MyRange(1000)
iterator = my_range.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
