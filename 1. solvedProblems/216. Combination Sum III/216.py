# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 09/26/2020, 21:22
# !! Description:
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iii
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

# !! step1: replace these two lines with the given code
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def Search(num, _Sum, oneSolution):
            if _Sum == 0 and len(oneSolution) == k:  # 找到了正确的解
                totalSolutions.append(oneSolution[:])  # 注意要切片一下。相当于复制了一遍内容。*切片不加也没关系。*
                return

            if num == 10:  # 1~9查完了
                return

            if _Sum < 0:  # 数组和大于n了
                return

            if len(oneSolution) > k:  # 数组长度大于k了
                return

            Search(num + 1, _Sum - num, oneSolution + [num])  # 选了这个数
            Search(num + 1, _Sum, oneSolution)   # 没选择这个数

        totalSolutions = []

        Search(1, n, [])

        return totalSolutions

    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        from copy import deepcopy
        rlt = []
        existol = set()

        def bt(sol, availIds, curSum):
            if len(sol) == k and sum(sol) == n:
                sol.sort()
                solStr = ''.join([str(ele) for ele in sol])
                if solStr in existol: return False
                rlt.append(sol)
                existol.add(solStr)
                return True

            if sum(sol) > n:
                return False
            
            for i in availIds:
                availIds.remove(i)
                bt(sol + [i], availIds, curSum - i)
                availIds.add(i)
                
        
        bt([], set(range(1, min(n + 1, 10))), 0)
        return rlt
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.combinationSum3,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        3,
        9,
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    )
    enableInput1 = True
    expectedRlt1 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

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
            if expectedRlt:
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
