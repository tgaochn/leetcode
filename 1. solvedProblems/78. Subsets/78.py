# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 09/04/2020, 14:20
# !! Description:
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking
        """
        rlt = []
        n = len(nums)

        def bt(sol, i):
            if i == n:
                rlt.append(sol)
                return

            for isPicked in [True, False]:
                newSol = sol + [nums[i]] if isPicked else sol
                bt(newSol, i + 1)

        bt([], 0)
        return rlt
    # endFunc

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        recursion (backtracking)

        Args:
            nums (List[int]): [description]

        Returns:
            List[List[int]]: [description]
        """

        res = []
        n = len(nums)

        def backtrack(sol, index):
            # step 1: condition for an end of a search
            if index == n:
                res.append(sol)
                return

            # step 2: update range of the backtracking and answers
            backtrack(sol + [nums[index]], index + 1)  # select or not select
            backtrack(sol, index + 1)

            # step 3: Pruning
            # not necessary in this case

        backtrack([], 0)
        return res
    # endFunc

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        loop

        Args:
            nums (List[int]): [description]

        Returns:
            List[List[int]]: [description]
        """

        rlt = [[]]
        for ele in nums:
            rlt = rlt + [lis + [ele] for lis in rlt]
        return rlt

    # endFunc
# endClass

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.subsets,
    ]
    inputParaLis1 = [
        [1, 2, 3],
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    ]
    inputParaLis2 = [
        None,
    ]
    inputParaLis3 = [
        None,
    ]
    # !! ====================================

    # ! instances that need an empty line
    specialTypeLis = [TreeNode, Node]

    # ! function and parameters count
    inputSetCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    funcParaCnt = 1
    if not inputParaLis3[0] is None:
        funcParaCnt = 3
    elif not inputParaLis2[0] is None:
        funcParaCnt = 2

    # ! for each input set
    for i in range(inputSetCnt):
        inputPara1 = inputParaLis1[i]
        para1Splitter = '\n' if isOneInstance(inputPara1, specialTypeLis) else '\t'
        inputPara2 = None
        para2Splitter = None
        inputPara3 = None
        para3Splitter = None

        # ! start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputParaLis2[i]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputParaLis3[i]
            para3Splitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'

        # ! for each function
        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            # ! output parameters
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

            # ! output result
            rltSplitter = '\n' if isinstance(rlt, TreeNode) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
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
