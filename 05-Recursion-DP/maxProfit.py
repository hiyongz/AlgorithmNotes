#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/11/11 13:38
# @Author:  haiyong
# @File:    maxProfit.py
from typing import List


from typing import List
class Solution:
    def maxProfit(self, k, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k > n//2: # 交易次数是无限次
            profit = 0
            for i in range(n-1):
                if prices[i+1] > prices[i]:
                    profit += prices[i+1] - prices[i]
            return profit

        d = dict()
        # index表示当前是哪天，status是买卖状态，coutnt为交易次数
        def dfs(index,status,count):
            if (index,status,count) in d:
                return d[index,status,count]
            if index==n or count==k:
                d[index,status,count] = 0
                return 0
            a, b, c = 0, 0, 0
            # 不动
            a = dfs(index+1,status,count)
            if status:
                # 卖，交易次数 +1，将交易状态设置为0
                b = dfs(index+1,0,count+1)+prices[index]
            else:
                # 买，将交易状态设置为1
                c = dfs(index+1,1,count)-prices[index]
            d[index,status,count] = max(a,b,c)
            print(d[index, status, count])
            return d[index,status,count]
        return dfs(0,0,0)

    def maxProfit2(self, k, prices):
        if not prices:
            return 0
        n = len(prices)
        # 当k非常大时转为无限次交易
        if k>n//2:
            dp0,dp1 = 0,-prices[0]
            for i in range(1,n):
                tmp = dp0
                dp0 = max(dp0,dp1+prices[i])
                dp1 = max(dp1,dp0-prices[i])
            return max(dp0,dp1)
        # 定义二维数组，交易了多少次、当前的买卖状态
        dp = [[0,0] for _ in range(k+1)]
        for i in range(k+1):
            dp[i][1] = -prices[0]
        for i in range(1,n):
            for j in range(1,k+1):
                # 处理第k次买入
                dp[j-1][1] = max(dp[j-1][1],dp[j-1][0]-prices[i])
                # 处理第k次卖出
                dp[j][0] = max(dp[j][0],dp[j-1][1]+prices[i])
        return dp[-1][0]

    def maxProfit3(self, k, prices):
        n = len(prices)
        if not n: return 0
        max_profit = 0
        if k >= n / 2:
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        dp = [[0 for j in range(n)] for i in range(k + 1)]
        for i in range(1, k + 1):
            sell = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], sell + prices[j])
                sell = max(sell, -prices[j] + dp[i - 1][j])
        return dp[-1][-1]
if __name__ == "__main__":
    solu = Solution()
    k = 2
    prices = [7,1,5,3,6,4,8]
    result = solu.maxProfit3(k, prices)
    print(result)

