# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/30/2020, 23:54
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
    def minWindow(self, s: str, t: str) -> str:
        """
        formatted sliding window
        """

        n1, n2 = len(s), len(t)
        l, r = 0, 0
        existHash = {}
        minLen = float('inf')
        minLenString = ''
        tCharFreqHash = {}
        for curChar in t:
            tCharFreqHash.setdefault(curChar, 0)
            tCharFreqHash[curChar] += 1
            

        def isCover():
            for curChar, freq in tCharFreqHash.items():
                if existHash.get(curChar, 0) < freq:
                    return False
            return True

        while r < n1:
            eleR = s[r]
            existHash.setdefault(eleR, 0)
            existHash[eleR] += 1

            while isCover():
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    minLenString = s[l: r + 1]

                eleL = s[l]
                existHash[eleL] -= 1
                if existHash[eleL] == 0:
                    del existHash[eleL]

                l += 1
            r += 1

        return minLenString

    def minWindow1(self, s: str, t: str) -> str:
        from copy import deepcopy
        if not s or len(s) < len(t): return ""
        n = len(s)
        l, r = 0, 0
        existHash = {}
        curLen, minLen = 0, float('inf')
        minLenStr = ""

        def isCharContained(myStr):
            myDict = deepcopy(existHash)

            for c in myStr:
                if c not in myDict or myDict[c] == 0:
                    return False
                myDict[c] -= 1
            return True

        while r < n:
            eleR = s[r]
            existHash.setdefault(eleR, 0)
            existHash[eleR] += 1
            curLen += 1
            r += 1

            while isCharContained(t):
                eleL = s[l]
                if curLen < minLen:
                    minLen = curLen
                    minLenStr = s[l:r]
                existHash[eleL] -= 1
                curLen -= 1
                l += 1

        return minLenStr
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.minWindow,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        "ADOBECODEBANC",
        "ABC",
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = False
    expectedRlt1 = None

    # ! para2
    input2 = (
        "a",
        "aa",
    )
    enableInput2 = False
    expectedRlt2 = None

    # ! para3
    input3 = (
        "aa",
        "aa",
    )
    enableInput3 = False
    expectedRlt3 = None

    # ! para4
    input4 = (
        "bbaa",
        "aba",
    )
    enableInput4 = True
    expectedRlt4 = None

    # ! para5
    input5 = (
        "acbbaca",
        "aba",
    )
    enableInput5 = False
    expectedRlt5 = None

    # ! para
    input6 = (
        "cwaefgcf",
        "cae",
    )
    enableInput6 = True
    expectedRlt6 = "cwae"
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
