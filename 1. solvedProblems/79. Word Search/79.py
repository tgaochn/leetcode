# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 09/23/2020, 20:06
# !! Description:
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
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

# !! step1: replace these two lines with the given code
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board: return False

        rowCnt = len(board)
        colCnt = len(board[0])
        n = len(word)
        visited = set()
        charPos = {}
        for row, items in enumerate(board):
            for col, curChar in enumerate(items):
                charPos.setdefault(curChar, [])
                charPos[curChar].append((row, col))

        def df(i, curRow, curCol, visited):
            if i == n: return True

            candPosLis = []
            if curRow > 0:
                candPosLis.append((curRow - 1, curCol))
            if curRow < rowCnt - 1:
                candPosLis.append((curRow + 1, curCol))
            if curCol > 0:
                candPosLis.append((curRow, curCol - 1))
            if curCol < colCnt - 1:
                candPosLis.append((curRow, curCol + 1))

            for (nextRow, nextCol) in candPosLis:
                if board[nextRow][nextCol] != word[i] or (nextRow, nextCol) in visited: continue
                visited.add((nextRow, nextCol))
                if df(i + 1, nextRow, nextCol, visited):
                    return True
                visited.remove((nextRow, nextCol))

            return False

        curChar = word[0]
        posLis = charPos.get(curChar, [])
        for row, col in posLis:
            visited.add((row, col))
            if df(1, row, col, visited):
                return True
            visited.remove((row, col))
        return False
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name and para here
    # !! input para can be found in "run code" - "test case"
    myFuncLis = [
        s.exist,
    ]
    inputParaLis1 = [
        [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
        ],

        # [
            # ["A", "B", "C", "E"],
            # ["S", "F", "C", "S"],
            # ["A", "D", "E", "E"]
        # ]
        # singleLinkedList.buildSingleList([])
        # binaryTree.buildTree([])
        # nTree.buildTree([])
    ]
    inputParaLis2 = [
        "ABCCED",
        # "ABCB",
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
