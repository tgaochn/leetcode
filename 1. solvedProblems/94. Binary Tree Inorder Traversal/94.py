# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 10/05/2020, 01:09
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(0, root)]
        rlt = []
        while stack:
            flag, node = stack.pop()
            if not node: continue
            if not flag:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:
                rlt.append(node.val)
        return rlt


        
    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        """
        recursively
        
        """
        rlt = []

        def inorderTra(node):
            if not node: return
            inorderTra(node.left)
            rlt.append(node.val)
            inorderTra(node.right)
        
        inorderTra(root)
        return rlt
    # endFunc


    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        non-recursion
        use stack
        """

        rlt = []
        myStack = [(0, root)]
        while myStack:
            flag, cur = myStack.pop()
            if not cur: continue
            if not flag:
                # myStack.append((0, cur.right))
                # myStack.append((0, cur.left))
                # myStack.append((1, cur))

                myStack.append((0, cur.right))
                myStack.append((1, cur))
                myStack.append((0, cur.left))

                # myStack.append((1, cur))
                # myStack.append((0, cur.right))
                # myStack.append((0, cur.left))
            else:
                rlt.append(cur.val)
        return rlt

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        Recursion
        """
        rlt = []

        def recurTraversal(curNode):
            if not curNode: return
            recurTraversal(curNode.left)
            rlt.append(curNode.val)
            recurTraversal(curNode.right)

        recurTraversal(root)
        return rlt
    # endFunc
# endClass

def func():
    onlyDisplayError = True
    enableInput1 = True
    enableInput2 = True
    enableInput3 = True
    enableInput4 = True
    enableInput5 = True
    enableInput6 = True

    s = Solution()

    # !! step2: change function name
    myFuncLis = [
        s.inorderTraversal,
    ]

    # !! step3: change input para, input para can be found in "run code" - "test case"

    # ! para1
    input1 = (
        # singleLinkedList.buildSingleList([])
        binaryTree.buildTree([1, null, 2, 3])
        # nTree.buildTree([[1, null, 2, 3]])
    )
    expectedRlt1 = None

    # ! para2
    input2 = (
        None
    )
    expectedRlt2 = None

    # ! para3
    input3 = (
        None
    )
    expectedRlt3 = None

    # ! para4
    input4 = (
        None
    )
    expectedRlt4 = None

    # ! para5
    input5 = (
        None
    )
    expectedRlt5 = None

    # ! para6
    input6 = (
        None
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
            para3Splitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
        if funcParaCnt >= 4:
            inputPara4 = inputPara[3]
            para4Splitter = '\n' if isOneInstance(para4Splitter, specialTypeLis) else '\t'

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
            rltSplitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
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
