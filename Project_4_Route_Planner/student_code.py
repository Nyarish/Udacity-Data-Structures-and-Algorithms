# References:
"""
In this project i have relied and got help from the below sources.The materials i used inspired me on to complete this project. I would like to credit and provide citation for the python code and other sources used in this project as below. 

References:

1. Udacity Lesson 4 A* Search from 11 - 16. Here is a link to the classroom. I also relied on help from the Udacity`s knowledge and chat forum for this project. 
https://classroom.udacity.com/nanodegrees/nd256/parts/94ec3f1b-f3ae-4de4-acbc-ec4b27548116/modules/7de98578-b282-48ef-bc47-3167f88582f8/lessons/152f5916-4ec3-4881-9f76-8e3c77213e34/concepts/d238bdfa-f49f-4f95-a14b-44a2e9cb184d

2. I relied on a similar project done on the python code. Here is the link to the source of my python work. https://github.com/fastalana/AStar/blob/master/route_planner.py

3. I also relied on links and artciles from this sources https://www.redblobgames.com/pathfinding/a-star/implementation.html


"""


import math
import heapq


# These code is inspired from https://github.com/fastalana/AStar/blob/master/route_planner.py

def shortest_path(M,start,goal):
    
    print("shortest path called")
    
    # Example show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])
    
    # initial state
    path = {start:0} # {5:34}
    cost_to_path = {start:0} # {5:34} which is road distance 
    
    # A* works by getting the minimum distance between a start and goal.
    # The variable frontier tracks where in the map it is covering 
    frontier = [(0, start)]
    
    # Here the frontier starts traversing the path to the goal=34
    while len(frontier) > 0:
        # first node to be checked is 5
        node = heapq.heappop(frontier)[1]
        
        if node == goal: # terminate search else continue
            break
            
        for other_paths in M.roads[node]:
            """
            Example
            show_map(map_40, start=5, goal=34)
            
            M.roads[node=5] = [32, 14, 5] == M.intersections
            
            The path_cost gets the cost (distance) 
            for the node and each intersections[32, 14, 5],
            to get the min cost distnace
            
            """
            path_cost = get_distance(M.intersections[node],M.intersections[other_paths])
            new_cost = cost_to_path[node] + path_cost
            
            # A* finds the lowest cost if h(s) < true cost
            # where "h" should never overestimate the distance to goal
            if other_paths not in cost_to_path or new_cost < cost_to_path[other_paths]:
                
                # update the dictionary
                path[other_paths] = node # {5: 34, 16: 34}
                cost_to_path[other_paths] = new_cost
                heapq.heappush(frontier, (new_cost, other_paths))
                
   
    
    return get_best_path(path, start, goal)

# Helper functions

def get_best_path(path, start, goal):
    """
    This function finds the optimal path on the map by doing a bach search. 
    """
    if goal not in path:
        return(f"Goal destination {goal} not found on map.")
    node = goal
    _path = []
    
    while node != start:
        _path.append(node)
        node = path[node]
    _path.append(start)
    _path.reverse()
    
    return _path


def get_distance(start, end):
    """
    calculates distance between 2 nodes
    """
    return (math.hypot(end[0] - start[0], end[1] - start[1]))