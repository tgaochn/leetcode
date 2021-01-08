# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 01/04/2021, 02:43
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

import bisect

# !! step1: replace these two lines with the given code
class RangeModule:
    """
    https://zhuanlan.zhihu.com/p/330875328
    暴力解法
    
    改进的话可以加入二分法
    """

    def __init__(self):
        self.allRange = []
        self.n = 0
        self.allLeft = []
        self.allRight = []

    def addRange(self, left: int, right: int) -> None:
        if not self.allRange:
            self.allRange = [(left, right)]
            return
        
        l = 0
        n = len(self.allRange)
        # n = self.n
        while l < n and left > self.allRange[l][1]:
            l += 1

        if l == n:
            self.allRange = self.allRange + [(left, right)]
            return
        
        r = l
        while r < n and right >= self.allRange[r][0]:
            r += 1
        
        if r == 0:
            self.allRange = [(left, right)] + self.allRange
            return 

        r -= 1
        left = min(left, self.allRange[l][0])
        right = max(right, self.allRange[r][1])
        self.allRange = self.allRange[:l] + [(left, right)] + self.allRange[r + 1:]

        # self.allLeft = []
        # self.allRight = []
        # self.n = len(self.allRange)
        # for i in range(self.n):
        #     rangeLeft = self.allRange[i][0]
        #     rangeRight = self.allRange[i][1]
        #     self.allLeft.append(rangeLeft)
        #     self.allRight.append(rangeRight)
        # print(self.allRange)

    def queryRange(self, left: int, right: int) -> bool:
        """
        暴力解法
        """
        n = len(self.allRange)
        for i in range(n):
            if self.allRange[i][0] <= left and right <= self.allRange[i][1]:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        if not self.allRange:
            return
        
        l = 0
        n = len(self.allRange)
        # n = self.n
        while l < n and left >= self.allRange[l][1]:
            l += 1

        if l == n:
            return

        r = l
        while r < n and right > self.allRange[r][0]:
            r += 1

        if r == 0:
            return

        r -= 1
        tmp = []
        if left > self.allRange[l][0]:
            tmp.append((self.allRange[l][0], left))
        if right < self.allRange[r][1]:
            tmp.append((right, self.allRange[r][1]))
        self.allRange = self.allRange[:l] + tmp + self.allRange[r + 1:]

        # self.allLeft = []
        # self.allRight = []
        # self.n = len(self.allRange)
        # for i in range(self.n):
        #     rangeLeft = self.allRange[i][0]
        #     rangeRight = self.allRange[i][1]
        #     self.allLeft.append(rangeLeft)
        #     self.allRight.append(rangeRight)
    # endFunc
# endClass

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.TODO,
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
    input[0] = parsePara('None')
    # input[0] = (
        # None,
    # )
    expectedRlt[0] = None

    # ! para2
    input[1] = parsePara('None')
    # input[1] = (
        # None,
    # )
    expectedRlt[1] = None

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
