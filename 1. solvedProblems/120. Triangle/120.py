# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 09/06/2020, 23:21
# !! Description:

"""
from typing import List
import sys
sys.path.append('..')
from utils import utils
from utils import binaryTree
from utils import singleLinkedList
from utils import nTree

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None

# !! step1: replace these two lines with the given code
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        DP from top to bottom
        三角形翻转, 很多入口但只有一个出口, 结果和原题一样都只有一条最短路径
        """
        n = len(triangle)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        triangle.reverse()
        dp[0] = triangle[0]
        for i in range(1, n):
            for j in range(n):
                if j <= n - i - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + triangle[i][j]

        return dp[n-1][0]
    # endFunc

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """
        DP from bottom to top
        """
        n = len(triangle)

        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[1][0] + dp[0][0]

        for i in range(0, n):
            for j in range(0, n):
                if j == 0 and i in (0, 1):
                    continue

                if i == j:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif i > j:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[n - 1])
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name and para here
    # !! input para can be found in "run code" - "test case"
    myFuncLis = [
        s.minimumTotal,
    ]
    inputParaLis1 = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        # [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9], [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0], [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5], [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]],
        # [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5]],
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    ]
    inputParaLis2 = [
        None,
    ]
    inputParaLis3 = [
        None,
    ]
    # !! ====================================

    # ! instances that need an extra empty line
    specialTypeLis = [TreeNode, Node]

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
        para1Splitter = '\n' if isOneInstance(inputPara1, specialTypeLis) else '\t'
        inputPara2 = None
        para2Splitter = None
        inputPara3 = None
        para3Splitter = None

        # ! start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputParaLis2[i]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputParaLis3[i]
            para3Splitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'

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
            rltSplitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
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
