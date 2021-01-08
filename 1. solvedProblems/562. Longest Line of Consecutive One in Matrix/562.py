# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 01/06/2021, 20:47
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



# !! step1: replace these two lines with the given code
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """
        DP
        size: 5 * 4 * 3, indexMax -> 5, 4, 3, 即下标顺序倒过来
        a = [[[-1] * 3 for _ in range(4)] for __ in range(5)]
        """
        
        if not M: return 0
        m = len(M)
        n = len(M[0])
        lineCntMatrix = [[[-1] * 4 for _ in range(n)] for __ in range(m)]
        # printMatrix(lineCntMatrix)
        
        def getAllLines(i, j):
            hori = M[i]
            horiCnt = 0
            maxHoriCnt = 0
            for ele in hori:
                if ele == 1:
                    horiCnt += 1
                    maxHoriCnt = max(maxHoriCnt, horiCnt)
                elif ele == 0:
                    horiCnt = 0
            
            vert = [M[idx][j] for idx in range(m)]
            vertCnt = 0
            maxVertCnt = 0
            for ele in vert:
                if ele == 1:
                    vertCnt += 1
                    maxVertCnt = max(maxVertCnt, vertCnt)
                elif ele == 0:
                    vertCnt = 0
            
            dia = []
            if i >= j:
                dia = [M[i - j + idx][idx] for idx in range(min(m, n)) if i - j + idx < m]
            else:
                dia = [M[idx][j - i + idx] for idx in range(min(m, n)) if j - i + idx < n]
            diaCnt = 0
            maxDiaCnt = 0
            for ele in dia:
                if ele == 1:
                    diaCnt += 1
                    maxDiaCnt = max(maxDiaCnt, diaCnt)
                elif ele == 0:
                    diaCnt = 0

            antiDia = []
            if i + j < m:
                antiDia = [M[i + j - idx][idx] for idx in range(min(m, n, i + j)) if i + j - idx < m]
            else:
                antiDia = [M[idx][j + i - idx] for idx in range(min(m, n, i + j)) if j + i - idx < n]
            antiDiaCnt = 0
            maxAntiDiaCnt = 0
            for ele in antiDia:
                if ele == 1:
                    antiDiaCnt += 1
                    maxAntiDiaCnt = max(maxAntiDiaCnt, antiDiaCnt)
                elif ele == 0:
                    antiDiaCnt = 0

            return [maxHoriCnt, maxVertCnt, maxDiaCnt, maxAntiDiaCnt]

        maxLen = -1
        for i in range(m): # 初始化: 标记第一列与最后一列
            oneCntList = getAllLines(i, 0)
            lineCntMatrix[i][0] = oneCntList
            maxLen = max(max(oneCntList), maxLen)

            oneCntList = getAllLines(i, n - 1)
            lineCntMatrix[i][n - 1] = oneCntList
            maxLen = max(max(oneCntList), maxLen)
        
        for j in range(1, n - 1):  # 初始化: 标记第一行
            oneCntList = getAllLines(0, j)
            lineCntMatrix[0][j] = oneCntList
            maxLen = max(max(oneCntList), maxLen)
        
        for i in range(1, m): # 剩下的用DP
            for j in range(1, n - 1):
                horiCnt = lineCntMatrix[i][j - 1][0]
                vertCnt = lineCntMatrix[i - 1][j][1]
                diaCnt = lineCntMatrix[i - 1][j - 1][2]
                antiDiaCnt = lineCntMatrix[i - 1][j + 1][3] if j < n else 0
                lineCntMatrix[i][j] = [horiCnt, vertCnt, diaCnt, antiDiaCnt]
                maxLen = max(max([horiCnt, vertCnt, diaCnt, antiDiaCnt]), maxLen)
        
        # printMatrix(lineCntMatrix)
        # print(getAllLines(0, 1))
        # print(getAllLines(3, 8))
        # print(lineCntMatrix[0][1])
        
        return maxLen
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.longestLine,
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
        [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]],
    )
    expectedRlt[0] = 3

    # ! para2
    # input[1] = parsePara('None')
    input[1] = (
        [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]],
    )
    expectedRlt[1] = 3

    # ! para3
    # input[2] = parsePara('None')
    input[2] = (
        [[0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1],[1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0],[1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1],[0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0],[1,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0],[1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,1],[1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1],[1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1],[1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0],[0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0],[1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1],[1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1],[1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0],[0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0],[1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1],[0,1,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],[1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1],[1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0],[1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1],[1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1],[1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1],[1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1],[0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1],[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,1,1]],
    )
    expectedRlt[2] = 17

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
