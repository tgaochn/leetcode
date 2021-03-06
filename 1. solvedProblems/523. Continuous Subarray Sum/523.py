# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Tue, 12/15/2020, 24:26
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
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        presum, 前缀和
        https://leetcode-cn.com/problems/continuous-subarray-sum/solution/qian-zhui-he-by-powcai-3/
        """
        if not nums: return False
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        preSum = [0]
        curSum = 0
        n = len(nums)
        for ele in nums:
            curSum += ele
            preSum.append(curSum)

        for i in range(n + 1):
            for j in range(i - 1):
                if (preSum[i] - preSum[j]) % k == 0:
                    return True

        return False 
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.checkSubarraySum,
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
        [358,432,465,409,331,226,256,387,35,468,313,153,139,326,161,451,450,241,213,26,449,185,522,389,192,348,14,370,433,4,34,360,80,446,520,429,246,524,439,165,333,444,447,218,357,191,86,236,338,212,121,340,119,246,467,22,520,140,452,429,275,344,345,190,516,205,231,104,140,469,15,393,322,399,164,437,392,54,59,300,8,463,264,242,224,480,372,96,270,425,453,524,434,381,204,242,10,311,187,460,456,293,199,146,476,42,500,130,420,521,79,56,453,421,497,315,442,282,23,428,239,218,460,42,263,240,129,526,214,287,457,97,315,74,240,357,311,359,464,427,478,452,266,327,129,172,282,25,345,172,325,70,38,198,182,244,54,211,309,519,367,244,411,310,410,132,19,175,446,6,416,449,98,328,490,339,107,517,196,162,285,484,250,52,483,115,468,187,387,229,213,380,184,189,481,93,420,400,263,70,221,147,314,23,405,189,428,122,14,263,170,103,328,469,399,449,187,493,164,283,387,166,260,271,393,347,93,15,69,183,422,346,49,1,389,240,516,23,90,134,414,226,67,309,274,328,497,180,405,187,165,202,355,261,312,334,213,31,280,8,317,168,127,124,483,452,133,160,66,319,76,333,94,55,199,492,242,165,51,286,290,444,371,471,29,216,362,156,343,366,262,240,403,220,65,306,228,477,237,340,217,121,255,278,511,124,235,268,160,23,279,406,431,410,431,211,319,116,264,476,495,244,480,299,399,20,513,361,120,286,198,31,256,475,442,223,277,179,379,48,387,235,55,32,480,167,353,59,499,44,220,392,254,293,345,481,183,361,492,286,245,254,356,350,240,217,71,337,190,519,279,354,218,242,487,304,35,165,425,76,40,318,160,341,269,233,40,344,276,347,298,30,63,275,235,339,50,263,119,344,95,184,192,230,460,314,432,122,58,161,318,51,63,47,382,301,143,350,7,48,240,325,114,306,437,467,230,438,235,284,306,108,509,245,30,413,147,403,19,302,1,366,249,116,107,303,91,146,385,127,91,135,500,26,512,278,272,519,432,230,448,474,115,406,264,170,59,331,294,160,390,194,56,398,287,520,412,194,346,396,503,523,473,157,139,308,214,189,476,405,2,297,301,511,474,357,520,365,169,471,198,132,76,392,62,48,466,118,181,118,472,472,46,47,243,149,289,462,206,9,149,240,370,489,129,250,217,381,133,340,344,68,310,179,119,397,348,292,358,288,337,176,231,135,10,515,188,303,437,436,473,392,306,236,296,92,241,342,193,312,470,73,437,222,391,401,490,305,174,15,11,369,113,502,26,341,257,409,516,138,493,134,91,430,162,131,328,198,85,285,118,307,49,472,406,41,64,34,209,479,228,438,306,292,275,488,515,473,189,372,19,165,438,127,69,408,409,28,517,493,120,68,199,305,457,192,352,139,341,40,287,38,220,69,418,186,522,96,301,17,359,473,99,4,152,88,316,41,379,136,242,370,365,8,501,200,182,465,135,183,307,261,95,374,40,447,501,26,457,88,252,113,117,32,148,298,202,220,6,107,116,55,433,99,490,397,177,302,73,282,147,20,288,229,257,209,491,221,355,243,271,148,22,211,366,68,270,318,403,25,14,261,500,61,460,72,259,285,185,335,194,185,495,270,132,159,444,78,269,169,447,304,296,110,364,321,320,303,168,20,32,166,170,292,418,61,438,411,51,64,189,480,225,496,411,501,498,18,299,109,227,210,195,264,369,499,480,124,457,317,47,151,53,94,20,344,525,116,307,51,120,20,368,379,118,381,154,325,403,120,263,61,475,296,25,251,377,459,465,120,408,57,226,218,500,61,179,219,492,487,493,500,410,19,453,351,341,407,191,368,240,422,2,463,321,9,445,374,471,248,306,9,180,38,40,249,287,267,385,29,266,100,214,242,285,97,272,206,90,95,11,68,223,185,376,358,427,395,146,32,375,423,465,17,191,293,166,83,507,51,16,316,122,169,147,414,223,60,166,354,420,14,15,53,355,383,166,97,457,472,55,35,391,94,523,168,79,92,177,2,149,198,224,512,264,298,253,383,463,343,281,504,206,271,270,177,381,329,452,4,92,41,418,209,312,162,283,395,489,215,128,278,493,150,315,133,11,202,33,181,302,301,319,26,342,430,182,196,519,502,484,395,69,308,306,23,3,409,149,153,486,333,466,485,156,204,419,252,445,51,28,515,297,465,9,418,85,467,488,187,453,375,212,106,442,237,400,198,325,134,425,499,511,324,55,233,127,427,316,112],
        732193917,
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
    expectedRlt[0] = False

    # ! para2
    input[1] = (
        [23, 2, 6, 4, 7],
        0,
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
    expectedRlt[1] = False

    # ! para3
    input[2] = (
        [0, 0],
        - 1,
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
    expectedRlt[2] = True

    # ! para4
    input[3] = (
        [1, 1],
        - 1,
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
    expectedRlt[3] = True

    # ! para5
    input[4] = (
        [1, 2, 3],
        6,
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
    expectedRlt[4] = True

    # ! para6
    input[5] = (
        [1, 1, 0],
        0,
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
    expectedRlt[5] = False
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
