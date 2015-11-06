from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dict = defaultdict(int)


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.dict[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.dict:
            if (value-n) == n:
                if self.dict[n] > 1:
                    return True
            elif (value-n) in self.dict:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)