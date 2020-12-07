# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 10/02/2020, 20:01
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
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if not A or not K: return 0
        n = len(A)
        l, r = 0, 0
        totalCnt = 0
        maxLenLis = []
        maxWinHash = {}
        minLenLis = []
        minWinHash = {}

        def addEle(ele, curHash):
            curHash.setdefault(ele, 0)
            curHash[ele] += 1

        def removeEle(ele, curHash):
            curHash[ele] -= 1
            if curHash[ele] == 0:
                del curHash[ele]  

        while r < n:
            win1 = A[l:r]
            winSize1 = r - l
            if len(maxWinHash) > K:
                removeEle(A[l], maxWinHash)
                l += 1
            elif len(maxWinHash) < K:
                addEle(A[r], maxWinHash)
                maxLenLis.append(0)
                r += 1
            else:
                addEle(A[r], maxWinHash)
                maxLenLis[-1] = max(maxLenLis[-1], winSize1)
                maxLenLis.append(0)
                r += 1
        while l < n:
            if len(maxWinHash) == K:
                maxLenLis[-1] = max(maxLenLis[-1], r - l)
            removeEle(A[l], maxWinHash)
            l += 1
            
        l, r = 0, 0
        while r < n:
            win2 = A[l:r]
            winSize2 = r - l
            if len(minWinHash) > K:
                removeEle(A[l], minWinHash)
                l += 1
            elif len(minWinHash) < K:
                addEle(A[r], minWinHash)
                minLenLis.append(r - (l - 1) + 1)
                r += 1
            else:
                removeEle(A[l], minWinHash)
                minLenLis[-1] = min(minLenLis[-1], winSize2)
                l += 1
        while l < n:
            if len(minWinHash) == K:
                minLenLis[-1] = min(minLenLis[-1], r - l)
            removeEle(A[l], minWinHash)
            l += 1


        # print(maxLenLis)
        # print(minLenLis)
        rlt = 0
        for i in range(n):
            if maxLenLis[i] == 0: continue
            rlt += maxLenLis[i] - minLenLis[i] + 1
        return rlt


    def subarraysWithKDistinct1(self, A: List[int], K: int) -> int:
        """
        two sliding window
        max + min
        """
        if not A or not K: return 0
        n = len(A)
        l, l, r = 0, 0, 0
        totalCnt = 0
        maxLenLis = []
        maxExistHash = {}
        minLenLis = []
        minExistHash = {}


        def addEle(ele, curHash):
            curHash.setdefault(ele, 0)
            curHash[ele] += 1

        def removeEle(ele, curHash):
            curHash[ele] -= 1
            if curHash[ele] == 0:
                del curHash[ele]

        while r < n:
            eleR = A[r]
            addEle(eleR, maxExistHash)
            addEle(eleR, minExistHash)

            while len(maxExistHash) > K:
                eleL = A[l]
                removeEle(eleL, maxExistHash)
                l += 1
            maxLenLis.append(r - l + 1)

            while len(minExistHash) >= K:
                eleL = A[l]
                removeEle(eleL, minExistHash)
                l += 1
            minLenLis.append(r - (l - 1) + 1)

            if r >= K - 1:
                totalCnt += maxLenLis[-1] - minLenLis[-1] + 1

            r += 1
            
        # print(maxLenLis)
        # print(minLenLis)

        return totalCnt
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.subarraysWithKDistinct,
    ]

    # !! step4: change enabled input set
    enableInput1 = True
    enableInput2 = True
    enableInput3 = True
    enableInput4 = True
    enableInput5 = True
    enableInput6 = True

    # !! step3: change input para, input para can be found in "run code" - "test case"

    # ! para1
    input1 = (
        [1, 2, 1, 2, 3],
        2,
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    expectedRlt1 = 7

    # ! para2
    input2 = (
        [2, 2, 1, 2, 2, 2, 1, 1],
        2,
    )
    expectedRlt2 = 23

    # ! para3
    input3 = (
        [2, 2, 1, 2, 3, 2, 1, 1],
        2,
    )
    expectedRlt3 = None

    # ! para4
    input4 = (
        # [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31],
        [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4, 11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18, 49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45, 37, 40, 35, 50, 50, 23, 32, 1, 2],
        # 8,
        20,
    )
    expectedRlt4 = None

    # ! para5
    input5 = (
        [1, 2],
        1,
    )
    expectedRlt5 = 2

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
