# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/30/2020, 17:46
# !! Description:

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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        标准左右边界搜索模板
        """
        
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            midVal = nums[mid]
            if target < midVal:
                r = mid - 1
            elif target > midVal:
                l = mid + 1
            elif target == midVal:
                r = mid - 1

        lb = l
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            midVal = nums[mid]
            if target < midVal:
                r = mid - 1
            elif target > midVal:
                l = mid + 1
            elif target == midVal:
                l = mid + 1

        rb = r
        if lb >= n or rb < 0 or nums[lb] != target or nums[rb] != target:
            return [-1, -1]

        return [lb, rb]
    
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        """
        二分 + 顺序
        """
        if not nums: return [-1, -1]
        n = len(nums)
        l, r = 0, n - 1

        def findPos(init):
            start, end = init, init
            while start > 0 and nums[start - 1] == nums[start]:
                start -= 1
            while end < n - 1 and nums[end + 1] == nums[end]:
                end += 1
            return [start, end]


        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return findPos(m)
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        
        return [-1, -1]
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.searchRange,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        [5, 7, 7, 8, 8, 10],
        8,
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    expectedRlt1 = None

    # ! para2
    input2 = (
        None
    )
    enableInput2 = True
    expectedRlt2 = None

    # ! para3
    input3 = (
        None
    )
    enableInput3 = True
    expectedRlt3 = None
    # !! ====================================

    # instances that need an extra empty line
    specialTypeLis = [TreeNode, Node]

    # function and parameters count
    allInput = [
        (input1, enableInput1, expectedRlt1),
        (input2, enableInput2, expectedRlt2),
        (input3, enableInput3, expectedRlt3),
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

        # start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputPara[1]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputPara[2]
            para3Splitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'

        # for each function
        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            # output parameters
            if funcParaCnt == 1:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                rlt = myFunc(inputPara1)
            if funcParaCnt == 2:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                rlt = myFunc(inputPara1, inputPara2)
            if funcParaCnt == 3:
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                rlt = myFunc(inputPara1, inputPara2, inputPara3)

            # output result
            rltSplitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            if expectedRlt is not None:
                print('expRlt:%s%s' % (rltSplitter, expectedRlt))
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
