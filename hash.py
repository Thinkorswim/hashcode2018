import numpy as np

time = 0

R, C, F, N, B, T = 0, 0, 0, 0, 0, 0 

class Ride:
    def __init__(self, start_coords, end_coords, start_time, end_time):
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        res = 'Ride with start coords: {}, end coords: {}, start time: {}, end time: {}'.format(self.start_coords, self.end_coords, self.start_time, self.end_time)
        return res


class Vehicle:
    def __init__(self, current_coordinates):
        self.current_coordinates = current_coordinates
        self.finish_time = 0;

def sort_rides(rides):
    rides_sorted = sorted(rides, key=lambda x: (x.end_time, x.start_time), reverse=False)
    return rides_sorted

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def utility(ride, vehicle):
    if (distance(ride.start_coords, ride.end_coords) + distance(ride.start_coords, vehicle.current_coordinates) + time > ride.end_time):
        return 0
    utility = 100-(ride.start_time+distance(ride.start_coords, vehicle.current_coordinates)-time)
    if (distance(ride.start_coords, vehicle.current_coordinates)+time < ride.start_time):
        global B
        utility += B /10

    utility += distance(ride.start_coords, ride.end_coords) * 0.5;
    return utility;


def read_data(dataset="data"):
    # R – number of rows of the grid (1 ≤ R ≤ 10000)
    # ● C – number of columns of the grid (1 ≤ C ≤ 10000)
    # ● F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
    # ● N – number of rides (1 ≤ N ≤ 10000)
    # ● B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
    # ● T – number of steps in the simulation (1 ≤ T ≤ 10 )

    isFirst = True
    rides = []
    vehicles = []


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
            rides.append(Ride((intLine[0], intLine[1]), (intLine[2], intLine[3]), intLine[4], intLine[5]))


    for i in range(F):
        vehicles.append(Vehicle((0, 0)))

    return R, C, F, N, B, T, rides, vehicles

if __name__ == '__main__':
    R, C, F, N, B, T, rides, vehicles  = read_data("a_example.in")

    print(rides[0])

    r1 = Ride(None, None, 2, 5)
    r2 = Ride(None, None, 3, 5)
    r3 = Ride(None, None, 1, 10)

    print(sort_rides([r2, r3, r1]))
