from grid_map import create_grid
from astar import astar
from robot import Robot

grid = create_grid()

start = (0,0)
goal = (19,19)

path = astar(grid,start,goal)

robot = Robot(grid,path)

robot.navigate()
