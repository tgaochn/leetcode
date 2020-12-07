# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/30/2020, 01:00
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []

        n = len(nums)
        l, r = 1, n - 1
        i = 0
        rlt = []

        def updateIdx(idx, updateType):
            if updateType == '+':
                idx += 1
                while idx < n - 1 and nums[idx - 1] == nums[idx]:
                    idx += 1
            elif updateType == '-':
                idx -= 1
                while idx > 0 and nums[idx + 1] == nums[idx]:
                    idx -= 1
               
            return idx
        # endFunc

        nums.sort()
        while 1:
            # print(i, l, r)
            if i >= n - 1 or nums[i] > 0:
                break
            if l >= r:
                i += 1
                while nums[i - 1] == nums[i]:
                    i += 1
                    if i >= n - 1:
                        break
                l = i + 1
                r = n - 1
                if l > n - 1:
                    break
                continue

            if nums[i] + nums[l] + nums[r] == 0:
                rlt.append([nums[i], nums[l], nums[r]])
                l = updateIdx(l, '+')
                r = updateIdx(r, '-')
            elif nums[i] + nums[l] + nums[r] < 0:
                l = updateIdx(l, '+')
            elif nums[i] + nums[l] + nums[r] > 0:
                r = updateIdx(r, '-')
        return rlt
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.threeSum,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        [-1, 0, 1, 2, -1, -4]
        # [-2, -3, 0, 0, -2]
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    expectedRlt1 = []

    # ! para2
    input2 = (
        [0, 0, 0]
    )
    enableInput2 = True
    expectedRlt2 = None

    # ! para3
    input3 = (
        [-4, -2, -1]
    )
    enableInput3 = True
    expectedRlt3 = None
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
            if expectedRlt is not None:
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
