from collections import deque
import collections
from typing import List


class Solution:
    from collections import defaultdict, deque
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Base case
        if source == target:
            return 0
        # Creating graph or routes
        graph = collections.defaultdict(set)
        
        # Since index represents bus_number on a route
        # suppose i is bus number and stops are the values present at that index
        for bus_number, stops in enumerate(routes):
            # for each stop adding buses going to that stop
            for stop in stops:
                graph[stop].add(bus_number)
        
        # Using bfs
        bfs = deque([(source, 0)])
        
        # visited stops 
        seen_stops = set()
        # visited buses
        seen_buses = set()
        
        while bfs:
            stop, count = bfs.popleft()
            # Resulting case
            if stop == target:
                    return count
                
            # Since our graph stores all buses going to a stop
            # We will iterate for every bus
            for bus_number in graph[stop]:
                # We dont want to travel in same bus as we might stuck into loop and reach nowhere
                if bus_number not in seen_buses:
                    seen_buses.add(bus_number)
                    
                    # Now we are in a bus, so we will travel all the stops that bus goes to but again, we only want to go to stops we haven't visited
                    for stop in routes[bus_number]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            bfs.append((stop, count + 1))
        return -1

    def numBusesToDestination2(self, routes: List[List[int]], source: int, target: int) -> int:
        # 如果起点和终点相同则不需要坐地铁
        if source == target:
            return 0
        # 建图
        graph = collections.defaultdict(set) # 使用字典保存图

        # 以车站作为节点，每个车站对应能经过它的地铁
        for routes_number, stations in enumerate(routes):
            for station in stations:
                graph[station].add(routes_number)

        # 进行广度优先搜索
        queue = deque([(source, 0)])# 新建一个队列（起点，记录经过的地铁线）
        visited_stations = set() # 已经经过的车站
        visited_routes = set() # 已经经过的铁路线

        while queue:
            station, count = queue.popleft() # 节点出队
            if station == target:
                return count
            # 遍历经过当前车站的铁路线
            for routes_number in graph[station]:
                if routes_number not in visited_routes:
                    visited_routes.add(routes_number)
                    # 访问当前铁路线的所有车站，如果没有访问，标记为已访问并入队
                    for station in routes[routes_number]:
                        if station not in visited_stations:
                            visited_stations.add(station)
                            queue.append((station, count + 1))
        return -1