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
        i, l = 0, x

        while i <= l:
            mid = i+(l - i) // 2
            if l == 1:
                return 1
            if (l - i)//2 <= 2 and (mid+1)*(mid+1)>x:                
                return mid
            if mid * mid <= x:
                i = mid
            else:
                l = mid

def func():
    s = Solution()

    # !! step1: change function name and para here
    inputParaLis1 = [
        2147483647]
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
    # print((0-0)//2)
# end_main


if __name__ == "__main__":
    main()
# end_if
