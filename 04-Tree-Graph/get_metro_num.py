#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/1/9 9:45
# @Author:  hiyongz
# @File:    get_metro_num.py
import collections
import sys
from collections import defaultdict
from collections import deque


import os.path
import random


class TestData():
    # 随机生成一个不重复的列表
    def creat_list(self,ll, maxn, lines):
        """
        :param ll: 生成列表长度
        :param maxn: 列表中数的项的最大值
        :lines：代表已有线路
        :return: 返回 --> 生成的列表
        """
        s = []
        while len(s) < ll:
            x = random.randint(1, maxn)
            if x not in s:
                s.append(x)
        # print('s', s)
        return s


    def list_to_str(self,ss):
        sult = ''
        for i in ss:
            if sult == '':
                sult += '%d' % i
            else:
                sult += ',%d' % i
        return sult


    def test_case(self,lines, coun, star,src,des):
        file_path = os.getcwd() + "\\test"
        if os.path.exists(file_path):
            os.chdir(file_path)

        for i in range(star, coun + star):
            filename = 'input%d.txt' % i
            if os.path.exists(filename):
                os.remove(filename)
            fd = open(filename, 'a+')
            fd.write('src = %d, dest = %d' % (src, des))
            fd.flush()

            for j in lines:
                strl = self.list_to_str(j)
                fd.write('\n')
                fd.write('%s' % strl)
                fd.flush()

            fd.close()
    def generate(self):
        # 生成lines中的一项
        # creat_list(10000, 10000)
        # ll_lines = random.randint(1, 10000)
        ll_lines = 1
        lines = []
        print("--------------------------")
        # 随机多少条线路
        # ll = random.randint(1, 10)
        # maxn = random.randint(1, 100)
        ll = 10000 # lines条数
        maxn = 9999 # 最大值
        # 文件结尾
        star = 100
        for m in range(ll):
            # line_length 每一项长度随机
            # if m == 1:
            #     line_length = 600
            # else:
            #     line_length = random.randint(5, 1000)
            line_length = random.randint(1, 1000)
            line = self.creat_list(line_length, maxn, lines)
            if line not in lines:
                lines.append(line)
        # print('lines', lines)
        s1, s2 = random.choices(lines, k=2)
        src, _ = random.choices(s1, k=2)
        des, _ = random.choices(s2, k=2)
        # self.test_case(lines, ll_lines, star,src,des)
        return lines,src,des


class Solution():
    # def __init__(self, input_file, output_file):
    #     self.input_file = input_file
    #     self.output_file = output_file

    def lines_load(self):
        """加载地铁路线数据
        :return:
        """
        src = ''
        dest = ''
        lines = []

        with open(self.input_file, "r+") as input:
            # input_data = input.readlines()
            for line in input.readlines():
                # 读取起点和终点
                if 'src' in line or 'source' in line:
                    src_dst = [input.strip() for input in line.split(",")]
                    for sd in src_dst:
                        res = [s.strip() for s in sd.split("=")]
                        if 'src' in res:
                            src = int(res[1])
                        elif 'dest' in res:
                            dest = int(res[1])
                # 铁路线
                elif 'src' not in line and line != '\n':
                    line2 = eval(line)
                    # lines.append([line2])
                    if isinstance(line2,int):
                        lines.append([line2])
                    else:
                        lines.append(list(line2))

        with open(self.output_file, "r+") as output:
            num_of_lines = output.read().strip()
        return lines, src, dest, int(num_of_lines)

    def get_metro_num_to_dest(self, lines, src, dest):
        # 如果起点和终点相同则不需要坐地铁
        if src == dest:
            return 0
        # 建图
        graph = defaultdict(list) # 使用字典保存图

        # 以车站作为节点，每个车站对应能经过它的地铁
        for lines_number, stations in enumerate(lines):
            for station in stations:
                graph[station].append(lines_number)

        # 进行广度优先搜索
        queue = [(src, 0)] # 新建一个队列（起点，记录经过的地铁线）
        visited_stations = [] # 已经经过的车站
        visited_lines = [] # 已经经过的铁路线

        while queue:
            station, count = queue.pop(0) # 节点出队
            if station == dest:
                return count
            # 遍历经过当前车站的铁路线
            for lines_number in graph[station]:
                if lines_number not in visited_lines:
                    visited_lines.append(lines_number)
                    # 访问当前铁路线的所有车站，如果没有访问，标记为已访问并入队
                    for station in lines[lines_number]:
                        if station not in visited_stations:
                            visited_stations.append(station)
                            queue.append((station, count + 1))
        return -1

    def get_metro_num_to_dest2(self, lines, src, dest):
        # 如果起点和终点相同则不需要坐地铁
        if src == dest:
            return 0
        # 建图
        graph = collections.defaultdict(set) # 使用字典保存图

        # 以车站作为节点，每个车站对应能经过它的地铁
        for routes_number, stations in enumerate(lines):
            for station in stations:
                graph[station].add(routes_number)

        # 进行广度优先搜索
        queue1 = deque()# 新建一个队列（起点，记录经过的地铁线）
        # visited_stations1 = set() # 已经经过的车站
        visited_routes1 = set() # 已经经过的铁路线
        for routes_number in graph[src]:
            queue1.append(routes_number)
            visited_routes1.add(routes_number)

        queue2 = deque()# 新建一个队列（起点，记录经过的地铁线）
        # visited_stations2 = set() # 已经经过的车站
        visited_routes2 = set() # 已经经过的铁路线
        for routes_number in graph[dest]:
            queue2.append(routes_number)
            visited_routes2.add(routes_number)
        count = 0
        while queue1 and queue2:

            # 比较俩队列长度 从短的的队列开始搜索
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited_routes1, visited_routes2 = visited_routes2, visited_routes1

            count = count + 1
            for _ in range(len(queue1)):
                route_index = queue1.popleft() # 节点出队
                if route_index in visited_routes2:
                    return count
                # 遍历经过当前车站的铁路线
                for station in lines[route_index]:
                    for new_route in graph[station]:
                        # 查看 route 是否被访问过 若没有 加入visited 和队列
                        if new_route not in visited_routes1:
                            visited_routes1.add(new_route)
                            queue1.append(new_route)
        return -1

if __name__ == "__main__":
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]
    # input_file = "test/input2.txt"
    # output_file = "test/output2.txt"
    # solu = Solution(input_file, output_file)
    # lines, src, dest, num_of_lines = solu.lines_load()
    solu = Solution()
    d = TestData()
    ll_lines = 1
    for i in range(100000):
        lines, src, dest = d.generate()
        result = solu.get_metro_num_to_dest2(lines, src, dest)
        if int(result) >= 2:
            print("666666666666")
            d.test_case(lines, ll_lines, i, src, dest)
            with open("results.txt", "w") as res_txt:
                res_txt.write(str(result))
                res_txt.write("\n")
    print(src)
    print(dest)
    print(result)
    # assert result == num_of_lines

