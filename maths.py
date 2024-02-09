"""Sheriff against robber
A sheriff has 180 km/h car.
A bank robber has 150 km/h car and 5 minutes head start.
How long does it take the sheriff to catch the robber ?
What distance will they have traveled at that point ?
(for simplicity, let's ignore acceleration, traffic, etc.)
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


matplotlib.use('TkAgg')
plt.style.use('dark_background')


TIME_IN_MIN = np.linspace(0, 60, 61)


def print_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(result)
        return result
    return wrapper


def visualize_function(function):
    def wrapper(*args, **kwargs):
        distance = function(TIME_IN_MIN, *args, **kwargs)
        plt.plot(
            TIME_IN_MIN,
            distance,
            label=function.__name__,
            color='b'
        )
        plt.grid(True)
        plt.axhline(0, color='white', lw=2)
        plt.axvline(0, color='white', lw=2)
        plt.xlabel('Time in Minutes')
        plt.ylabel('Distance in Kilometers')
        plt.title('Distance over Time')
        return distance
    return wrapper


@visualize_function
def calculate_distance_vs_time(time_in_min, speed_kilometers_per_hour, start_delay_min=0):
    time_in_hours = np.maximum(0, time_in_min - start_delay_min) / 60
    return speed_kilometers_per_hour * time_in_hours


@print_result
def find_intersection(distance1, distance2):
    for i in TIME_IN_MIN:
        if int(i) > 0 and distance1[int(i)] == distance2[int(i)]:
            return distance1[int(i)], TIME_IN_MIN[int(i)]


if __name__ == "__main__":
    sheriff = calculate_distance_vs_time(speed_kilometers_per_hour=180, start_delay_min=5)
    robber = calculate_distance_vs_time(speed_kilometers_per_hour=150)
    distance, time = find_intersection(sheriff, robber)
    print(f"the sheriff catch the robber at {distance}kms and {time}mins")
    plt.show()

