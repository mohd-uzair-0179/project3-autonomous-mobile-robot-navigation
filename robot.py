import matplotlib.pyplot as plt

from lidar import simulate_lidar

class Robot:

    def __init__(self,grid,path):

        self.grid=grid

        self.path=path

    def navigate(self):

        plt.imshow(self.grid,cmap="gray_r")

        x=[]

        y=[]

        for p in self.path:

            simulate_lidar(p)

            x.append(p[1])

            y.append(p[0])

        plt.plot(x,y,'r',linewidth=2)

        plt.scatter(x[0],y[0],c='green',label='Start')

        plt.scatter(x[-1],y[-1],c='blue',label='Goal')

        plt.legend()

        plt.title("Autonomous Robot Navigation")

        plt.show()
