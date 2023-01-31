# Daniela L Sanchez, dls4848
# COE332 Homework02: Meteorite Landings

This repository/homework02 is conprised of two different python files that work in conjuction with each other. The purpose of this homework is to practice some of the knowledge 
gained during lecture. Concepts such as creating and calling dictionaries, proper coding documentation, and pushing files to GitHub are all found within this homework project. 
Below you will find a detailed description of the files and code used as well as how to utilize and run said code. It is important to keep all of the following files in one folder 
so the script can have easy acess to  each other as we are calling one file in another.

---

## Script01: generate_site.py

This is the first script in this repository and should be run first. This script will generate random meterite sites based on a couple of requirements. This script will, in 
the end, take all five sites and store them into a 'dictionary' and will make it a JSON file that we can use in the following script.
The requirements for the landing sites are as follows:

        1. give each landing site a set of random latitude and longitude pair between 16.0-18.0 degrees North and 82.0-84.0 degrees East respectively
        2. give each landing site a random composition out of a list ' ["stony", "iron", "stony-iron"] '

As stated previously, this code should yield a JSON file that is storing all the information for the five meteroite landing sites in a dictionary with the key 'sites'.


## Script02: calculate_trip.py

This is the second script in the repository and will be run second as this script will call the JSON file created by the first script. This script will read the JSON file 
created and will calculate the time required for a robot to take samples from each of the meterite landing sites. There are some assumptions that are good to know before 
running this code, they are as follows:

        1. robot starts at lat/lon {16.0, 82.0}
        2. robot's max speed is 10 km/hr
        3. the landing sites are on the planet Mars, hence we are taking into account the radius of Mars which
                in this case is 3389.5 km
        4. the script uses the great-circle distance algorithm to calculate the distance between two points.
                The function was provided by the COE332 professors and was used in this script.
        5. the time that the robot stops at each landing site is determined by the composition of the
                meteorite; stony = 1 hr, iron = 2 hrs, and stony-iron = 3 hrs.

After the robot has finished visiting all five of the meteorite sites, the script will print information about each leg of the trip, including travel time between each 
leg and the time it took to sample the meteorite. The script will also print a summary of the entire trip.
