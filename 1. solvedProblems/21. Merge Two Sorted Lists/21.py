# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 08/30/2020, 19:40
# !! Description:
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import linkedList

ListNode = linkedList.ListNode
TreeNode = binaryTree.TreeNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1pt = l1
        l2pt = l2
        rlt = None
        rltPt = None

        if not (l1pt is None and l2pt is None):
            if l1pt is None or (not l2pt is None and l1pt.val > l2pt.val):
                rlt = ListNode(l2pt.val)
                l2pt = l2pt.next
            else:
                rlt = ListNode(l1pt.val)
                l1pt = l1pt.next
            rltPt = rlt

        while not (l1pt is None and l2pt is None):
            curNode = None
            if l1pt is None or (not l2pt is None and l1pt.val > l2pt.val):
                curNode = ListNode(l2pt.val, l2pt.next)
                l2pt = l2pt.next
            else:
                curNode = ListNode(l1pt.val, l1pt.next)
                l1pt = l1pt.next
            rltPt.next = curNode
            rltPt = rltPt.next
        return rlt

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.mergeTwoLists,
    ]
    inputParaLis1 = [
        # linkedList.buildSingleList([1, 2, 4]),
        linkedList.buildSingleList([1]),
    ]
    inputParaLis2 = [
        # linkedList.buildSingleList([1, 3, 4]),
        linkedList.buildSingleList([]),
    ]
    # inputParaLis3 = [
        # TODO,
    # ]

    paraCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    for i in range(paraCnt):
        inputPara1 = inputParaLis1[i]
        inputPara2 = inputParaLis2[i]
        # inputPara3 = inputParaLis3[i]

        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            print('input1:\t%s' % inputPara1)
            print('input2: %s' % inputPara2)
            # print('input3: %s' % inputPara3)

            # rlt = myFunc(inputPara1)
            rlt = myFunc(inputPara1, inputPara2)
            # rlt = myFunc(inputPara1, inputPara2, inputPara3)
            print('rlt: \t%s' % rlt)
            print('==' * 20)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
