# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 12/21/2020, 18:57
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
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        topo 排序典型题目
        http://www.shengjie.me/2018/07/23/leetcode-444/
        以例子4为例， [5,2,6,3] -> [5,2],[2,6],[6,3], [4,1,5,2] -> [4,1],[1,5],[5,2]
        基于以上的edge list可以构造一个图数据结构，而参数org则是满足有向图的遍历路径。当且仅当，org是唯一合法的拓扑遍历路径时，返回true.
        
        即把seqs所有int转化成图结构, 相邻则有边, 当且仅当，org是唯一合法的拓扑遍历路径时，返回true.
        这题边界条件巨恶心, 直接写出基本结构然后抄别人代码好了
        """ 

        from collections import deque
        
        n = len(org)
        adjHash = {id: [] for id in range(1, n + 1)}
        inDegreeHash = {id: 0 for id in range(1, n + 1)}
        
        for seq in seqs:
            m = len(seq)
            for i in range(m - 1):
                fromId = seq[i]
                toId = seq[i + 1]
                adjHash[fromId].append(toId)
                inDegreeHash[toId] += 1
        
        # print(adjHash)
        # print(inDegreeHash)
        
        myQue = deque([org[0]])
        visitedCnt = 0
        while myQue:
            curId = myQue.popleft()
            visitedCnt += 1
            nextIdLis = adjHash.get(curId, [])
            for nextId in nextIdLis:
                inDegreeHash[nextId] -= 1

            validNextIdLis = [id for id in nextIdLis if inDegreeHash[id] == 0] # 只有一条路才是valid
            if not validNextIdLis: continue
            if len(validNextIdLis) > 1: return False
            myQue.append(validNextIdLis[0])
        
        return visitedCnt == n
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.sequenceReconstruction,
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
        [1, 2, 3],
        [[1, 2], [1, 3]],
    )
    expectedRlt[0] = False

    # ! para2
    input[1] = (
        [1, 2, 3],
        [[1, 2]],
    )
    expectedRlt[1] = False

    # ! para3
    input[2] = (
        [1, 2, 3],
        [[1, 2], [1, 3], [2, 3]],
    )
    expectedRlt[2] = True

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
