import unittest


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        resultsSet = set()
        nums.sort()
        for i in range(0, len(nums)-2):
            for l in range(i+1, len(nums)-1):
                r = len(nums)-1
                while r > l:
                    result = nums[i] + nums[l] + nums[r]
                    if result == 0 :
                        if (nums[i], nums[l], nums[r]) not in resultsSet:
                            results.append([nums[i], nums[l], nums[r]])
                            resultsSet.add((nums[i], nums[l], nums[r]))
                        break
                    elif result > 0:
                        r -= 1
                    else:
                        break

        return results


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_0(self):
        sums = self.solution.threeSum([])
        self.assertListEqual(sums, [])

    def test_1(self):
        sums = self.solution.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertListEqual(sums, [[-1, -1, 2], [-1, 0, 1]])

    def test_2(self):
        sums = self.solution.threeSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13])
        self.assertListEqual(sums, [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,7,8],[-14,0,14],[-14,1,13],[-14,2,12],[-14,3,11],[-14,4,10],[-14,6,8],[-14,7,7],[-13,-1,14],[-13,0,13],[-13,1,12],[-13,2,11],[-13,3,10],[-13,5,8],[-13,6,7],[-12,-2,14],[-12,-1,13],[-12,0,12],[-12,1,11],[-12,2,10],[-12,4,8],[-12,5,7],[-12,6,6],[-11,-3,14],[-11,-2,13],[-11,-1,12],[-11,0,11],[-11,1,10],[-11,3,8],[-11,4,7],[-11,5,6],[-10,-4,14],[-10,-3,13],[-10,-2,12],[-10,-1,11],[-10,0,10],[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-3,12],[-9,-2,11],[-9,-1,10],[-9,1,8],[-9,2,7],[-9,3,6],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-3,11],[-8,-2,10],[-8,0,8],[-8,1,7],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-3,10],[-7,-1,8],[-7,0,7],[-7,1,6],[-7,2,5],[-7,3,4],[-6,-6,12],[-6,-5,11],[-6,-4,10],[-6,-2,8],[-6,-1,7],[-6,0,6],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-3,-3,6],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,0,1]])

    def test_3(self):
        sums = self.solution.threeSum([-1,-12,14,-6,4,-11,2,-7,13,-15,-1,11,-15,-15,13,-9,-11,-10,-7,-13,7,9,-13,-3,10,1,-5,12,11,-9,2,-4,-6,-7,5,5,-2,14,13,-12,14,-3,14,14,-11,5,12,-6,10,-9,-4,-6,-15,-9,-1,2,-1,9,-9,-5,-15,8,-2,-6,9,10,7,14,9,5,-13,9,-12,8,8,-8,-2,-2,1,-15,-4,5,-13,-4,3,1,5,-13,-13,11,-11,10,5,3,11,-9,-2,3,-10,-7,-6,14,9,-11,7,2,-4,13,7,5,13,-12,-13,7,-9,5,-7,11,-1,-12,8,3,13,-10,13,1,-4])
        self.assertListEqual(sums, [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,7,8],[-13,-1,14],[-13,1,12],[-13,2,11],[-13,3,10],[-13,4,9],[-13,5,8],[-12,-2,14],[-12,-1,13],[-12,1,11],[-12,2,10],[-12,3,9],[-12,4,8],[-12,5,7],[-11,-3,14],[-11,-2,13],[-11,-1,12],[-11,1,10],[-11,2,9],[-11,3,8],[-11,4,7],[-10,-4,14],[-10,-3,13],[-10,-2,12],[-10,-1,11],[-10,1,9],[-10,2,8],[-10,3,7],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-3,12],[-9,-2,11],[-9,-1,10],[-9,1,8],[-9,2,7],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-3,11],[-8,-2,10],[-8,-1,9],[-8,1,7],[-8,3,5],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-3,10],[-7,-2,9],[-7,-1,8],[-7,2,5],[-7,3,4],[-6,-6,12],[-6,-5,11],[-6,-4,10],[-6,-3,9],[-6,-2,8],[-6,-1,7],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-4,9],[-5,-3,8],[-5,-2,7],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-1,5],[-4,1,3],[-4,2,2],[-3,-2,5],[-3,-1,4],[-3,1,2],[-2,-2,4],[-2,-1,3],[-2,1,1],[-1,-1,2]])

    def test_4(self):
        sums = self.solution.threeSum([11,-8,9,-6,-10,14,-5,-10,2,-1,-14,-13,-5,9,-5,-12,9,5,-1,-4,-14,5,-11,3,6,-7,2,-14,9,-6,-8,-2,-7,8,7,-2,7,9,3,-14,-14,5,-12,-4,-9,-1,-8,7,11,-2,-11,4,-11,-15,-7,10,-7,10,4,10,11,11,-7,-11,4,7,2,-12,1,12,-10,2,2,-15,6,1,-1,13,-7,-12,-4,-11,7,0,-11,-15,-12,-10,2,7,-15,-2,3,-15,-6,14,-1,11,-13,-15,9,14,-5,-12,-15,-14,4,-9,6,5,-6,-13,9])
        self.assertListEqual(sums, [[-15,1,14],[-15,2,13],[-15,3,12],[-15,4,11],[-15,5,10],[-15,6,9],[-15,7,8],[-14,0,14],[-14,1,13],[-14,2,12],[-14,3,11],[-14,4,10],[-14,5,9],[-14,6,8],[-14,7,7],[-13,-1,14],[-13,0,13],[-13,1,12],[-13,2,11],[-13,3,10],[-13,4,9],[-13,5,8],[-13,6,7],[-12,-2,14],[-12,-1,13],[-12,0,12],[-12,1,11],[-12,2,10],[-12,3,9],[-12,4,8],[-12,5,7],[-12,6,6],[-11,-2,13],[-11,-1,12],[-11,0,11],[-11,1,10],[-11,2,9],[-11,3,8],[-11,4,7],[-11,5,6],[-10,-4,14],[-10,-2,12],[-10,-1,11],[-10,0,10],[-10,1,9],[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,-5,14],[-9,-4,13],[-9,-2,11],[-9,-1,10],[-9,0,9],[-9,1,8],[-9,2,7],[-9,3,6],[-9,4,5],[-8,-6,14],[-8,-5,13],[-8,-4,12],[-8,-2,10],[-8,-1,9],[-8,0,8],[-8,1,7],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-7,14],[-7,-6,13],[-7,-5,12],[-7,-4,11],[-7,-2,9],[-7,-1,8],[-7,0,7],[-7,1,6],[-7,2,5],[-7,3,4],[-6,-6,12],[-6,-5,11],[-6,-4,10],[-6,-2,8],[-6,-1,7],[-6,0,6],[-6,1,5],[-6,2,4],[-6,3,3],[-5,-5,10],[-5,-4,9],[-5,-2,7],[-5,-1,6],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-4,8],[-4,-2,6],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]])




if __name__ == '__main__':
    unittest.main()