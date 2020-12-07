# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Thu, 11/12/2020, 02:24
# !! Description:
题目:
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=678726&highlight=snowflake

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

import math
import copy

# A class to represent a Point in 2D plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        rlt = '(%s, %s)' % (self.x, self.y)
        return rlt

    def __repr__(self):
        return self.__str__()
# endClass

# A utility function to find the distance between two points
def dist(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    # return math.sqrt((p1.x - p2.x) *
    #  (p1.x - p2.x) +
    #  (p1.y - p2.y) *
    #  (p1.y - p2.y))
# endFunc

# A Brute Force method to return the smallest distance between two points in points[] of size n
def minDistBF(points):
    minDist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            minDist = min(minDist, dist(points[i], points[j]))

    return minDist
# endFunc

def minDistNearEdge(points, minDist):
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if points[j].y - points[i].y >= minDist: break
            minDist = min(minDist, dist(points[i], points[j]))

    return minDist
# endFunc

def closestPointsPairDC(points1, points2):
    n = len(points1)

    # if n <= 3:
    if n <= 4:
        return minDistBF(points1)

    midIdx = n // 2
    midPoint = points1[midIdx]

    distL = closestPointsPairDC(points1[:midIdx], points2)
    distR = closestPointsPairDC(points1[midIdx:], points2)
    minDist = min(distL, distR)
    pointsNearEdge = [points2[i] for i in range(n) if abs(points2[i].x - midPoint.x) < minDist]
    minDist1 = minDistNearEdge(pointsNearEdge, minDist)
    # minDist1 = minDistBF(pointsNearEdge)

    return min(minDist, minDist1)
# endFunc

# !! step1: replace these two lines with the given code
class Solution:
    def cloestSquareDistance(self, x, y):
        points = []
        n = len(x)
        for i in range(n):
            posX = x[i]
            posY = y[i]
            points.append(Point(posX, posY))

        points1 = sorted(points, key=lambda point: point.x)
        points2 = sorted(points, key=lambda point: point.y)

        # print(points1)
        # print(points2)

        # divide and conquer
        minDist = closestPointsPairDC(points1, points2)
        return minDist
        # return math.sqrt(minDist)
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.cloestSquareDistance,
    ]

    onlyDisplayError = True
    enableInput1 = True
    enableInput2 = True
    enableInput3 = True
    enableInput4 = True
    enableInput5 = True
    enableInput6 = True

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        [2, 12, 40, 5, 12, 3],
        [3, 30, 50, 1, 10, 4],
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt1 = 2

    # ! para2
    input2 = (
        # binaryTree.buildTree(None),
        [0, 10, 15],
        [0, 10, 20],
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt2 = 125

    # ! para3
    input3 = (
        [77, 1000, 992, 1000000],
        [0, 1000, 500, 0]
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt3 = 250064

    # ! para4
    input4 = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt4 = None

    # ! para5
    input5 = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt5 = None

    # ! para6
    input6 = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
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
        inputPara4 = None
        para4Splitter = None

        # start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputPara[1]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputPara[2]
            para3Splitter = '\n' if isOneInstance(inputPara3, specialTypeLis) else '\t'
        if funcParaCnt >= 4:
            inputPara4 = inputPara[3]
            para4Splitter = '\n' if isOneInstance(inputPara4, specialTypeLis) else '\t'

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]
            # print('func: \t%s' % myFunc.__name__)

            # output parameters
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara1)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
            if funcParaCnt == 2:
                rlt = myFunc(inputPara1, inputPara2)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
            if funcParaCnt == 3:
                rlt = myFunc(inputPara1, inputPara2, inputPara3)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
            if funcParaCnt == 4:
                rlt = myFunc(inputPara1, inputPara2, inputPara3, inputPara4)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                print('input4:%s%s' % (para4Splitter, inputPara4))

            # output result
            rltSplitter = '\n' if isOneInstance(rlt, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            if expectedRlt is not None:
                print('expRlt:%s%s' % (rltSplitter, expectedRlt))
            # print('==' * 20)
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
