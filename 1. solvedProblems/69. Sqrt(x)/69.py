# !/usr/bin/env python
# coding: utf-8
"""
1.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    Sat, 08/29/2020, 21:46
Link:

Description:

    Implement int sqrt(int x).

    Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

    Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

    Example 1:

    Input: 4
    Output: 2
    Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since
                the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = l + (r - l) // 2
            if m ** 2 == x:
                return m
            elif m ** 2 > x:
                r = m - 1
            else:
                l = m + 1
        
        return l - 1
                    

    def mySqrt1(self, x: int) -> int:
        l = 0
        r = x
        m = (l + r) // 2

        while l <= r:
            if m ** 2 == x:
                return m
            else:
                if m ** 2 > x:
                    r = m - 1
                else:
                    l = m + 1
            m = min((l + r) // 2, r)
        return m

def func():
    s = Solution()

    # !! step1: change function name and para here
    inputParaLis1 = [8, 1]
    # inputParaLis2 = []
    # inputParaLis3 = []
    myFuncLis = [
        s.mySqrt,
        ]

    paraCnt = len(inputParaLis1)
    funcCnt = len(myFuncLis)
    for i in range(paraCnt):
        inputPara1 = inputParaLis1[i]
        # inputPara2 = inputParaLis2[i]
        # inputPara3 = inputParaLis3[i]

        for j in range(funcCnt):
            myFunc = myFuncLis[j]
            rlt = myFunc(inputPara1)
            print('func: \t%s' % myFunc.__name__)
            print('input1:\t%s' % inputPara1)
            # print('input2: %s' % inputPara2)
            # print('input3: %s' % inputPara3)
            print('rlt: \t%s' % rlt)
            print('==' * 20)


# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
