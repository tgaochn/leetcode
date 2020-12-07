# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 08/30/2020, 23:10
# !! Description:
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import singleLinkedList

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fastPt, slowPt = head, head
        while fastPt and fastPt.next:
            fastPt = fastPt.next.next
            slowPt = slowPt.next
            if fastPt == slowPt:
                return True
        return False


# end_class

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.hasCycle,
    ]
    inputParaLis1 = [
        singleLinkedList.buildCycleList([3, 2, 0, -4], 1),
    ]
    # inputParaLis2 = [
        # TODO,
    # ]
    # inputParaLis3 = [
        # TODO,
    # ]

    paraCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    for i in range(paraCnt):
        inputPara1 = inputParaLis1[i]
        # inputPara2 = inputParaLis2[i]
        # inputPara3 = inputParaLis3[i]

        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            print('func: \t%s' % myFunc.__name__)

            print('input1:\t%s' % inputPara1)
            # print('input2: %s' % inputPara2)
            # print('input3: %s' % inputPara3)

            rlt = myFunc(inputPara1)
            # rlt = myFunc(inputPara1, inputPara2)
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
