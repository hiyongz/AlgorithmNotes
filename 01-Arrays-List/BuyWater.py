#!/usr/bin/python3
#-*-coding:utf-8-*-

class Solution:
    def BuyWater(self, n):
        """
        题目描述：2块钱买一瓶水，2个空瓶可以换一瓶水，3个瓶盖可以换一瓶水,n块钱最终可以得到多少瓶水
        """
        self.money = n
        self.water = 0
        self.bottle = 0
        self.cap = 0

        def buy():
            self.money = self.money - 2
            self.water = self.water + 1
            self.bottle = self.bottle + 1
            self.cap = self.cap + 1
            if self.money >= 2:
                buy()
            if self.cap >=3:
                self.cap = self.cap -3
                buy()
            if self.bottle >= 2:
                self.bottle = self.bottle - 2
                buy()

        buy()
        print(self.water)
        print(self.money)

    def BuyWater2(self, n):
        """
        题目描述：2块钱买一瓶水，3个瓶盖可以换一瓶水,n块钱最终可以得到多少瓶水
        """
        self.money = n
        self.water = 0
        self.cap = 0

        def buy():
            self.money = self.money - 2
            self.water = self.water + 1
            self.cap = self.cap + 1
            if self.money >= 2:
                buy()
            if self.cap >=3:
                self.cap = self.cap -3
                buy()
        buy()
        print(self.water)
        print(self.money)
if __name__ == "__main__":
    Solu = Solution()
    result = Solu.BuyWater2(6)
    print(result)







