# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Mon, 08/31/2020, 00:11
# !! Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
"""
from typing import List
import sys
sys.path.append('..')
from utils import binaryTree
from utils import singleLinkedList

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.minEleIdxLis = []
        self.eleCnt = 0

    def push(self, x: int) -> None:
        if len(self.minStack) <= self.eleCnt:
            self.minEleIdxLis.append(None)
            self.minStack.append(None)

        if self.eleCnt == 0 or self.getMin() > x:
            self.minEleIdxLis[self.eleCnt] = self.eleCnt
        else:
            self.minEleIdxLis[self.eleCnt] = self.minEleIdxLis[self.eleCnt - 1]

        self.minStack[self.eleCnt] = x
        self.eleCnt += 1


    def pop(self) -> None:
        self.eleCnt -= 1

    def top(self) -> int:
        return self.minStack[self.eleCnt - 1]

    def getMin(self) -> int:
        return self.minStack[self.minEleIdxLis[self.eleCnt - 1]]

# end_class

def func():
    obj = MinStack()
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(2147483647)
    print(obj.top())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    obj.pop()
    obj.push(2147483647)
    print(obj.top())
    print(obj.getMin())
    obj.push(-2147483648)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
