# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.valid = iterator.hasNext()
        if self.valid:
            self.cur  = iterator.next()
            self.iter = iterator


    def peek(self):
        return self.cur


    def next(self):
        temp = self.cur
        if self.iter.hasNext():
            self.valid = True
            self.cur = self.iter.next()
        else:
            self.valid = False
        return temp


    def hasNext(self):
        return self.valid

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].