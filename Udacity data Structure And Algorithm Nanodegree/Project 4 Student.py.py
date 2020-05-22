import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    cameFrom = {}
    costTillNow = {}
    cameFrom[start] = None
    costTillNow[start] = 0
    Frontier = [(0, start)]

    while len(Frontier) > 0:
        node = heapq.heappop(Frontier)[1]

        if node == goal:
            break

        for neighbour in M.roads[node]:
            PCost = distance(M.intersections[node], M.intersections[neighbour])
            NewCost = costTillNow[node] + PCost

            if neighbour not in costTillNow or NewCost < costTillNow[neighbour]:
                cameFrom[neighbour] = node
                costTillNow[neighbour] = NewCost
                heapq.heappush(Frontier, (NewCost, neighbour))

    return ShortestlengthPath(cameFrom, start, goal)

#The past cost is the distance between the two states

def distance(start, end):

    return math.hypot(end[0] - start[0], end[1] - start[1])


def ShortestlengthPath(cameFrom, start, Goal): #Function to find the best Route

    node = Goal
    path = []

    if node not in cameFrom:
        print('Node: {node} not found in map.')
        return

    while node != start:
        path.append(node)
        node = cameFrom[node]
    path.append(start)
    path.reverse()
    print(path)
    return path


# Test Cases
map_10 = load_map("map-10.pickle")
map_40 = load_map("map-40.pickle")

shortest_path(map_40, 8, 24)

shortest_path(map_10, 2, 0)

shortest_path(map_10, 3, 9)
