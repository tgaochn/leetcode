# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 11/11/2020, 22:54
# !! Description:
题目:
https://leetcode.com/discuss/interview-question/808374/Amazon-or-OA-2020-or-Nearest-City/683808
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
    def getNearestCities(self, numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries):
        """
        最坏情况 N * N, 应该比另一种方法快得多
        """
        import gc

        # ! 根据坐标对city分组
        x2cityIdx = {}
        y2cityIdx = {}
        for idx, x in enumerate(xCoordinates):
            x2cityIdx.setdefault(x, [])
            x2cityIdx[x].append(idx)
        for idx, y in enumerate(yCoordinates):
            y2cityIdx.setdefault(y, [])
            y2cityIdx[y].append(idx)

        cityIdxSameX = x2cityIdx.values()
        cityIdxSameY = y2cityIdx.values()
        del x2cityIdx, y2cityIdx
        gc.collect()
        # print(cityIdxSameX)
        # print(cityIdxSameY)

        # ! 根据分组的city计算dist
        cityDistMap = {}
        for cityIdxList in cityIdxSameX:
            for cityIdx1 in cityIdxList:
                cityDistMap.setdefault(cityIdx1, set())
                minDist = float('inf')
                for cityIdx2 in cityIdxList:
                    cityDistMap.setdefault(cityIdx2, set())
                    if cityIdx1 >= cityIdx2: continue
                    dist = abs(yCoordinates[cityIdx1] - yCoordinates[cityIdx2])
                    if dist < minDist:
                        cityDistMap[cityIdx1].add((cityIdx2, dist))
                        cityDistMap[cityIdx2].add((cityIdx1, dist))
                        minDist = dist
        print(cityDistMap)

        for cityIdxList in cityIdxSameY:
            for cityIdx1 in cityIdxList:
                minDist = float('inf')
                for cityIdx2 in cityIdxList:
                    if cityIdx1 >= cityIdx2: continue
                    dist = abs(yCoordinates[cityIdx1] - yCoordinates[cityIdx2])
                    if dist < minDist:
                        cityDistMap[cityIdx1].add((cityIdx2, dist))
                        cityDistMap[cityIdx2].add((cityIdx1, dist))
                        minDist = dist

        print(cityDistMap)

        # ! 根据dist找到nearest city
        nearestCityMap = {}
        for city, distInfo in cityDistMap.items():
            if not distInfo:
                nearestCityMap[cities[city]] = None
            else:
                distInfo = min(distInfo, key=lambda x: (x[1], cities[x[1]]))
                nearestCityMap[cities[city]] = cities[distInfo[0]]
                cityDistMap[city] = None

        del cityDistMap
        gc.collect()
        print(nearestCityMap)

        # ! query
        rlt = []
        for queryCity in queries:
            nearestCity = nearestCityMap.get(queryCity, None)
            rlt.append(nearestCity)

        return rlt
    # endFunc

    def getNearestCities1(self, numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries):
        """
        Complexity O(nq log(n))
        """
        def getDistance(x1, y1, x2, y2):
            distance = abs(x1 - x2) + abs(y1 - y2)
            return distance

        def getNeighbours(queryCity):
            finalList = []
            minDist = float('inf')

            ind = cities.index(queryCity)
            x = xCoordinates[ind]
            y = yCoordinates[ind]

            for i in range(numOfCities):
                # for i, city in enumerate(cities):
                if i != ind and (xCoordinates[i] == x or yCoordinates[i] == y):
                    distance = getDistance(x, y, xCoordinates[i], yCoordinates[i])
                    if distance < minDist:
                        finalList = []
                        minDist = distance
                        finalList.append(i)
                    elif distance == minDist:
                        finalList.append(i)
            return finalList

        result = []
        for city in queries:
            temp = getNeighbours(city)
            if len(temp) == 1:
                result.append(cities[temp[0]])
            elif len(temp) == 0:
                result.append(None)
            else:
                cityIdxList = []
                for ele in temp:
                    cityIdxList.append(cities[ele])
                result.append(sorted(cityIdxList)[0])
        return result
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.getNearestCities,
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
        3,
        ["c1", "c2", "c3"],
        [3, 2, 1],
        [3, 2, 3],
        3,
        ["c1", "c2", "c3"],
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt1 = ["c3", None, "c1"]

    # ! para2
    input2 = (
        # binaryTree.buildTree(None),
        5,
        ["c0", "c1", "c2", "c3", "c4"],
        [3, 2, 1, 1, 1],
        [3, 2, 3, 1, 2],
        3,
        ["c0", "c1", "c2", 'c4'],
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt2 = None

    # ! para3
    input3 = (
        None
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt3 = None

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
        inputPara5 = None
        para5Splitter = None
        inputPara6 = None
        para6Splitter = None

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
        if funcParaCnt >= 5:
            inputPara5 = inputPara[4]
            para5Splitter = '\n' if isOneInstance(inputPara5, specialTypeLis) else '\t'
        if funcParaCnt >= 6:
            inputPara6 = inputPara[5]
            para6Splitter = '\n' if isOneInstance(inputPara6, specialTypeLis) else '\t'

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
            if funcParaCnt == 5:
                rlt = myFunc(inputPara1, inputPara2, inputPara3, inputPara4, inputPara5)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                print('input4:%s%s' % (para4Splitter, inputPara4))
                print('input5:%s%s' % (para5Splitter, inputPara5))
            if funcParaCnt == 6:
                rlt = myFunc(inputPara1, inputPara2, inputPara3, inputPara4, inputPara5, inputPara6)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                print('input4:%s%s' % (para4Splitter, inputPara4))
                print('input5:%s%s' % (para5Splitter, inputPara5))
                print('input6:%s%s' % (para6Splitter, inputPara6))

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
