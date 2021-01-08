# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 12/16/2020, 01:39
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
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        面试重写
        """
        from collections import deque
        import heapq
        
        l, r = 0, 0
        n = len(nums)
        win = deque()
        maxLen = 0

        maxHeap = []
        minHeap = []
        heapq.heapify(maxHeap)
        heapq.heapify(minHeap)

        while r < n:
            if not win:
                heapq.heappush(maxHeap, (-nums[r], r))
                heapq.heappush(minHeap, (nums[r], r))
                win.append(nums[r])
                r += 1
            elif -maxHeap[0][0] - minHeap[0][0] > limit:
            # elif max(win) - min(win) > limit:
                if maxHeap[0][1] <= l:
                    heapq.heappop(maxHeap)
                if minHeap[0][1] <= l:
                    heapq.heappop(minHeap)
                
                win.popleft()
                l += 1
            else:
                maxLen = max(maxLen, len(win))
                heapq.heappush(maxHeap, (-nums[r], r))
                heapq.heappush(minHeap, (nums[r], r))
                win.append(nums[r])
                r += 1
        
        if -maxHeap[0][0] - minHeap[0][0] <= limit:
        # if max(win) - min(win) <= limit:
            maxLen = max(maxLen, len(win))
        
        return maxLen

        
              
        
    def longestSubarray1(self, nums: List[int], limit: int) -> int:
        """
        滑动窗口 + 大小堆 经典题目
        """
        from collections import deque
        import heapq

        win = deque()
        i, j = 0, 0
        n = len(nums)
        maxLen = -float('inf')

        max_hq = []
        min_hq = []

        while j < n:
            if not win:
                win.append(nums[j])

                heapq.heappush(max_hq, (-nums[j], j))
                heapq.heappush(min_hq, (nums[j], j))

                j += 1
            # elif max(win) - min(win) > limit:
            elif -max_hq[0][0] - min_hq[0][0] > limit:
                win.popleft()

                while max_hq[0][1] <= i:
                    heapq.heappop(max_hq)
                while min_hq[0][1] <= i:
                    heapq.heappop(min_hq)

                i += 1
            else:
                maxLen = max(maxLen, len(win))
                win.append(nums[j])

                heapq.heappush(max_hq, (-nums[j], j))
                heapq.heappush(min_hq, (nums[j], j))

                j += 1
            # print(win)

        # if max(win) - min(win) <= limit:
        if -max_hq[0][0] - min_hq[0][0] <= limit:
            maxLen = max(maxLen, len(win))

        return maxLen
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.longestSubarray,
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
        [8, 2, 4, 7],
        4,
        # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),
    )
    expectedRlt[0] = 2

    # ! para2
    input[1] = (
        [10, 1, 2, 4, 7, 2],
        5,
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = 4

    # ! para3
    input[2] = (
        None,
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[2] = None

    # ! para4
    input[3] = (
        None,
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[3] = None

    # ! para5
    input[4] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
        # nTree.buildTree(None),
    )
    expectedRlt[4] = None

    # ! para6
    input[5] = (
        None
        # singleLinkedList.buildSingleList(None),
        #         # binaryTree.buildTree(
        #     None
        # ),
        #
        # singleLinkedList.buildSingleList(
        #     None
        # ),
        #
        # nTree.buildTree(
        #     None
        # ),,
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
