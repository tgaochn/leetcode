# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/30/2020, 23:09
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
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        formatted sliding window for longest string
        new template for longest string
        """
        if not s: return 0

        n = len(s)
        l, r = 0, 0
        existHash = {}
        maxLen = 0

        while r < n:
            eleR = s[r]
            existHash.setdefault(eleR, 0)
            existHash[eleR] += 1

            while len(existHash) > 2:
                eleL = s[l]
                existHash[eleL] -= 1
                if existHash[eleL] == 0:
                    del existHash[eleL]
                l += 1
            if len(existHash) == 2:
                maxLen = max(maxLen, r - l + 1)

            r += 1
        return maxLen

    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        """
        formatted sliding window
        """
        if not s: return 0

        n = len(s)
        l, r = 0, 0
        existHash = {}
        maxLen = 0

        while r < n:
            eleR = s[r]
            existHash.setdefault(eleR, 0)
            existHash[eleR] += 1

            if len(existHash) <= 2:
                maxLen = max(maxLen, r - l + 1)
            else:
                while len(existHash) > 2:
                    eleL = s[l]
                    existHash[eleL] -= 1
                    if existHash[eleL] == 0:
                        del existHash[eleL]
                    l += 1
            r += 1
        return maxLen

    def lengthOfLongestSubstringTwoDistinct1(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        l, r = 0, 0
        existEle = {}
        maxLen = 0
        curLen = 0
        availCnt = 2

        while r < n:
            eleR = s[r]
            existEle.setdefault(eleR, 0)
            if existEle[eleR] == 0:
                availCnt -= 1
            existEle[eleR] += 1
            r += 1
            curLen += 1
            if availCnt >= 0:
                maxLen = max(maxLen, curLen)
            else:
                while availCnt < 0:
                    eleL = s[l]
                    existEle[eleL] -= 1
                    if existEle[eleL] == 0:
                        availCnt += 1
                    l += 1
                    curLen -= 1

        return maxLen
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.lengthOfLongestSubstringTwoDistinct,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        # "eceba"
        "abcabcabc"
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    # expectedRlt1 = None
    expectedRlt1 = 2

    # ! para2
    input2 = (
        "bacc"
    )
    enableInput2 = True
    expectedRlt2 = 3

    # ! para3
    input3 = (
        "abaccc"
    )
    enableInput3 = True
    expectedRlt3 = 4
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
