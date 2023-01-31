# Daniela L Sanchez, dls4848
# This is the generate_sites.py file

import json
import random

# function that will generate random lat/long values
def rand_lat_lon():

    """
    This function will generate random latigtude and longitude for the specified range.

        Args:
            This function does not take in any arguments.

        Returns:
            random.uniform(16.0, 18.0) (float): This is a random latitude float
            random.uniform(82.0, 84.0) (float): This is a random longitude float
    """

    return(random.uniform(16.0, 18.0), random.uniform(82.0, 84.0))

# dinfing a list of possible compositions for the meteors
composition = ["stony", "iron", "stony-iron"]

# creating a list of dictionaries for each meteorite site
sites = []


for i in range(1, 6):
    lat, lon = rand_lat_lon()
    comp = random.choice(composition)
    site = {"site_id": i, "latitude": lat, "longitude": lon, "composition": comp}
    sites.append(site)

# creating dictionary with the data
data = {"sites": sites}

# save data to json file
with open("meteorite_sites.json", "w") as f:
    json.dump(data, f)
