# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 12/21/2020, 20:09
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
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        https://leetcode-cn.com/problems/xun-bao/solution/ji-yu-bfsde-zhuang-tai-kong-jian-sou-suo-ji-zhuang/
        经典好题
        这种连通关系不完全的半隐式图问题 都要考虑增加状态变量
        """
        
        from collections import deque
        
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        
        if k >= m + n - 3:
            return m + n - 2
        
        def markVisited(i, j, s):
            for idx in range(s + 1):
                self.visited.add((i, j, idx))
        
        def getNeib(grid, i, j, s):
            neibLis = []
            if i > 0:
                if grid[i - 1][j] == 0:
                    neibLis.append((i - 1, j, s))
                elif s > 0:
                    neibLis.append((i - 1, j, s - 1))
            if i < m - 1:
                if grid[i + 1][j] == 0:
                    neibLis.append((i + 1, j, s))
                elif s > 0:
                    neibLis.append((i + 1, j, s - 1))
            if j > 0:
                if grid[i][j - 1] == 0:
                    neibLis.append((i, j - 1, s))
                elif s > 0:
                    neibLis.append((i, j - 1, s - 1))
            if j < n - 1:
                if grid[i][j + 1] == 0:
                    neibLis.append((i, j + 1, s))
                elif s > 0:
                    neibLis.append((i, j + 1, s - 1))
            return neibLis
                
        self.visited = set()
        myQue = deque([(0, 0, k, 0)])
        while myQue:
            # print(myQue)
            i, j, s, step = myQue.popleft()
            if i == m - 1 and j == n - 1:
                return step
            markVisited(i, j, s)
            # print(self.visited)
            neibLis = getNeib(grid, i, j, s)
            for nextI, nextJ, nextS in neibLis:
                if (nextI, nextJ, nextS) in self.visited: continue
                myQue.append((nextI, nextJ, nextS, step + 1))
        return -1
    # endFunc
        
    def shortestPath1(self, grid: List[List[int]], k: int) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def getNeib(i, j):
            neibLis = []
            if i > 0:
                neibLis.append((i - 1, j))
            if i < m - 1:
                neibLis.append((i + 1, j))
            if j > 0:
                neibLis.append((i, j - 1))
            if j < n - 1:
                neibLis.append((i, j + 1))
            return neibLis
        
        def dfs(i, j, k, visited):
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return 0
            neibLis = getNeib(i, j)
            curRlt = []
            for (nextI, nextJ) in neibLis:
                if (nextI, nextJ) in visited:
                    continue
                if grid[nextI][nextJ] == 1:
                    if k == 0:
                        continue
                    curRlt.append(1 + dfs(nextI, nextJ, k - 1, visited.union({(nextI, nextJ)})))
                else:
                    curRlt.append(1 + dfs(nextI, nextJ, k, visited))
            return float('inf') if not curRlt else min(curRlt)
            
        rlt = dfs(0, 0, k, set())
        return -1 if rlt == float('inf') else rlt
                
            

        pass
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.shortestPath,
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
        [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]],
        1,
    )
    expectedRlt[0] = 6

    # ! para2
    input[1] = (
        [[0, 1, 1],
         [1, 1, 1],
         [1, 0, 0]], 1,
    )
    expectedRlt[1] = -1

    # ! para3
    input[2] = (
        [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0]],
        18,
    )
    expectedRlt[2] = 7

    # ! para4
    input[3] = (
        [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]],
        1,
    )
    expectedRlt[3] = 20

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
