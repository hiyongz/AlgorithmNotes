#!/usr/bin/python3
#-*-coding:utf-8-*-

#  图的DFS、BFS遍历
from collections import defaultdict
 
class Graph:
    def __init__(self): 
        # 使用字典保存图
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        # 用于给图添加边（连接）
        self.graph[u].append(v)
 
    def DFSTrav(self, v, visited): 
        # 标记已经访问过的节点
        visited.append(v)
         
        # 访问当前节点的相邻节点
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSTrav(neighbour, visited)
 
    def DFS(self, v): 
        # 初始化保存已访问节点的集合
        visited = []
 
        # 递归遍历节点
        self.DFSTrav(v, visited)
        print(visited) 
    
    def DFS2(self, v): 
        # 初始化保存已访问节点的集合
        visited = []
        stack = []
        stack.append(v)
        visited.append(v)
        while stack:            
            # 访问当前节点邻居节点的第一个节点，如果没有访问，标记为已访问并入栈           
            for i in self.graph[v]:
                if i not in visited:
                    visited.append(i)                                    
                    stack.append(i)
                    break            
            # 如果当前节点所有邻居节点都已访问，将当前节点弹出（出栈）
            v = stack[-1]
            if set(self.graph[v]) < set(visited):
                stack.pop()
        print(visited)   
    # BFS遍历
    def BFS(self, v):
        # 新建一个队列
        queue = []
 
        # 将访问的节点入队
        queue.append(v)
        visited = []
        visited.append(v)
        while queue: 
            # 节点出队
            v = queue.pop(0)

            # 访问当前节点的相邻节点，如果没有访问，标记为已访问并入队
            for i in self.graph[v]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        print(visited)

if __name__ == "__main__": 
    # 新建图
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 0)
    graph.addEdge(2, 0)
    graph.addEdge(3, 0)
    graph.addEdge(1, 4)
    graph.addEdge(2, 4)
    graph.addEdge(3, 2)
    graph.addEdge(4, 1)
    graph.addEdge(4, 2)
    graph.addEdge(4, 3)
    
    # DFS遍历图：指定一个起点
    graph.DFS(0)
    graph.DFS2(0)

    # BFS遍历图：指定一个起点
    graph.BFS(0)









