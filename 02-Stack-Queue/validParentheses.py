#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/30 15:23
# @Author:  haiyong
# @File:    validParentheses.py
class Solution:
    def isValid(self, s: str) -> bool:
        parth = {'{': '}', '[': ']', '(': ')',0: None,}
        stack = [0]
        for par in s:
            if par in parth:
                stack.append(par)
            else:
                parth_pop = stack.pop(-1)   # 出栈：删除最后一个元素
                if parth[parth_pop] != par:
                    return False
        return len(stack) == 1


if __name__ == "__main__":
    Solu = Solution()
    result = Solu.isValid("()")
    print(result)
