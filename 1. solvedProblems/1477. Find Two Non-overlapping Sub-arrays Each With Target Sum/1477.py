# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 12/18/2020, 18:30
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
)

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None
testCaseCnt = 6
# maxFuncInputParaCnt = 8

# !! step1: replace these two lines with the given code
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solution/java-hua-dong-chuang-kou-dong-tai-gui-hua-er-fen-b/
        https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solution/hua-dong-chuang-kou-te-shu-testcase-you-hua-dong-t/
        1. 滑动窗口找到所有备选区间
        2. 用dp
        minWinList[i] 表示以i为起点的最小winLen, 有点像preSum
        dp[i] 表示从第 i 个起往后，最小的最小winLen
        O(n)
        PS:
        还是超时...
        不过已经是O(n)了, 再优化也没意义了...
        就这样吧
        """
        from collections import deque

        # sliding window to find all the subarray
        n = len(arr)
        l, r = 0, 0
        win = deque()
        allWin = []
        winSum = 0
        while r < n:
            if not win or winSum < target:
                win.append(arr[r])
                winSum += arr[r]
                r += 1
            elif winSum > target:
                popEle = win.popleft()
                winSum -= popEle
                l += 1
            else:
                shortestRlt = None
                while winSum == target:
                    shortestRlt = (l, r, list(win))
                    popEle = win.popleft()
                    winSum -= popEle
                    l += 1
                allWin.append(shortestRlt)
        shortestRlt = None
        while winSum >= target:
            shortestRlt = (l, r, list(win))
            popEle = win.popleft()
            winSum -= popEle
            l += 1
        if shortestRlt and sum(shortestRlt[2]) == target:
            allWin.append(shortestRlt)

        # print(allWin)
        m = len(allWin)
        if m <= 1:
            return -1

        minWinList = [float('inf')] * n  # minWinList[i] 表示以i为起点的最小winLen, 有点像preSum
        for s, e, win in allWin:
            winLen = e - s
            if minWinList[s] > winLen:
                minWinList[s] = winLen

        # print(minWinList)
        dp = [float('inf')] * n  # dp[i] 表示从第 i 个起往后，最小的最小winLen
        dp[-1] = minWinList[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i + 1], minWinList[i])

        # print(dp)
        minLenSum = float('inf')
        for i in range(n):  # 遍历一遍minWinList再找对应的dp值即可, 有点像twoSum
            winLen1 = minWinList[i]
            if i + winLen1 >= n: continue
            winLen2 = dp[i + winLen1]
            if minLenSum > winLen1 + winLen2:
                minLenSum = winLen1 + winLen2

        return minLenSum if minLenSum != float('inf') else -1

    def minSumOfLengths1(self, arr: List[int], target: int) -> int:
        """
        https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solution/java-hua-dong-chuang-kou-dong-tai-gui-hua-er-fen-b/
        1. 滑动窗口找到所有区间
        2. 双循环找两个区间
        最差情况 O(n^2)
        """
        from collections import deque

        # sliding window to find all the subarray
        n = len(arr)
        l, r = 0, 0
        win = deque()
        allWin = []
        while r < n:
            if not win or sum(win) < target:
                win.append(arr[r])
                r += 1
            elif sum(win) > target:
                win.popleft()
                l += 1
            else:
                shortestRlt = None
                while sum(win) == target:
                    shortestRlt = (l, r, list(win))
                    win.popleft()
                    l += 1
                allWin.append(shortestRlt)
        shortestRlt = None
        while sum(win) >= target:
            shortestRlt = (l, r, list(win))
            win.popleft()
            l += 1
        if shortestRlt and sum(shortestRlt[2]) == target:
            allWin.append(shortestRlt)

        print(allWin)

        # loop to find the 2 min range
        n = len(allWin)
        if n <= 1:
            return -1
        minLen1 = float('inf')
        minLen2 = float('inf')
        for s, e, win in allWin:
            winLen = e - s
            if winLen < minLen1:
                winLen2 = minLen1
                minLen1 = winLen
            elif winLen < minLen2:
                minLen2 = winLen

        print(minLen1, minLen2)
        minLenSum = float('inf')
        for i in range(n):
            s1, e1, win1 = allWin[i]
            winLen1 = e1 - s1
            for j in range(i + 1, n):
                s2, e2, win2 = allWin[j]
                winLen2 = e2 - s2
                if minLenSum == minLen1 + minLen2 and minLenSum != float('inf'):  # 提前返回条件, 否则超时
                    return minLenSum
                if s2 >= e1 and winLen1 + winLen2 < minLenSum:
                    minLenSum = winLen1 + winLen2

        return minLenSum if minLenSum != float('inf') else -1
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.minSumOfLengths,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    enableInput[0] = False
    # enableInput[1] = False
    enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input[0] = (
        [3, 2, 2, 4, 3],
        3,
        # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),
    )
    expectedRlt[0] = 2

    # ! para2
    input[1] = (
        [7, 3, 4, 7],
        7,
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = None

    # ! para3
    input[2] = (
        [4, 3, 2, 6, 2, 3, 4],
        6,
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[2] = None

    # ! para4
    input[3] = (
        [1] * 10,
        4,
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[3] = None

    # ! para5
    input[4] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[4] = None

    # ! para6
    input[5] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
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
