# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Thu, 11/12/2020, 21:43
# !! Description:

"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import singleLinkedList
from utils import nTree
from utils.utils import printMatrix

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None

# !! step1: replace these two lines with the given code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        经典DP, dp[i][j] 表示子串 s[i..j] 是否为回文子串, 如果是, 长度多少
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        maxPaliLen = 1
        maxPali = s[0]

        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 0
            if dp[i][i + 1] > maxPaliLen:
                maxPaliLen = 2
                maxPali = s[i:i + 2]

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i + 1, -1):
                dp[i][j] = 0 if s[i] != s[j] or dp[i + 1][j - 1] == 0 else dp[i + 1][j - 1] + 2
                if dp[i][j] > maxPaliLen:
                    maxPaliLen = dp[i][j]
                    maxPali = s[i:j + 1]

        # printMatrix(dp)
        return maxPali
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.longestPalindrome,
    ]

    onlyDisplayError = True
    enableInput1 = False
    enableInput2 = False
    enableInput3 = False
    enableInput4 = False
    enableInput5 = True
    enableInput6 = True

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        "babad"
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt1 = "aba"

    # ! para2
    input2 = (
        # binaryTree.buildTree(None),
        "cbbd"
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt2 = "bb"

    # ! para3
    input3 = (
        "a"
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt3 = "a"

    # ! para4
    input4 = (
        "ac"
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt4 = "a"

    # ! para5
    input5 = (
        "aaaa"
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt5 = "aaaa"

    # ! para6
    input6 = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
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
        inputPara4 = None
        para4Splitter = None

        # start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputPara[1]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputPara[2]
            para3Splitter = '\n' if isOneInstance(inputPara3, specialTypeLis) else '\t'
        if funcParaCnt >= 4:
            inputPara4 = inputPara[3]
            para4Splitter = '\n' if isOneInstance(inputPara4, specialTypeLis) else '\t'

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]
            # print('func: \t%s' % myFunc.__name__)

            # output parameters
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara1)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
            if funcParaCnt == 2:
                rlt = myFunc(inputPara1, inputPara2)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
            if funcParaCnt == 3:
                rlt = myFunc(inputPara1, inputPara2, inputPara3)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
            if funcParaCnt == 4:
                rlt = myFunc(inputPara1, inputPara2, inputPara3, inputPara4)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                print('input4:%s%s' % (para4Splitter, inputPara4))

            # output result
            rltSplitter = '\n' if isOneInstance(rlt, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            if expectedRlt is not None:
                print('expRlt:%s%s' % (rltSplitter, expectedRlt))
            # print('==' * 20)
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
