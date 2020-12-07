# !/usr/bin/env python
# coding: utf-8
"""
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sun, 08/30/2020, 19:16
# !! Description:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List

class Solution:
    def list2int(self, myList):
        cnt = len(myList)
        myInt = 0
        for i in range(cnt):
            myInt = myInt * 10 + myList[i]
        return myInt

    def int2list(self, myInt):
        myList = []
        while myInt > 0:
            curDigit = myInt % 10
            myList.append(curDigit)
            myInt = myInt // 10
        myList.reverse()
        return myList

    def plusOne(self, digits: List[int]) -> List[int]:
        myInt = self.list2int(digits)
        myInt += 1
        myList = self.int2list(myInt)
        return myList


# end_class

def func():
    s = Solution()

    # !! change function name and para here
    inputParaLis1 = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [0],
        ]
    # inputParaLis2 = []
    # inputParaLis3 = []
    myFuncLis = [
        s.plusOne,
        ]

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
            print('rlt: \t%s' % rlt)
            print('==' * 20)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
