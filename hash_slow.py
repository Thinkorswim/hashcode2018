import numpy as np
import queue as Q
import sys

time = 0

R, C, F, N, B, T = 0, 0, 0, 0, 0, 0

class Ride:
    def __init__(self, start_coords, end_coords, start_time, end_time, index):
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.start_time = start_time
        self.end_time = end_time
        self.index = index

    def __repr__(self):
        res = 'Ride with start coords: {}, end coords: {}, start time: {}, end time: {}'.format(self.start_coords, self.end_coords, self.start_time, self.end_time)
        return res


class Vehicle:
    def __init__(self, current_coordinates):
        self.current_coordinates = current_coordinates
        self.finish_time = 0
        self.completed = []

    def __lt__(self, other):
        return self.finish_time < other.finish_time

def sort_rides(rides):
    rides_sorted = sorted(rides, key=lambda x: (x.end_time, x.start_time), reverse=False)
    return rides_sorted

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def utility(ride, vehicle):
    if (distance(ride.start_coords, ride.end_coords) + distance(ride.start_coords, vehicle.current_coordinates) + time > ride.end_time):
        return -sys.maxsize -1
    utility = 100-(ride.start_time+distance(ride.start_coords, vehicle.current_coordinates)-time)
    if (distance(ride.start_coords, vehicle.current_coordinates)+time < ride.start_time):
        global B
        utility += B*10

    utility += distance(ride.start_coords, ride.end_coords) * 0.5;
    return utility;


def read_data(dataset="data"):
    # R – number of rows of the grid (1 ≤ R ≤ 10000)
    # C – number of columns of the grid (1 ≤ C ≤ 10000)
    #F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
    # N – number of rides (1 ≤ N ≤ 10000)
    # ● B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
    # ● T – number of steps in the simulation (1 ≤ T ≤ 10 )

    isFirst = True
    rides = []
    vehicles = Q.PriorityQueue()
    vehiclesArray = []
    index = 0


    f=open(dataset, 'r')
    for line in f.readlines():
        intLine = [int(s) for s in line.split(' ')]

        if isFirst:
            global R; global C; global F; global N; global B; global T
            R = intLine[0]
            C = intLine[1]
            F = intLine[2]
            N = intLine[3]
            B = intLine[4]
            T = intLine[5]

            isFirst = False

        else:
            rides.append(Ride((intLine[0], intLine[1]), (intLine[2], intLine[3]), intLine[4], intLine[5], index))
            index += 1


    for i in range(F):
        v_new = Vehicle((0,0))
        vehicles.put(v_new)
        vehiclesArray.append(v_new)

    return R, C, F, N, B, T, rides, vehicles, vehiclesArray

if __name__ == '__main__':
    R, C, F, N, B, T, rides, vehicles, vehiclesArray  = read_data("e_high_bonus.in")


    while not vehicles.empty():
        v = vehicles.get()
        time = v.finish_time
        utils = []

        if not len(rides):
            break

        for ride in rides:
            utils.append((utility(ride,v),ride))

        utils = sorted(utils, key=lambda x: x[0], reverse=True)
        best = utils[0][1]
        if not (utils[0][0] == -sys.maxsize -1):
            v.finish_time = time + distance(v.current_coordinates, best.start_coords) + distance(best.end_coords, best.start_coords)

            if (v.finish_time <= T):
                v.completed.append(best.index);
                v.current_coordinates = best.end_coords
                rides.remove(best)
                vehicles.put(v)

        # print(time)

    for v in vehiclesArray:
        print(str(len(v.completed)) + " " + str(" ".join([str(x) for x in v.completed])))
