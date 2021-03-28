#-*-coding:utf-8-*-

if __name__ == '__main__':
    T = int(raw_input())
    NM = [int(i) for i in raw_input().split()]
    temp = True
    count = 0

    while (temp and count < T):
        map = []
        for i in range(NM[0]):
            #line = int(raw_input().split())
            line = [int(k) for k in raw_input().split()]
            map.append(list(line))
        maps = [[0] * NM[1] for _ in range(NM[1])]
        for v in map: maps[v[0]][v[1]] = 1


        count = count + 1








    m = int(raw_input())
    x = raw_input()
    map = []
    for i in range(n):
        line = [int(x) for x in raw_input().split()]
        map.append(list(line))
    dp = [list(x) for x in map]  # 一维列表浅拷贝用list(),二维列表浅拷贝用[list(x) for x in dp]  三维用[[list(i) for i in x] for x in dp]
    last_dp = [list(x) for x in map]
    for k in range(m - 1):  # 共循环m-1轮，每一次循环后的dp矩阵元素代表i和j之间的长度为m的最短路径
        for i in range(n):
            for j in range(n):
                tmp = [last_dp[i][x] + map[x][j] for x in range(n) if x != i and x != j]
                dp[i][j] = min(tmp)
        # copy
        last_dp = [list(x) for x in dp]

    print dp

    temp = True
    count = 0
    while (temp and count < 5):
        (x, y) = (int(x) for x in raw_input().split())
        ary1 = raw_input().split()
        ary2 = raw_input().split()
        ary1.extend(ary2)
        ary3 = []
        ary3 = [int(i) for i in ary1]
        ary4 = []
        ary4 = list(set(ary3))  # set无序不重复元素集, 基本功能包括关系测试和消除重复元素
        ary4.sort()
        ary5 = []
        ary5 = [str(i) for i in ary4]
        print (' '.join(ary5))
        count = count + 1