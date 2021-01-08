# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 09/27/2020, 23:39
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
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        固定长度滑动窗口
        中间sliding window 当做不选的牌
        """
        from collections import deque
        
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        
        l, r = 0, 0
        win = deque()
        winSum = 0
        minWinSum = float('inf')
        
        while r < n:
            # print(win, winSum)
            if len(win) < n - k:
                win.append(cardPoints[r])
                winSum += cardPoints[r]
                r += 1
                if len(win) == n - k:
                    winSum = sum(win)
                    minWinSum = min(winSum, minWinSum)
            else:
                eleL = win.popleft()
                win.append(cardPoints[r])
                winSum = winSum - eleL + cardPoints[r]
                minWinSum = min(winSum, minWinSum)
                l += 1
                r += 1
        
        minWinSum = min(sum(win), minWinSum)
        return sum(cardPoints) - minWinSum
    # endFunc  
        
    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        """
        不是普通的sliding window, 抽卡的id可以是[0, 1, -1]
        所以每次从正向list中去掉最后一位, 增加反向list的一位
        """
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        mySum = sum(cardPoints[:k])
        maxSum = mySum
        for i in range(1, k + 1):
            mySum = mySum - cardPoints[k - i] + cardPoints[-i]
            maxSum = max(maxSum, mySum)

        return maxSum
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.maxScore,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        [100, 40, 17, 9, 73, 75],
        3,
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    expectedRlt1 = 248

    # ! para2
    input2 = (
        [1, 1000, 1],
        1,
    )
    enableInput2 = True
    expectedRlt2 = None

    # ! para3
    input3 = (
        [1, 2, 3, 4, 5, 6, 1],
        3,
    )
    enableInput3 = True
    expectedRlt3 = 12
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
            if expectedRlt:
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
