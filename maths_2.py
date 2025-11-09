"""Sheriff against robber
A sheriff has 180 km/h car.
A bank robber has 150 km/h car and 5 minutes head start.
How long does it take the sheriff to catch the robber ?
What distance will they have traveled at that point ?
(for simplicity, let's ignore acceleration, traffic, etc.)
"""


from functools import partial



robber_speed_km_by_hour: float = 150.0
sherif_speed_km_by_hour: float = 180.0



def traveled_distance_at_target_time(target_time_in_min: int, speed_km_by_hour: float, delay_in_min: int = 0) -> float:
    return speed_km_by_hour / 60 * (target_time_in_min - delay_in_min)


def find_intersection(func_1: callable, func_2: callable) -> int | None:
    for min in range(0, 60):
        if func_1(min) == func_2(min):
            return min



if __name__ == "__main__":
    print("--- Start résolution ---")

    robber_distance_trajectory = partial(
        traveled_distance_at_target_time, speed_km_by_hour=robber_speed_km_by_hour
    )
    sherif_distance_trajectory = partial(
        traveled_distance_at_target_time, speed_km_by_hour=sherif_speed_km_by_hour, delay_in_min=5
    )

    intersection_in_min: int | None = find_intersection(func_1=robber_distance_trajectory, func_2=sherif_distance_trajectory)

    robber_distance_traveled: float = traveled_distance_at_target_time(target_time_in_min=intersection_in_min, speed_km_by_hour=robber_speed_km_by_hour)
    sherif_distance_traveled: float = traveled_distance_at_target_time(target_time_in_min=intersection_in_min, speed_km_by_hour=sherif_speed_km_by_hour, delay_in_min=5)

    print("robber distance traveled", robber_distance_traveled)
    print("sherif distance traveled", sherif_distance_traveled)
    print("Intersection is at", intersection_in_min, "mins")

