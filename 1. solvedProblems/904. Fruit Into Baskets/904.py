# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Thu, 10/01/2020, 01:55
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
    def totalFruit(self, tree: List[int]) -> int:
        if not tree: return 0
        n = len(tree)
        l, r = 0, 0
        existHash = {}
        curLen, maxLen = 0, -float('inf')

        while r < n:
            eleR = tree[r]
            existHash.setdefault(eleR, 0)
            existHash[eleR] += 1
            curLen += 1
            if len(existHash) <= 2:
                maxLen = max(maxLen, curLen)
            r += 1
            while len(existHash) > 2 :
                eleL = tree[l]
                existHash[eleL] -= 1
                if existHash[eleL] == 0:
                    del existHash[eleL]
                curLen -= 1
                l += 1
        
        return maxLen
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.totalFruit,
    ]

    # !! step4: change enabled input set
    enableInput1 = False
    enableInput2 = False
    enableInput3 = True
    enableInput4 = False
    enableInput5 = False
    enableInput6 = False

    # !! step3: change input para, input para can be found in "run code" - "test case"

    # ! para1
    input1 = (
        [1, 2, 1]
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    expectedRlt1 = None

    # ! para2
    input2 = (
        [0, 1, 2, 2]
    )
    expectedRlt2 = None

    # ! para3
    input3 = (
        [3,3,3,1,2,1,1,2,3,3,4]
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
