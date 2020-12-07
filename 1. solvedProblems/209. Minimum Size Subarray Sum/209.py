# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 09/27/2020, 20:24
# !! Description:

"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import singleLinkedList
from utils import nTree

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None

# !! step1: replace these two lines with the given code
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        sliding window for shortest string
        new template for shortest string
        """

        l, r = 0, 0
        n = len(nums)
        minLen = float('inf')
        mySum = 0

        while r < n:
            mySum += nums[r]
            while mySum >= s:
                mySum -= nums[l]
                l += 1
            
            if l > 0 and mySum + nums[l - 1] >= s:
                minLen = min(minLen, r - (l - 1) + 1)

            r += 1

        return minLen if minLen != float('inf') else 0

    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        """
        sliding window
        """

        l, r = 0, 0
        n = len(nums)
        minLen = float('inf')
        mySum = 0

        while r < n:
            mySum += nums[r]
            while mySum >= s:
                minLen = min(minLen, r - l + 1)
                mySum -= nums[l]
                l += 1
            r += 1

        return minLen if minLen != float('inf') else 0
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.minSubArrayLen,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        # 213,
        # [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12],

        7,
        [2, 3, 1, 2, 4, 3],

        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = False
    expectedRlt1 = 2

    # ! para2
    input2 = (
        4,
        [1, 4, 4],
    )
    enableInput2 = False
    expectedRlt2 = 1

    # ! para3
    input3 = (
        11,
        [1, 2, 3, 4, 5],
    )
    enableInput3 = True
    expectedRlt3 = 3
    # !! ====================================

    # instances that need an extra empty line
    specialTypeLis = [TreeNode, Node]

    # function and parameters count
    allInput = [
        (input1, enableInput1, expectedRlt1),
        (input2, enableInput2, expectedRlt2),
        (input3, enableInput3, expectedRlt3),
    ]
    if not input1 and not input2:
        print("ERROR: please assign at least one input for input1 or input2!")
        exit()
    funcParaCnt = 1 if not isinstance(input1, tuple) else len(input1)
    funcCnt = len(myFuncLis)

    # for each input set
    for inputPara, enableInput, expectedRlt in allInput:
        if not enableInput or not inputPara: continue
        inputPara1 = inputPara if not isinstance(inputPara, tuple) else inputPara[0]
        para1Splitter = '\n' if isOneInstance(inputPara1, specialTypeLis) else '\t'
        inputPara2 = None
        para2Splitter = None
        inputPara3 = None
        para3Splitter = None

        # start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputPara[1]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputPara[2]
            para3Splitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'

        # for each function
        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            # output parameters
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

            # output result
            rltSplitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            if expectedRlt:
                print('expRlt:%s%s' % (rltSplitter, expectedRlt))
            print('==' * 20)
# endFunc

def isOneInstance(myInstance, typeLis):
    for curType in typeLis:
        if isinstance(myInstance, curType):
            return True
    return False
# endFunc

def main():
    func()
# endMain


if __name__ == "__main__":
    main()
# endIf
