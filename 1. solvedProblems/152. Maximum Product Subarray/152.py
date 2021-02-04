# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 01/18/2021, 16:16
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
    def maxProduct(self, nums: List[int]) -> int:
        """
        标准DP - 两个一维DP
        不知道win要缩还是要扩, 不能用 sliding window
        和53很像
        https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
        考虑到负数, 要注意做乘法要同时找max和min

        DP[i] - nums[0: i - 1]中的Maximum Product Subarray
        """

        n = len(nums)
        dpMax = [0] * n
        dpMin = [0] * n
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        maxProd = nums[0]

        for i in range(1, n):
            dpMax[i] = max(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])
            dpMin[i] = min(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])
            maxProd = max(maxProd, dpMax[i])

        return maxProd

    def maxProduct1(self, nums: List[int]) -> int:
        """
        非标准DP
        不知道win要缩还是要扩, 不能用 sliding window
        和53很像
        https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
        考虑到负数, 要注意做乘法要同时找max和min
        """

        n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]
        preMax = nums[0]
        preMin = nums[0]
        maxProd = preMax

        for i in range(1, n):
            # dp[i] = max(dp[i - 1] * nums[i], nums[i])
            # preMax = max(preMax, dp[i])
            curMax = max(preMax * nums[i], preMin * nums[i], nums[i])
            curMin = min(preMax * nums[i], preMin * nums[i], nums[i])
            maxProd = max(maxProd, curMax)
            preMax = curMax
            preMin = curMin

        return maxProd
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.maxProduct,
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
        [2, 3, -2, 4],
    )
    expectedRlt[0] = 6

    # ! para2
    # input[1] = parsePara('Input: [-2,0,-1]')
    input[1] = (
        [-2, 0, -1],
    )
    expectedRlt[1] = 0

    # ! para3
    # input[2] = parsePara('None')
    input[2] = (
        [-2, 3, -4],
    )
    expectedRlt[2] = 24

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
