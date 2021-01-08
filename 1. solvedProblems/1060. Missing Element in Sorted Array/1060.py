# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 12/19/2020, 20:12
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
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        一次性二分, missing counting 二分的时候算
        """
        n = len(nums)
        l, r = 0, n - 1
        
        def getMissingCnt(nums, idx):
            return (nums[idx] - nums[0] + 1) - (idx - 0 + 1)  # shouldHave - realHave
        
        while l <= r:   # 多个相同 missing cnt要找左边界, 因此用左边界模板
            mid = l + (r - l) // 2
            missingCnt = getMissingCnt(nums, mid)
            if missingCnt > k:
                r = mid - 1
            elif missingCnt < k:
                l = mid + 1
            elif missingCnt == k:
                r = mid - 1
        
        # print(l, r)

        # 不可能在左边追加, 所以忽略 r < 0
        if l > n - 1:   # 整个数组的missing cnt都不够, 则追加到数组后面
            return nums[n - 1] + k - getMissingCnt(nums, n - 1)
        elif getMissingCnt(nums, l) == k: # 某个时候 missing cnt == k, 则返回右边界的值 - 1
            return nums[l] - 1 
        else:  # 某个时候 missing cnt < k, 则从左边界的值开始往后补
            return nums[r] + k - getMissingCnt(nums, r)
    # endFunc
            
    def missingElement2(self, nums: List[int], k: int) -> int:
        """
        https://leetcode-cn.com/problems/missing-element-in-sorted-array/solution/you-xu-shu-zu-zhong-de-que-shi-yuan-su-by-leetcode/
        更容易理解的 missing counting 二分
        先算missing counting, 再二分
        """
        n = len(nums)
        l, r = 0, n - 1
        missingCntList = [0] * n
        for i in range(n):
            missingCntList[i] = (nums[i] - nums[0] + 1) - (i - 0 + 1) # shouldHave - realHave
        
        # print(missingCntList)
        while l <= r:
            mid = l + (r - l) // 2
            if missingCntList[mid] == k:    # 多个相同missing cnt取最左边, 即找左边界
                r = mid - 1
            elif missingCntList[mid] > k:
                r = mid - 1
            elif missingCntList[mid] < k:
                l = mid + 1

        # print(l)
        if l < n and missingCntList[l] == k:
            return nums[l] - 1
        
        if l < n:
            return nums[l] - 1 - (missingCntList[l] - k)
        
        if l >= n:
            return nums[n - 1] + (k - missingCntList[n - 1])
        
        
            

    def missingElement1(self, nums: List[int], k: int) -> int:
        """
        https://leetcode-cn.com/problems/missing-element-in-sorted-array/solution/c-er-fen-cha-zhao-1060-you-xu-shu-zu-zhong-de-que-/
        第一反应是遍历
        第二看到是排序数组, 想到二分
        """
        n = len(nums)
        l, r = 0, n - 1

        missingCnt = None
        while l <= r:
            m = l + (r - l) // 2
            missingCnt = (nums[m] - nums[l] + 1) - (m - l + 1)  # shouldHave - realHave
            if missingCnt == k:
                return nums[m] - 1
            elif missingCnt < k:
                l = m + 1
                k -= missingCnt
            elif missingCnt > k:
                r = m - 1

        # print(l, r, k)
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.missingElement,
        # optional: add another function for comparison
    ]

    onlyDisplayError = False
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
        [4, 7, 9, 10],
        1,
    )
    expectedRlt[0] = 5

    # ! para2
    input[1] = (
        [4, 7, 9, 10],
        3,
    )
    expectedRlt[1] = 8

    # ! para3
    input[2] = (
        [1, 2, 4],
        3,
    )
    expectedRlt[2] = 6

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
