# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Wed, 01/27/2021, 15:51
# !! Description:

"""
import sys
from typing import List

sys.path.append('..')
sys.path.append('../..')
from utils import binaryTree, nTree, singleLinkedList
from utils.utils import (
    printMatrix,
    printDict,
    printList,
    isMatrix,
    parsePara,
)

ListNode = singleLinkedList.ListNode
TreeNode = binaryTree.TreeNode
Node = nTree.Node
null = None
testCaseCnt = 6
# maxFuncInputParaCnt = 8
true = True
false = False

import re

# !! step1: replace these two lines with the given code
class Solution:
    def getEventsOrder(self, team1, team2, events1, events2):
        """
        https://leetcode.com/discuss/interview-question/375258/Twitter-or-OA-2019-or-Game-Events
        """
        rePatternStr = r'([a-zA-Z\s]*)(\d+)[+]?(\d*).([G,Y,R,S])([a-zA-z\s]*)'
        pattern = re.compile(rePatternStr)
        gameInfo = []
        eventOri = []
        prio = ['G', 'Y', 'R', 'S']

        for i, events in enumerate([events1, events2]):
            for event in events:
                curTeam = team1 if i == 0 else team2
                eventOri.append(curTeam + ' ' + event)
                matches = pattern.search(event)
                record = [curTeam]
                if matches:
                    playerNm = matches.group(1).strip()
                    gameTime = int(matches.group(2).strip())
                    extraTime = matches.group(3).strip()
                    extraTime = int(extraTime) if extraTime else 0
                    eventType = prio.index(matches.group(4).strip())
                    player2 = matches.group(5).strip()
                    record += [playerNm, gameTime, extraTime, eventType, player2]
                gameInfo.append(record)
        # print(gameInfo)

        rltLisSorted = sorted(range(len(gameInfo)),
                              key=lambda x: (
            gameInfo[x][2],
            gameInfo[x][3],
            gameInfo[x][4],
            gameInfo[x][0],
            gameInfo[x][1],
            gameInfo[x][5],
        )
        )

        rlt = [eventOri[i] for i in rltLisSorted]
        return rlt
    # endFunc
# endClass

def func():
    # !! step2: change function name
    s = Solution()
    myFuncLis = [
        s.getEventsOrder,
        # optional: add another function for comparison
    ]

    onlyDisplayError = True
    enableInput = [True] * testCaseCnt
    input = [None] * testCaseCnt
    expectedRlt = [None] * testCaseCnt
    # enableInput[0] = False
    # enableInput[1] = False
    # enableInput[2] = False
    # enableInput[3] = False
    # enableInput[4] = False
    # enableInput[5] = False

    # !! step3: change input para, input para can be found in "run code" - "test case"
    # ! para1
    # input[0] = parsePara('None')
    input[0] = (
        'EDC',
        'CDE',
        ['Name1 12 G', 'FirstName LastName 43 Y'],
        ['Name3 45+1 S SubName', 'Name4 46 G'],
    )
    expectedRlt[0] = None

    # ! para2
    # input[1] = parsePara('None')
    input[1] = (
        None,
    )
    expectedRlt[1] = None

    # ! para3
    # input[2] = parsePara('None')
    input[2] = (
        None,
    )
    expectedRlt[2] = None

    # ! para4
    # input[3] = parsePara('None')
    input[3] = (
        None,
    )
    expectedRlt[3] = None

    # ! para5
    # input[4] = parsePara('None')
    input[4] = (
        None
    )
    expectedRlt[4] = None

    # ! para6
    # input[5] = parsePara('None')
    input[5] = (
        None
    )
    expectedRlt[5] = None
    # !! ====================================

    # function and parameters count
    allInput = [(input[i], enableInput[i], expectedRlt[i]) for i in range(testCaseCnt)]
    if not input[0]:
        print("ERROR: please assign at least one input for input[0]!")
        exit()
    funcParaCnt = 1 if not isinstance(input[0], tuple) else len(input[0])
    funcCnt = len(myFuncLis)

    # for each test case
    for inputPara, enableInput, expectedRlt in allInput:
        if not enableInput or not inputPara or (isinstance(inputPara, tuple) and not inputPara[0]): continue
        inputParaList = [None] * funcParaCnt

        if not isinstance(inputPara, tuple):
            inputPara = [inputPara]

        for j in range(funcParaCnt):
            inputParaList[j] = inputPara[j]

        # for each function
        for j in range(funcCnt):
            print('==' * 20)
            myFunc = myFuncLis[j]

            # ! manually call function, max para count: 8
            rlt = None
            if funcParaCnt == 1:
                rlt = myFunc(inputPara[0])
            if funcParaCnt == 2:
                rlt = myFunc(inputPara[0], inputPara[1])
            if funcParaCnt == 3:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2])
            if funcParaCnt == 4:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3])
            if funcParaCnt == 5:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4])
            if funcParaCnt == 6:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5])
            if funcParaCnt == 7:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6])
            if funcParaCnt == 8:
                rlt = myFunc(inputPara[0], inputPara[1], inputPara[2], inputPara[3], inputPara[4], inputPara[5], inputPara[6], inputPara[7])

            # only output when the result is not expected
            if onlyDisplayError and expectedRlt is not None and expectedRlt == rlt: continue

            # output function name
            if funcCnt > 1:
                print('func: \t%s' % myFunc.__name__)

            # output para
            for k in range(funcParaCnt):
                para = inputParaList[k]
                if para:
                    formatPrint('input %s:' % (k + 1), para)
                else:
                    print(para)

            # output result
            print()
            if not rlt:
                print('rlt:\t', rlt)
            else:
                formatPrint('rlt:', rlt)
            if expectedRlt is not None:
                if not expectedRlt:
                    print('expRlt:\t', expectedRlt)
                else:
                    formatPrint('expRlt:', expectedRlt)
    print('==' * 20)
# endFunc

def isSpecialInstance(myInstance):
    for curType in [TreeNode, Node]:
        if isinstance(myInstance, curType):
            return True
    return False
# endFunc

def formatPrint(prefix, data):
    if isMatrix(data):
        print('%s' % prefix)
        printMatrix(data)
    else:
        splitter = '\n' if isSpecialInstance(data) else '\t'
        print('%s%s%s' % (prefix, splitter, data))
# endFunc

def main():
    func()
# endMain


if __name__ == "__main__":
    main()
# endIf

# !! ========================== Obsolete Code ==========================
