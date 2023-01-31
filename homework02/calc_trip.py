# Daniela L Sanchez, dls4848
#this is calculate_trip.py file

import json
import math

radius_of_mars = 3389.5 # this value is in km

def calculate_gdc(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    This function will calculate the distance between the latitude and longitude points
    using the great-circle distance algorithm. This function was kindly provided by the
    COE332 professors on slack.

        Args:
            latitude_1 (float): This is a randomly generated lat value calculated in
                                the acompanying script.
            longitude_1 (float): This is a randomly generated long value calulated in
                                the acompanying script.
            latitude_2 (float): This is a randomly generated lat value calculated in
                                the acompanying script.
            longitude_2 (float): This is a randomly generated long value calculated in
                                the acompanying script.


        Returns:
            radius_of_mars * d_sigma (float): This value is the calcuated value of the
                                distance between two points using the great_circle
                                distance algorithm
    """

    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return (radius_of_mars * d_sigma)

with open("meteorite_sites.json", "r") as f:
    data = json.load(f)

                                                                                                                                                                                                # initializing lat/lon start points
lat_start = 16.0
lon_start = 82.0


speed = 10 # this value is in km/hr

sample_times = {"stony":1, "iron":2, "stony-iron": 3}

total_time = 0

for i, site in enumerate(data["sites"]):
    # calculate distance to the next site
    distance = calculate_gdc(lat_start, lon_start, data['sites'][i]['latitude'], data['sites'][i]['longitude'])

    # convert distance to hours
    travel_time = distance / speed
    total_time += travel_time

    # time to sample
    sample_time = sample_times[site["composition"]]
    total_time += sample_time

    # print information for each leg of the trip
    print(f"leg {i+1}: time to travel = {travel_time:.2f} hr, time to sample = {sample_time} hr")
    start_lat = site

# print summary
print("=========================================")
print(f"number of legs: {len(data['sites'])}, total time elapsed: {total_time} hr")
