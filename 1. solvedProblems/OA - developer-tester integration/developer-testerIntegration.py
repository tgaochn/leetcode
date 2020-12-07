# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Thu, 11/12/2020, 02:17
# !! Description:
题目:
https://www.1point3acres.com/bbs/thread-677432-1-1.html

"""
from typing import List
import sys
sys.path.append('..')
from utils.utils import printList
from utils import binaryTree
from utils import singleLinkedList
from utils import nTree

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None

# !! step1: replace these two lines with the given code
class Solution:
    def formTeam(self, d, t, q):
        n = max(q)
        npEndD = [0 for _ in range(n)]
        npEndT = [0 for _ in range(n)]

        npEndD[0] = 1
        npEndT[0] = 1

        # npEndD = [1] + npEndD
        # npEndT = [1] + npEndT

        for i in range(1, n):
        # for i in range(2, n + 1):
            npEndD[i] = npEndT[i - 1] + npEndD[i - 1] - (npEndT[i - d] if i - d >= 0 else 0)
            npEndT[i] = npEndD[i - 1] + npEndT[i - 1] - (npEndD[i - t] if i - t >= 0 else 0)

        rlt = []
        for i in q:
            rlt.append((npEndD[i - 1] + npEndT[i - 1]) % (10 ** 9 + 7))
            # rlt.append((npEndD[i] + npEndT[i]) % (10 ** 9 + 7))
        return rlt

    def formTeam1(self, d, t, q):
        """
        参考答案:
        https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=677432&highlight=Snowflake

        for i in range(0, n):
        对于i而言， array_d 等于array_t[i-1] + 其中一部分arrayd[i-1]. array_t[i-1]毕竟容易理解, 因为有这么多个组合是以T结尾的,拿过来append一个D, 就都是valid的以D结尾的.

        下面重点讨论怎么算是哪一部分array_d[i-1], 因为array_d[i-1]中有一些已经有了d-1个D了. 所以他们不能再继续append一个D,  需要把他们减掉.  这部分组合其实是从array_t[i-d+1]拿过来的. 因为他们拿来以后随着index增加, 一直在append D. index到i的时候, 他们已经积累了d-1个D了. 所以把他们减掉

        所以答案应该是 array_d[i-1] - array_t[i-d]

        时间空间复杂度都是O(n)
        array_d 和 array_t 分别记录以长度为i+1的时候D和T结尾组合个数， 从n = 0 开始构建数组
        """

        n = max(q)

        arr_d = [0 for _ in range(n + 1)]
        arr_t = [0 for _ in range(n + 1)]

        arr_d[0] = 1
        arr_t[0] = 1
        arr_d[1] = 1
        arr_t[1] = 1

        for i in range(2, n + 1):
            arr_d[i] = arr_t[i - 1] + arr_d[i - 1] - (0 if i - d < 0 else arr_t[i - d])
            arr_t[i] = arr_d[i - 1] + arr_t[i - 1] - (0 if i - t < 0 else arr_d[i - t])
        
        rlt = []
        for i in q:
            rlt.append((arr_d[i] + arr_t[i]) % (10 ** 9 + 7))
        return rlt
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.formTeam,
        # s.formTeam1,
    ]

    onlyDisplayError = True
    enableInput1 = True
    enableInput2 = True

    enableInput3 = False
    enableInput4 = False
    enableInput5 = False
    enableInput6 = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    input1 = (
        3, 2, [4]
        # binaryTree.buildTree(None)
        # singleLinkedList.buildSingleList(None)
        # nTree.buildTree(None)
    )
    expectedRlt1 = [5]

    # ! para2
    input2 = (
        # binaryTree.buildTree(None),
        2, 2, [2, 5, 7, 11]
        # singleLinkedList.buildSingleList(None),
        # nTree.buildTree(None),
    )
    expectedRlt2 = [2,2,2,2]

    # ! para3
    input3 = (
        2, 2, 5
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt3 = 2

    # ! para4
    input4 = (
        2, 2, 7
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt4 = 2

    # ! para5
    input5 = (
        2, 2, 11
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt5 = 2

    # ! para6
    input6 = (
        3, 3, 4
        # singleLinkedList.buildSingleList(None),
        # binaryTree.buildTree(None),
        # nTree.buildTree(None),
    )
    expectedRlt6 = None
    # !! ====================================

    # instances that need an extra empty line
    specialTypeLis = [TreeNode, Node]

    # function and parameters count
    allInput = [
        (input1, enableInput1, expectedRlt1),
        (input2, enableInput2, expectedRlt2),
        (input3, enableInput3, expectedRlt3),
        (input4, enableInput4, expectedRlt4),
        (input5, enableInput5, expectedRlt5),
        (input6, enableInput6, expectedRlt6),
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
        inputPara4 = None
        para4Splitter = None

        # start a new line if the parameter is a tree
        if funcParaCnt >= 2:
            inputPara2 = inputPara[1]
            para2Splitter = '\n' if isOneInstance(inputPara2, specialTypeLis) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputPara[2]
            para3Splitter = '\n' if isOneInstance(inputPara3, specialTypeLis) else '\t'
        if funcParaCnt >= 4:
            inputPara4 = inputPara[3]
            para4Splitter = '\n' if isOneInstance(inputPara4, specialTypeLis) else '\t'

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]
            # print('func: \t%s' % myFunc.__name__)

            # output parameters
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara1)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
            if funcParaCnt == 2:
                rlt = myFunc(inputPara1, inputPara2)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
            if funcParaCnt == 3:
                rlt = myFunc(inputPara1, inputPara2, inputPara3)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
            if funcParaCnt == 4:
                rlt = myFunc(inputPara1, inputPara2, inputPara3, inputPara4)
                if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue
                print('input1:%s%s' % (para1Splitter, inputPara1))
                print('input2:%s%s' % (para2Splitter, inputPara2))
                print('input3:%s%s' % (para3Splitter, inputPara3))
                print('input4:%s%s' % (para4Splitter, inputPara4))

            # output result
            rltSplitter = '\n' if isOneInstance(rlt, specialTypeLis) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            if expectedRlt is not None:
                print('expRlt:%s%s' % (rltSplitter, expectedRlt))
            # print('==' * 20)
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
