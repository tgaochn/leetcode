# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 01/18/2021, 20:41
# !! Description:

"""
import sys
from typing import List

sys.path.append('..')
from utils import binaryTree, nTree, singleLinkedList
from utils.utils import (
    printMatrix,
    printDict,
    printList,
    isMatrix,
    parsePara,
)

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None
testCaseCnt = 6
# maxFuncInputParaCnt = 8
true = True
false = False

# !! step1: replace these two lines with the given code
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        ref -> 715
        增加区间, 可以直接参考终极题目715
        """
        if not intervals: return [newInterval]
        
        n = len(intervals)
        l = 0
        left = newInterval[0]
        right = newInterval[1]
        
        while l < n and left > intervals[l][1]:
            l += 1
        
        if l == n:
            return intervals + [newInterval]

        r = l
        while r < n and right >= intervals[r][0]:
            r += 1
        
        if r == 0:
            return [newInterval] + intervals
        
        r -= 1
        left = min(left, intervals[l][0])
        right = max(right, intervals[r][1])
        return intervals[:l] + [[left, right]] + intervals[r + 1:]
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.insert,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    # enableInput[0] = False
    # enableInput[1] = False
    # enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    # input[0] = parsePara('None')
    input[0] = (
        [[1, 3], [6, 9]],
        [2, 5],
    )
    expectedRlt[0] = [[1, 5], [6, 9]]

    # ! para2
    input[1] = parsePara('intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]')
    # input[1] = (
        # [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
    # )
    expectedRlt[1] = [[1, 2], [3, 10], [12, 16]]

    # ! para3
    input[2] = parsePara('intervals = [], newInterval = [5,7]')
    # input[2] = (
        # None,
    # )
    expectedRlt[2] = [[5, 7]]

    # ! para4
    # input[3] = parsePara('None')
    input[3] = (
        [[1, 5]],
        [6, 8],
    )
    expectedRlt[3] = [[1, 5], [6, 8]]

    # ! para5
    # input[4] = parsePara('None')
    input[4] = (
        None
    )
    expectedRlt[4] = None

    # ! para6
    # input[5] = parsePara('None')
    input[5] = (
        None
    )
    expectedRlt[5] = None
    # !! ====================================

    # function and parameters count
    allInput = [(input[i], enableInput[i], expectedRlt[i]) for i in range(testCaseCnt)]
    if not input[0]:
        print("ERROR: please assign at least one input for input[0]!")
        exit()
    funcParaCnt = 1 if not isinstance(input[0], tuple) else len(input[0])
    funcCnt = len(myFuncLis)

    # for each test case
    for inputPara, enableInput, expectedRlt in allInput:
        if not enableInput or not inputPara or (isinstance(inputPara, tuple) and not inputPara[0]): continue
        inputParaList = [None] * funcParaCnt

        if not isinstance(inputPara, tuple):
            inputPara = [inputPara]

        for j in range(funcParaCnt):
            inputParaList[j] = inputPara[j]

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]

            # ! manually call function, max para count: 8
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara[0])
            if funcParaCnt == 2:
                rlt = myFunc(inputPara[0], inputPara[1])
            if funcParaCnt == 3:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2])
            if funcParaCnt == 4:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3])
            if funcParaCnt == 5:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4])
            if funcParaCnt == 6:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5])
            if funcParaCnt == 7:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6])
            if funcParaCnt == 8:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6], inputPara[7])

            # only output when the result is not expected
            if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue

            # output function name
            if funcCnt > 1:
                print('func: \t%s' % myFunc.__name__)

            # output para
            for k in range(funcParaCnt):
                para = inputParaList[k]
                if para:
                    formatPrint('input %s:' % (k + 1), para)
                else:
                    print(para)

            # output result
            print()
            if not rlt:
                print('rlt:\t', rlt)
            else:
                formatPrint('rlt:', rlt)
            if expectedRlt is not None:
                if not expectedRlt:
                    print('expRlt:\t', expectedRlt)
                else:
                    formatPrint('expRlt:', expectedRlt)
    print('==' * 20)
# endFunc

def isSpecialInstance(myInstance):
    for curType in [TreeNode, Node]:
        if isinstance(myInstance, curType):
            return True
    return False
# endFunc

def formatPrint(prefix, data):
    if isMatrix(data):
        print('%s' % prefix)
        printMatrix(data)
    else:
        splitter = '\n' if isSpecialInstance(data) else '\t'
        print('%s%s%s' % (prefix, splitter, data))
# endFunc

def main():
    func()
# endMain


if __name__ == "__main__":
    main()
# endIf
