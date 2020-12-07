# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Xuan Dai (xdai@huskers.unl.edu)
CreationDate:
    Thu, 09/03/2020, 00:17
# !! Description:

"""
from typing import List
import sys
sys.path.append('..')

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            dict[index] = num
        for i, num in dict.items:
            if dict[i]+dict[j]=target:
                return [i,j]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        i=0 
             
        while i < len(nums)-1:
            addend=target-nums[i]
            j=i+1
            while j < len(nums):
                print ([i,j])
                if addend==nums[j]:
                    
                    return [i,j]
                else:
                    j+=1
            i+=1

# end_class

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.twoSum,
    ]
    inputParaLis1 = [
        [2, 7, 11, 15],
    ]
    inputParaLis2 = [
        9,
    ]
    inputParaLis3 = [
        None,
    ]
    # !! ====================================

    # ! function and parameters count
    inputSetCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    funcParaCnt = 1
    if not inputParaLis3[0] is None:
        funcParaCnt = 3
    elif not inputParaLis2[0] is None:
        funcParaCnt = 2

    # ! for each input set
    for i in range(inputSetCnt):
        inputPara1 = inputParaLis1[i]
        para1Splitter = '\t'
        inputPara2 = None
        para2Splitter = None
        inputPara3 = None
        para3Splitter = None

        # ! start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputParaLis2[i]
            para2Splitter = '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputParaLis3[i]
            para3Splitter = '\t'

        # ! for each function
        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            # ! output parameters
            if funcParaCnt == 1:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                rlt = myFunc(inputPara1)
            if funcParaCnt == 2:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                rlt = myFunc(inputPara1, inputPara2)
            if funcParaCnt == 3:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                rlt = myFunc(inputPara1, inputPara2, inputPara3)

            # ! output result
            rltSplitter = '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            print('==' * 20)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
