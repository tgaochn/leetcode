# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 12/21/2020, 19:03
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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/zhi-jie-tao-yong-tuo-bu-pai-xu-mo-ban-mei-you-ji-q/
        topo sorting, 从入度为0的pos开始找
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])

        def getNext(i, j):
            nextPosLis = []
            curEle = matrix[i][j]
            if i > 0 and curEle < matrix[i - 1][j]:
                nextPosLis.append((i - 1, j))
            if i < m - 1 and curEle < matrix[i + 1][j]:
                nextPosLis.append((i + 1, j))
            if j > 0 and curEle < matrix[i][j - 1]:
                nextPosLis.append((i, j - 1))
            if j < n - 1 and curEle < matrix[i][j + 1]:
                nextPosLis.append((i, j + 1))
            return nextPosLis

        inDegreeHash = {}
        adjHash = {}
        for i in range(m):
            for j in range(n):
                inDegreeHash.setdefault((i, j), 0)
                nextPosLis = getNext(i, j)
                for nextI, nextJ in nextPosLis:
                    inDegreeHash.setdefault((nextI, nextJ), 0)
                    inDegreeHash[(nextI, nextJ)] += 1
                adjHash[(i, j)] = nextPosLis
        
        self.maxPathLen = 0
        inDegreeZeroLis = [pos for pos, inDegree in inDegreeHash.items() if inDegree == 0]
        # self.maxPathLenHash = {}

        # printDict(inDegreeHash)
        # print('==')
        # printDict(adjHash)
        # print('==')
        # print(inDegreeZeroLis)
        # print('==')

        def dfs(curPos, curPathLen, path):
            if not adjHash.get(curPos, []):
                self.maxPathLen = max(self.maxPathLen, curPathLen)
                # self.maxPathLenHash[curPos] = 1
                # print(path)
            
            for nextPos in adjHash[curPos]:
                dfs(nextPos, curPathLen + 1, path + [nextPos])
        
        for inDegreeZeroPos in inDegreeZeroLis:
            dfs(inDegreeZeroPos, 1, [inDegreeZeroPos])
        
        return self.maxPathLen

        
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        """
        DFS
        """
        
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])
        self.pathLenHash = {}
        
        def getNeib(i, j):
            neibLis = []
            if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
                neibLis.append((i + 1, j))
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                neibLis.append((i - 1, j))
            if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
                neibLis.append((i, j + 1))
            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                neibLis.append((i, j - 1))
            return neibLis

        def dfs(i, j):
            if (i, j) in self.pathLenHash:
                return self.pathLenHash[(i, j)]

            neibLis = getNeib(i, j)
            if not neibLis:
                self.pathLenHash[(i, j)] = 1
                return 1
            
            maxLen = 1 + max([dfs(nextI, nextJ) for nextI, nextJ in neibLis])
            self.pathLenHash[(i, j)] = maxLen
            
            return maxLen
            
        maxLen = 0
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, dfs(i, j))
                
        return maxLen
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.longestIncreasingPath,
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
    input[0] = (
        [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
    )
    expectedRlt[0] = 4

    # ! para2
    input[1] = (
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ],
    )
    expectedRlt[1] = 4

    # ! para3
    input[2] = (
        None,
    )
    expectedRlt[2] = None

    # ! para4
    input[3] = (
        None,
    )
    expectedRlt[3] = None

    # ! para5
    input[4] = (
        None
    )
    expectedRlt[4] = None

    # ! para6
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
