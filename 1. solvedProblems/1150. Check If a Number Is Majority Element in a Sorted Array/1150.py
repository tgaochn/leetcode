# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/30/2020, 18:19
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
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        def isBound(i, boundType):
            if boundType == 'l':
                return i <= 0 or (nums[i - 1] < nums[i] and nums[i + 1] == nums[i])
            if boundType == 'r':
                return i >= n - 1 or (nums[i + 1] > nums[i] and nums[i - 1] == nums[i])
        
        def bs(l, r, boundType):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    if isBound(m, boundType):
                        return m
                    else:
                        if boundType == 'l':
                            r = m - 1
                        else:
                            l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        
        l, r = 0, n - 1
        m = l + (r - l) //2
        if nums[m] != target:
            return False
        else:
            lBound = bs(l, m, 'l')
            rBound = bs(m, r, 'r')
            # print(nums[l: m + 1])
            # print(nums[m: r + 1])
            # print(lBound, rBound)
            cnt = rBound - lBound + 1
            return cnt > n / 2
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.isMajorityElement,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        [2, 4, 5, 5, 5, 5, 5, 6, 6],
        5,
        # singleLinkedList.buildSingleList([]),
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    expectedRlt1 = None

    # ! para2
    input2 = (
        [2, 5, 5],
        5,
    )
    enableInput2 = True
    expectedRlt2 = True

    # ! para3
    input3 = (
        None
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
