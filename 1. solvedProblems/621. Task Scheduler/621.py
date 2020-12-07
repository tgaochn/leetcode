# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 11/23/2020, 18:44
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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        填桶法任务调度
        https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/
        有空闲(桶没填满) + 没空闲(总数)
        """

        taskCnt = len(tasks)
        maxFreqTaskCnt = 0
        maxFreq = 0

        freqDic = {}
        for task in tasks:
            freqDic.setdefault(task, 0)
            freqDic[task] += 1
            if freqDic[task] > maxFreq:
                maxFreq = freqDic[task]
                maxFreqTaskCnt = 1
            elif freqDic[task] == maxFreq:
                maxFreqTaskCnt += 1

        rltHasIdle = (maxFreq - 1) * (n + 1) + maxFreqTaskCnt
        rltHasNoIdle = taskCnt

        return max(rltHasIdle, rltHasNoIdle)
    # endFunc

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        """
        priotiry queue - 超时
        """
        import queue

        freqDic = {}
        for task in tasks:
            freqDic.setdefault(task, 0)
            freqDic[task] += 1

        # print(freqDic)
        myQue = queue.PriorityQueue()
        for task, freq in freqDic.items():
            myQue.put((-freq, task))

        time = 0
        lastExcTime = {}
        tmp = []
        rlt = []
        while not myQue.empty():
            freq, task = myQue.get()

            # find the element to excute
            while time - lastExcTime.get(task, -n - 1) <= n and not myQue.empty():
                tmp.append((freq, task))
                freq, task = myQue.get()

            # excute the element
            if myQue.empty() and time - lastExcTime.get(task, -n - 1) <= n:
                rlt.append('idle')
                myQue.put((freq, task))
            else:
                rlt.append(task)
                lastExcTime[task] = time
                if -freq > 1:
                    myQue.put((freq + 1, task))
            time += 1

            # put everything back
            while tmp:
                myQue.put(tmp.pop())

        # print(rlt)
        return len(rlt)
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.leastInterval,
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
        ["A", "A", "A", "B", "B", "B"],
        2,
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt[0] = None

    # ! para2
    input[1] = (
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
        2,
        # binaryTree.buildTree(None),
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = 16

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
                formatPrint('input %s:' % (k + 1), para)

            # output result
            print()
            formatPrint('rlt:', rlt)
            if expectedRlt is not None:
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
