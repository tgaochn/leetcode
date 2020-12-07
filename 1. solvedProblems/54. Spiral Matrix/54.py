# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 12/04/2020, 16:22
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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        一般DFS, 控制neib即可
        """
        self.rlt = []
        self.visited = set()
        self.m = len(matrix)
        self.n = len(matrix[0])

        def getNext(cur, direction):
            x, y = cur
            nextLis = []
            if direction == 0:
                while (x + 1, y) not in self.visited and x + 1 < self.n:
                    nextLis.append((x + 1, y))
                    x += 1
                return (x, y), nextLis
            elif direction == 1:
                while (x, y + 1) not in self.visited and y + 1 < self.m:
                    nextLis.append((x, y + 1))
                    y += 1
                return (x, y), nextLis
            elif direction == 2:
                while (x - 1, y) not in self.visited and x - 1 >= 0:
                    nextLis.append((x - 1, y))
                    x -= 1
                return (x, y), nextLis
            elif direction == 3:
                while (x, y - 1) not in self.visited and y - 1 >= 0:
                    nextLis.append((x, y - 1))
                    y -= 1
                return (x, y), nextLis

        def dfs(cur, direction):
            self.visited.add(cur)
            next, pathNodeList = getNext(cur, direction)
            while next == (0, 0) and len(self.visited) < self.m * self.n:
                direction += 1
                next, pathNodeList = getNext(cur, direction)
            if next in self.visited: return
            for pathNode in pathNodeList:
                self.visited.add(pathNode)
                x, y = pathNode
                self.rlt.append(matrix[y][x])
            dfs(next, (direction + 1) % 4)

        self.rlt.append(matrix[0][0])
        dfs((0, 0), 0)
        return self.rlt
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.spiralOrder,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    enableInput[0] = False
    enableInput[1] = False
    # enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input[0] = (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt[0] = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # ! para2
    input[1] = (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        # binaryTree.buildTree(None),
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # ! para3
    input[2] = (
        [[3], [2]]
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt[2] = [3, 2]

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
                formatPrint('input %s:' % (k + 1), para)

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
