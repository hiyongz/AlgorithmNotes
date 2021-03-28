#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/31 21:39
# @Author:  haiyong
# @File:    groupAnagrams.py
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        init_dict = collections.defaultdict(list)
        for s in strs:
            init_dict[tuple(sorted(s))].append(s)
        return list(init_dict.values())
if __name__ == "__main__":
    Solu = Solution()
    result = Solu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(list(result))