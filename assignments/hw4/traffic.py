"""
Name: Caroline Greer
traffic.py

Problem: Calculate and output average number of vehicles traveling on each road

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def main():
    num_roads = int(input("How many roads were surveyed? "))
    total_veh = 0
    average_per_road = 0
    for road_number in range(num_roads):
        total_road = 0
        enter_days = int(input("How many days was road " + str(road_number + 1) + " surveyed?"))
        for cars in range(enter_days):
            enter_cars = int(input("How many cars traveled on day " + str(cars + 1) + "?"))
            total_veh = total_veh + enter_cars
            total_road = total_road + enter_cars
        average = total_road / enter_days
        print("Road " + str(num_roads) + " average vehicles per day: ", round(average, 2))
    average_per_road = total_veh / num_roads
    print("total number of vehicles traveled on all roads: ", round(total_veh, 2))
    print("average number of vehicles per roads: ", round(average_per_road, 2))

if __name__ == "__main__":
    main()
