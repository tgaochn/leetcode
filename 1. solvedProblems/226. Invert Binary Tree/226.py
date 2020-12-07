# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Tue, 09/01/2020, 20:19
# !! Description:
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import singleLinkedList

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp
        return root

# end_class

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.invertTree,
    ]
    inputParaLis1 = [
        binaryTree.buildTree([4, 2, 7, 1, 3, 6, 9]),
    ]
    inputParaLis2 = [
        None,
    ]
    inputParaLis3 = [
        None,
    ]

    inputSetCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    funcParaCnt = 1
    if not inputParaLis3[0] is None:
        funcParaCnt = 3
    elif not inputParaLis2[0] is None:
        funcParaCnt = 2

    for i in range(inputSetCnt):
        inputPara1 = inputParaLis1[i]
        para1Splitter = '\n' if isinstance(inputPara1, TreeNode) else '\t'
        inputPara2 = None
        para2Splitter = None
        inputPara3 = None
        para3Splitter = None

        if funcParaCnt >= 2: 
            inputPara2 = inputParaLis2[i]
            para2Splitter = '\n' if isinstance(inputPara2, TreeNode) else '\t'
        if funcParaCnt >= 3:
            inputPara3 = inputParaLis3[i]
            para3Splitter = '\n' if isinstance(para3Splitter, TreeNode) else '\t'


        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

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

            rltSplitter = '\n' if isinstance(rlt, TreeNode) else '\t'
            print('rlt:%s%s' % (rltSplitter, rlt))
            print('==' * 20)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
