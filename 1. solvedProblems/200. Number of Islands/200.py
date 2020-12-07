# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 09/13/2020, 20:34
# !! Description:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
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
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS and DFS
        """
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        islandCnt = 0

        def getNeib(i, j):
            neibLis = []
            if i > 0:
                neibLis.append((i - 1, j))
            if i < m - 1:
                neibLis.append((i + 1, j))
            if j > 0:
                neibLis.append((i, j - 1))
            if j < n - 1:
                neibLis.append((i, j + 1))
            return neibLis

        def dfs(i, j):
            visited[i][j] = 1
            neibLis = getNeib(i, j)
            for nextI, nextJ in neibLis:
                if grid[nextI][nextJ] == '0' or visited[nextI][nextJ]: continue
                dfs(nextI, nextJ)

        from collections import deque
        def bfs(i, j):
            myQueue = deque([(i, j)])
            while myQueue:
                curI, curJ = myQueue.popleft()
                if grid[curI][curJ] == '0' or visited[curI][curJ]: continue
                visited[curI][curJ] = 1
                neibLis = getNeib(curI, curJ)
                for nextI, nextJ in neibLis:
                    if grid[nextI][nextJ] == '0' or visited[nextI][nextJ]: continue
                    myQueue.append((nextI, nextJ))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]:
                    continue
                # dfs(i, j)
                bfs(i, j)
                islandCnt += 1
        
        return islandCnt
    # endFunc                

    def numIslands3(self, grid: List[List[str]]) -> int:
        """
        union find
        """
        if not grid:
            return 0

        rowCnt = len(grid)
        colCnt = len(grid[0])
        prevMap = {}

        def find(cur):
            prevMap.setdefault(cur, cur)
            if prevMap[cur] != cur:
                updatedPrev = find(prevMap[cur])
                prevMap[cur] = updatedPrev
            return prevMap[cur]

        def union(x, y):
            root1 = find(x)
            root2 = find(y)
            prevMap[root1] = root2

        def getNeib(i, j):
            neibLis = []
            if i > 0:
                neibLis.append((i - 1, j))
            if i < rowCnt - 1:
                neibLis.append((i + 1, j))
            if j > 0:
                neibLis.append((i, j - 1))
            if j < colCnt - 1:
                neibLis.append((i, j + 1))
            return neibLis

        for i in range(rowCnt):
            for j in range(colCnt):
                if grid[i][j] == "0": continue
                neibLis = getNeib(i, j)
                for nextI, nextJ in neibLis:
                    if grid[nextI][nextJ] == '0':continue
                    union((nextI, nextJ), (i, j))

        islandCnt = 0
        for i in range(rowCnt):
            for j in range(colCnt):
                if grid[i][j] == "0": continue
                if find((i, j)) == (i, j):
                    islandCnt += 1

        return islandCnt

    def numIslands2(self, grid: List[List[str]]) -> int:
        """
        BFS
        """

        if not grid: return 0

        rowCnt = len(grid)
        colCnt = len(grid[0])
        visitedLis = [[False] * colCnt for _ in range(rowCnt)]
        islandCnt = 0
        
        def getNeib(i, j):
            neibLis = []
            if i > 0:
                neibLis.append((i - 1, j))
            if i < rowCnt - 1:
                neibLis.append((i + 1, j))
            if j > 0:
                neibLis.append((i, j - 1))
            if j < colCnt - 1:
                neibLis.append((i, j + 1))
            return neibLis

        from collections import deque
        myQueue = deque()
        for i in range(rowCnt):
            for j in range(colCnt):
                if visitedLis[i][j] or grid[i][j] == '0': continue
                myQueue.append((i, j))
                islandCnt += 1
                while myQueue:
                     curI, curJ = myQueue.popleft()
                     if visitedLis[curI][curJ] or grid[curI][curJ] == '0': continue
                     visitedLis[curI][curJ] = True
                     neibLis = getNeib(curI, curJ)
                     for nextI, nextJ in neibLis:
                        if visitedLis[nextI][nextJ] or grid[nextI][nextJ] == '0':continue
                        myQueue.append((nextI, nextJ))
        
        return islandCnt

    def numIslands1(self, grid: List[List[str]]) -> int:
        """
        DFS
        """
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        visitedLis = [[False] * m for _ in range(n)]
        islandCnt = 0

        def getNeib(i, j):
            neibLis = []
            if i > 0:
                neibLis.append((i - 1, j))
            if i < n - 1:
                neibLis.append((i + 1, j))
            if j > 0:
                neibLis.append((i, j - 1))
            if j < m - 1:
                neibLis.append((i, j + 1))
            return neibLis

        def dfs(i, j):
            visitedLis[i][j] = True
            neibLis = getNeib(i, j)
            for nextI, nextJ in neibLis:
                if visitedLis[nextI][nextJ] or grid[nextI][nextJ] == "0":
                    continue
                dfs(nextI, nextJ)

        for i in range(n):
            for j in range(m):
                if visitedLis[i][j] or grid[i][j] == "0":
                    continue
                islandCnt += 1
                dfs(i, j)
        return islandCnt
    # endFunc
# endClass

def func():
    s = Solution()

    # !! step2: change function name and para here
    # !! input para can be found in "run code" - "test case"
    myFuncLis = [
        s.numIslands,
    ]
    inputParaLis1 = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "0", "1", "1"]
        ],
        # [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
        # [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
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
