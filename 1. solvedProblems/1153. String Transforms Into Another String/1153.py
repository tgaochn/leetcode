# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Fri, 12/18/2020, 17:32
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
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        https://leetcode-cn.com/problems/string-transforms-into-another-string/solution/c-jian-dan-bian-li-ji-ke-by-da-li-wang/
        两种情况不能转化:
        1. str2 有26个字母且str1 != str2
        2. str1 中的相同字母对应位置在 str2 中不相同
        """
        # transform into location hash
        locHash1 = {}
        locHash2 = {}
        for idx, curChar in enumerate(str1):
            locHash1.setdefault(curChar, [])
            locHash1[curChar].append(idx)
        for idx, curChar in enumerate(str2):
            locHash2.setdefault(curChar, [])
            locHash2[curChar].append(idx)

        if len(locHash2) == 26 and str1 != str2:
            return False
        for curChar, idxLis in locHash1.items():
            if len(idxLis) == 1: continue
            ele1st = str2[idxLis[0]] # 第一个元素和后面所有元素是否相等
            for idx in idxLis[1:]:
                if ele1st != str2[idx]:
                    return False
        
        return True
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.canConvert,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    # enableInput[0] = False
    enableInput[1] = False
    # enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input[0] = (
        "aabcc",
        "ccdee",
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
    expectedRlt[0] = True

    # ! para2
    input[1] = (
        "leetcode",
        "codeleet",
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
