#!/usr/bin/python3
#-*-coding:utf-8-*-

class Solution(object):

    def swap(self, arr, i, j):
        # tmp = arr[i]
        # arr[i] = arr[j]
        # arr[j] = tmp
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    def bubble_sort(self, arr):
        # 冒泡排序
        n = len(arr)
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x = x + 1

            for i in range(1, n-x):
                if arr[i-1] > arr[i]:
                    arr = self.swap(arr, i-1, i)
                    swapped = True
        return arr

    def selection_sort(self, arr):
        # 选择排序
        n = len(arr)
        
        for i in range(0, n):
            min_num = i
            for j in range(i + 1, n):
                # 找到最小值
                if arr[j] < arr[min_num]:
                    min_num = j
            
            # 将找到的最小值与第i个元素交换，也就是将最小元素放到前面
            arr = self.swap(arr, i, min_num)      
        return arr

    def insertion_sort(self, arr):
        # 插入排序
        n = len(arr)
        
        for i in range(0, n):
            pos = i
            # 比较、交换
            while pos > 0 and arr[pos-1] > arr[i]:
                arr = self.swap(arr, pos-1, pos)
                pos -= 1                
        return arr
    def insertion_sort2(self, arr):
        # 插入排序
        n = len(arr)
        
        for i in range(0, n):
            cursor = arr[i]
            pos = i
            # 移动并比较元素
            while pos > 0 and arr[pos-1] > cursor:
                arr[pos] = arr[pos-1]
                pos -= 1
            arr[pos] = cursor
        return arr


        
if __name__ == "__main__":
    Solu = Solution()
    result = Solu.bubble_sort([60, 10, 30, 35, 2, 8, 42, 50, 20, 52])
    print(result)
    result = Solu.selection_sort([60, 10, 30, 35, 2, 8, 42, 50, 20, 52])
    print(result)
    result = Solu.insertion_sort2([60, 10, 30, 35, 2, 8, 42, 50, 20, 52])
    print(result)
