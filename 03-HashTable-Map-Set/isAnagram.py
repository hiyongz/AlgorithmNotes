#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/6 15:23
# @Author:  haiyong
# @File:    isAnagram.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            if d.get(ch, 0) == 0: return False
            d[ch] -= 1
            if d[ch] == 0: del d[ch]

        return not d

if __name__ == "__main__":
    num = Solution()
    s = "anagram"
    t = "nagaram"
    result = num.isAnagram(s,t)
    print(result)