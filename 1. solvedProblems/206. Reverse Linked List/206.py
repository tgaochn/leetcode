# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Thu, 09/03/2020, 23:57
# !! Description:
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        def recurReverse(pre, cur):
            if not cur:
                return pre
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            return recurReverse(pre, cur)
        
        return recurReverse(None, head)

    def reverseList10(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    
    
    def reverseList2(self, head: ListNode) -> ListNode:
        """
        stack
        """
        if not head: return None

        eleStack = []
        while head:
            eleStack.append(head.val)
            head = head.next

        rltLinkedList = ListNode(eleStack.pop())
        curNode = rltLinkedList
        while eleStack:
            curNode.next = ListNode(eleStack.pop())
            curNode = curNode.next
        
        return rltLinkedList

    def reverseList3(self, head: ListNode) -> ListNode:
        """
        recursively: 
        # !! to be reviewed

        Args:
            head (ListNode): [description]

        Returns:
            ListNode: [description]
        """

        if head is None or head.next is None:
            return head

        def reverseListCur(pre, cur):
            if not cur: return pre
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            return reverseListCur(pre, cur)
        
        return reverseListCur(None, head)
    # endFunc

    def reverseList1(self, head: ListNode) -> ListNode:
        """
        iteratively

        Args:
            head (ListNode): [description]

        Returns:
            ListNode: [description]
        """
        cur = head
        pre = None

        while cur:
            tmp = cur.next # 先保留next, 然后循环顺序来
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    # endFunc
# endClass

def func():
    s = Solution()

    # !! change function name and para here
    myFuncLis = [
        s.reverseList,
    ]
    inputParaLis1 = [
        singleLinkedList.buildSingleList([1,2,3,4,5])
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
