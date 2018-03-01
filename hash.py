import numpy as np


class Ride:
    def __init__(self, start_coords, end_coords, start_time, end_time):
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.start_time = start_time
        self.end_time = end_time

def read_data(dataset="data"):
    # R – number of rows of the grid (1 ≤ R ≤ 10000)
    # ● C – number of columns of the grid (1 ≤ C ≤ 10000)
    # ● F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
    # ● N – number of rides (1 ≤ N ≤ 10000)
    # ● B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
    # ● T – number of steps in the simulation (1 ≤ T ≤ 10 )

    isFirst = True
    rides = []


    f=open(dataset, 'r')
    for line in f.readlines():
        intLine = [int(s) for s in line.split(' ')]

        if isFirst:
            R = intLine[0]
            C = intLine[1]
            F = intLine[2]
            N = intLine[3]
            B = intLine[4]
            T = intLine[5]

            isFirst = False

        else:
            rides.append(Ride((intLine[0], intLine[1]), (intLine[2], intLine[3]), intLine[4], intLine[5]))

    return R, C, F, N, B, T, rides

if __name__ == '__main__':
    R, C, F, N, B, T, rides  = read_data("a_example.in.txt")

    print(rides[0])
