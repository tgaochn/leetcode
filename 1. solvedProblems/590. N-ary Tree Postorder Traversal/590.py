# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 09/13/2020, 03:18
# !! Description:
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
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

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        rlt = []
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if not node: continue
            if not flag:
                stack.append((1, node))
                if not node.children: continue
                n = len(node.children)
                for i in range(n):
                    child = node.children[-(i + 1)]
                    stack.append((0, child))
            else:
                rlt.append(node.val)
        return rlt



    def postorder3(self, root: 'Node') -> List[int]:
        rlt = []

        def postOrderTra(node):
            if not node: return
            if node.children:
                for child in node.children:
                    postOrderTra(child)
            rlt.append(node.val)

        postOrderTra(root)
        return rlt

    def postorder2(self, root: 'Node') -> List[int]:
        """
        loop
        """
        if not root:return []
        rlt = []
        myStack = [(0, root)]
        while myStack:
            flag, cur = myStack.pop()
            if flag:
                rlt.append(cur.val)
                continue
            myStack.append((1, cur))
            childrenCnt = len(cur.children) if cur.children else 0
            for i in range(childrenCnt):
                child = cur.children[childrenCnt - 1 - i]
                myStack.append((0, child))
        return rlt

    def postorder1(self, root: 'Node') -> List[int]:
        """
        recursion
        """

        rlt = []

        def curTra(cur):
            if not cur:
                return
            children = cur.children if cur.children else []
            for child in children:
                curTra(child)
            rlt.append(cur.val)
        curTra(root)
        return rlt
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name and para here
    # !! input para can be found in "run code" - "test case"
    myFuncLis = [
        s.postorder,
    ]
    inputParaLis1 = [
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([1, null, 3, 2, 4, null, 5, 6])
        nTree.buildTree([1, null, 3, 2, 4, null, 5, 6]),
        nTree.buildTree([]),
    ]
    inputParaLis2 = [
        None,
    ]
    inputParaLis3 = [
        None,
    ]
    # !! ====================================

    # ! instances that need an extra empty line
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
            rltSplitter = '\n' if isOneInstance(para3Splitter, specialTypeLis) else '\t'
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
