# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 08/29/2020, 23:39
# !! Description:
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        lastEle = None
        eleCnt = 0
        numCnt = len(nums)
        for idx in range(numCnt):
            ele = nums[idx]
            if ele != lastEle:
                if not lastEle is None:
                    nums[eleCnt] = ele
                lastEle = ele
                eleCnt += 1
            # else:
                # nums[idx - 1] = lastEle
        # print (nums)
        return eleCnt
# end_class

def func():
    s = Solution()

    inputParaLis1 = [
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        # [0, 0, 1, 1],
        # [1, 1, 2],
        ]
    # inputParaLis2 = []
    # inputParaLis3 = []
    myFuncLis = [
        s.removeDuplicates,
    ]

    paraCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    for i in range(paraCnt):
        inputPara1 = inputParaLis1[i]
        # inputPara2 = inputParaLis2[i]
        # inputPara3 = inputParaLis3[i]

        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            print('input1:\t%s' % inputPara1)
            # print('input2: %s' % inputPara2)
            # print('input3: %s' % inputPara3)
            
            rlt = myFunc(inputPara1)
            print('rlt: \t%s' % rlt)
            print('==' * 20)

# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
