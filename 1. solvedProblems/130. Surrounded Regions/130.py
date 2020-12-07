# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 12/05/2020, 18:06
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
    def solve(self, board: List[List[str]]) -> None:
        """
        DFS, 找联通区域, 没连到边上的都变成X
        """
        if not board: return
        self.m, self.n = len(board), len(board[0])
        self.posO = set()
        self.visited = set()
        self.surrounded = True
        self.curCompNodes = set()

        # printMatrix(board)

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    self.posO.add((i, j))
        
        # print(self.posO)
        def isOnEdge(cur):
            x, y = cur
            if x == 0 or x == self.m - 1 or y == 0 or y == self.n - 1:
                return True
            return False
        # endFunc

        def getNeib(cur):
            x, y = cur
            neibLis = []
            # print(x, self.n - 1)
            # print(board[x + 1][y])
            if x > 0 and board[x - 1][y] == 'O':
                neibLis.append((x - 1, y))
            if x < self.m - 1 and board[x + 1][y] == 'O':
                neibLis.append((x + 1, y))
            if y > 0 and board[x][y - 1] == 'O':
                neibLis.append((x, y - 1))
            if y < self.n - 1 and board[x][y + 1] == 'O':
                neibLis.append((x, y + 1))
            return neibLis
        # endFunc

        def dfs(cur):
            if cur in self.visited: return
            self.visited.add(cur)
            self.curCompNodes.add(cur)
            if isOnEdge(cur):
                self.surrounded = False
            neibLis = getNeib(cur)
            for neib in neibLis:
                if neib in self.visited:
                    continue
                dfs(neib)

        for pos in self.posO:
            dfs(pos)
            if self.surrounded:
                for x, y in self.curCompNodes:
                    board[x][y] = 'X'
            self.surrounded = True
            self.curCompNodes = set()
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.solve,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    enableInput[0] = False
    # enableInput[1] = False
    # enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input[0] = (
        [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt[0] = None

    # ! para2
    input[1] = (
        [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
        # binaryTree.buildTree(None),
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = None

    # ! para3
    input[2] = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt[2] = None

    # ! para4
    input[3] = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt[3] = None

    # ! para5
    input[4] = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt[4] = None

    # ! para6
    input[5] = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
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
        if not enableInput or not inputPara: continue
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
