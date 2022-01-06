from collections import deque
import collections
from typing import DefaultDict, List


class Solution:
    from collections import defaultdict, deque
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Base case
        if source == target:
            return 0
        # Creating graph or routes
        graph = DefaultDict(set)
        
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

    def numBusesToDestination2(self, routes: List[List[int]], S: int, T: int) -> int:
        # https://leetcode.com/problems/bus-routes/discuss/256518/A-Different-Python-BFS-Solution-All-in-a-Graph
        if S == T: return 0
        
        # Builds graph.
        graph = collections.defaultdict(list)  # Don't use set. See below.
        for bus, stops in enumerate(routes):
            bus = -bus - 1  # To avoid conflict with the stops.
            
            # `set.update` consumes extra memory, so a `list` is used instead.
            graph[bus] = stops
            for s in stops:
                graph[s].append(bus)

        # Does BFS.
        dq = collections.deque()
        dq.append((S, 0))
        seen = set([S])
        while dq:
            node, depth = dq.popleft()
            for adj in graph[node]:
                if adj in seen: continue
                if adj == T: return depth
                # If `adj` < 0, it's a bus, so we add 1 to `depth`.
                dq.append((adj, depth + 1 if adj < 0 else depth))
                seen.add(adj)
        return -1