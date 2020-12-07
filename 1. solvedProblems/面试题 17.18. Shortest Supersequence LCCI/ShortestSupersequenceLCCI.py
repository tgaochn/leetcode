# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 10/02/2020, 23:12
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
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        nb, ns = len(big), len(small)
        l, r = 0, 0
        coverHash = {}
        shortCharSet = set(small)
        minLen = float('inf')
        minLenIdx = []

        def isCover():
            for ele in shortCharSet:
                if ele not in coverHash:
                    return False
            return True

        while r < nb:
            eleR = big[r]
            coverHash.setdefault(eleR, 0)
            coverHash[eleR] += 1

            while isCover():
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minLenIdx = [l, r]
                eleL = big[l]
                coverHash[eleL] -= 1
                if coverHash[eleL] == 0:
                    del coverHash[eleL]
                l += 1
            r += 1
        return minLenIdx
    # endFunc
# endClass

def func():
    enableInput1 = True
    enableInput2 = True
    enableInput3 = True
    enableInput4 = True
    enableInput5 = True
    enableInput6 = True

    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.shortestSeq,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"

    # ! para1
    input1 = (
        [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7],
        [1, 5, 9],
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    expectedRlt1 = None

    # ! para2
    input2 = (
        None
    )
    expectedRlt2 = None

    # ! para3
    input3 = (
        None
    )
    expectedRlt3 = None

    # ! para4
    input4 = (
        None
    )
    expectedRlt4 = None

    # ! para5
    input5 = (
        None
    )
    expectedRlt5 = None

    # ! para6
    input6 = (
        None
    )
    expectedRlt6 = None
    # !! ====================================

    # instances that need an extra empty line
    specialTypeLis = [TreeNode, Node]

    # function and parameters count
    allInput = [
        (input1, enableInput1, expectedRlt1),
        (input2, enableInput2, expectedRlt2),
        (input3, enableInput3, expectedRlt3),
        (input4, enableInput4, expectedRlt4),
        (input5, enableInput5, expectedRlt5),
        (input6, enableInput6, expectedRlt6),
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
