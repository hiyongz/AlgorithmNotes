#-*-coding:utf-8-*-
def shortest_len(N,M,Dim,map):
    dp = [list(Dim) for Dim in map]
    last_dp = [list(Dim) for Dim in map]
    for k in range(M - 1):
        for i in range(N):
            for j in range(N):
                tmp = [last_dp[i][Dim] + map[Dim][j] for Dim in range(N) if Dim != i and Dim != j]
                dp[i][j] = min(tmp)
        # copy
        last_dp = [list(x) for x in dp]
    return dp

if __name__ == '__main__':
    N = int(raw_input())
    M = int(raw_input())
    Dim = raw_input()
    map = []
    for i in range(N):
        #line = int(raw_input().split())
        line = [int(k) for k in raw_input().split()]
        map.append(list(line))

    dp = shortest_len(N, M, Dim, map)
    print dp