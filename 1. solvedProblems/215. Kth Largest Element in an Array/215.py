# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 12/05/2020, 20:13
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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        默写快排
        """
        import random
        
        def partition(nums, l, r):
            randomId = random.randint(l, r)
            pivot = nums[randomId]
            nums[l], nums[randomId] = nums[randomId], nums[l]
            
            lp = l + 1
            rp = r
            while True:
                while lp <= r and nums[lp] <= pivot:
                    lp += 1
                while rp >= l + 1 and nums[rp] >= pivot:
                    rp -= 1
                    
                if lp > rp: break
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
                rp -= 1

            nums[l], nums[rp] = nums[rp], nums[l]
            return rp
        
        n = len(nums)
        k = n - k
        l, r = 0, n - 1
        while l <= r:
            p = partition(nums, l, r)
            if p == k:
                return nums[p]
            elif p > k:
                r = p - 1
            elif p < k:
                l = p + 1
        return -1
        
        
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """
        经典快排 quick sort
        这个partition容易理解
        """
        import random

        def partition(nums, l, r):
            if r == l + 1: return l  # optional

            randId = random.randint(l, r)
            pivot = nums[randId]
            nums[l], nums[randId] = nums[randId], nums[l]  # 先换到左边

            lp = l + 1  # 记得用2个新指针
            rp = r

            while True:
                while lp <= r and nums[lp] <= pivot:
                    lp += 1
                while rp >= l + 1 and nums[rp] >= pivot:
                    rp -= 1

                # ! 这里条件是否有等于无所谓, 因为lp仅在r==l + 1时有可能等于rp. 假设 lp == rp
                # 1. lp,rp不可能在中间, 因为和pivot的关系
                # 2. 如果在两边则lp == r + 1, rp == r 或者 rp == l, lp == r + 1, 都不可能
                if lp > rp:  # >= 也可以
                    break

                nums[lp], nums[rp] = nums[rp], nums[lp]  # 交换左边第一个大的/右边第一个小的
                lp += 1
                rp -= 1

            # ! 因为rp是右边第一个小的, 所以交换之后还是左边都比pivot小. 这里必须是rp才能超出界限后自我交换不影响
            nums[l], nums[rp] = nums[rp], nums[l]
            return rp

        n = len(nums)
        k = n - k  # 第k大 <=> 第n-k小
        l = 0
        r = n - 1

        while l <= r:
            p = partition(nums, l, r)
            if k == p:
                return nums[p]
            elif k < p:
                r = p - 1
            else:
                l = p + 1
        return -1

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        quick sort 1
        这个partition不太容易理解
        """
        import random

        def partition(nums, l, r):
            midVal = nums[l]

            while l < r:
                while l < r and nums[r] >= midVal:
                    r -= 1
                nums[l] = nums[r]

                while l < r and nums[l] <= midVal:
                    l += 1
                nums[r] = nums[l]

            nums[l] = midVal
            return l

        print(nums)
        n = len(nums)
        k = n - k
        l = 0
        r = n - 1
        while l <= r:
            p = partition(nums, l, r)
            if k == p:
                return nums[p]
            elif k < p:
                r = p - 1
            else:
                l = p + 1
        return -1

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        use heap lib
        """
        import heapq

        myHeap = nums[:k]
        heapq.heapify(myHeap)

        for ele in nums[k:]:
            heapq.heappushpop(myHeap, ele)

        return min(myHeap)
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.findKthLargest,
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
        [3, 2, 1, 5, 6, 4],
        2,
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt[0] = 5

    # ! para2
    input[1] = (
        [4, 3, 4, 4], 2

        # binaryTree.buildTree(None),
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt[1] = 4

    # ! para3
    input[2] = (
        [2, 2, 2, 3], 2
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt[2] = 2

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
