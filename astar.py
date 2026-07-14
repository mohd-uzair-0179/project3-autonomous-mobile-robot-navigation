import heapq

def heuristic(a,b):

    return abs(a[0]-b[0])+abs(a[1]-b[1])

def astar(grid,start,goal):

    rows,cols=grid.shape

    pq=[]

    heapq.heappush(pq,(0,start))

    came={}

    cost={start:0}

    while pq:

        _,current=heapq.heappop(pq)

        if current==goal:

            break

        x,y=current

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:

            nx=x+dx

            ny=y+dy

            if 0<=nx<rows and 0<=ny<cols:

                if grid[nx][ny]==1:

                    continue

                new_cost=cost[current]+1

                if (nx,ny) not in cost or new_cost<cost[(nx,ny)]:

                    cost[(nx,ny)]=new_cost

                    priority=new_cost+heuristic((nx,ny),goal)

                    heapq.heappush(pq,(priority,(nx,ny)))

                    came[(nx,ny)]=current

    path=[]

    current=goal

    while current!=start:

        path.append(current)

        current=came[current]

    path.append(start)

    path.reverse()

    return path
