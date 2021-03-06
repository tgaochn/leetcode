# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 01/25/2021, 03:06
# !! Description:

"""
import sys
from typing import List

sys.path.append('..')
sys.path.append('../..')
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
    def maxWeight(self, n, weights, tasks, p):
        """
        0-1背包问题
        直接套用模板即可
        https://www.lintcode.com/problem/efficient-job-processing-service/description

        """
        n = len(weights)
        dp = [[0] * (p + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, p + 1):
                tmp = 0 if j - tasks[i - 1] * 2 < 0 else dp[i - 1][j - tasks[i - 1] * 2] + weights[i - 1]
                dp[i][j] = max(dp[i - 1][j], tmp)

        # printMatrix(dp)
        return dp[-1][-1]
    # endFunc


# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.maxWeight,
        # s.maxWeightRef,
        # s.maximumTotalWeight,
        # optional: add another function for comparison
    ]

    onlyDisplayError = False
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
        4,
        [2, 4, 4, 5],
        [2, 2, 3, 4],
        15,
    )
    expectedRlt[0] = 10

    # ! para2
    # input[1] = parsePara('None')
    input[1] = (
        3,
        [3, 2, 2],
        [3, 2, 2],
        9,
    )
    expectedRlt[1] = 4

    # ! para3
    # input[2] = parsePara('None')
    input[2] = (
        None,
    )
    expectedRlt[2] = None

    # ! para4
    # input[3] = parsePara('None')
    input[3] = (
        None,
    )
    expectedRlt[3] = None

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


# !! ========================== Obsolete Code ==========================

def maxWeightRef(self, n, weights, tasks, p):
    """
    0-1背包问题
    https://www.lintcode.com/problem/efficient-job-processing-service/description
    """
    dp = [[0] * (p // 2 + 1) for i in range(n + 1)]
    for i in range(1, n + 1, 1):
        for j in range(1, p // 2 + 1, 1):
            if (j < tasks[i - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - tasks[i - 1]] + weights[i - 1])
    printMatrix(dp)
    return dp[n][p // 2]
# endFunc

def maximumTotalWeight(self, n, weights, tasks, p):
    items = [[tasks[i] * 2, weights[i]] for i in range(len(tasks))]
    knapsackValues = [[0 for _ in range(p + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        duration, value = items[i - 1]
        for d in range(1, p + 1):
            if duration > d:
                knapsackValues[i][d] = knapsackValues[i - 1][d]
            else:
                knapsackValues[i][d] = max(knapsackValues[i - 1][d], knapsackValues[i - 1][d - duration] + value)
    printMatrix(knapsackValues)
    return knapsackValues[-1][-1]
# endFunc
