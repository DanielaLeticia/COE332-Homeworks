

# **Homework03: Water Turbidity Analysis**

---

The subject of this homework is a continuation of homework02. In homework02 we were tasked with programming a scenerio where
a robot is collecting rock samples on mars. Now, our robot has finished collecting rocks and it's time to take them back to the
lab for analysis! For this analysis, we need water. This project focuses on checking the water quality and asses whether
or not it is deemed safe to analyize samples with. 

## Part 1:
The water quality is analyized from a data set. This data set is the base for this project so the user would need to download
this json data set. Please click the following link in order to access the water quality json data set: 
[turbidty_data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) . 
Please note that this data set must be in the same folder as the other scripts in this project to ensure that they all run smoothly.

## Part 2:
This part of the project/homework is done with the script 'analyze_water.py'. This script will read the water quality data 
set and give the user some useful information. The output of the script will give the user the current water turbidity (which 
is the average of the most recent five data points), whether the current turbidity is below the safe threshold, and finally 
the minimum time required for the turbidity to fall below the safe threshold if it is not already. The following bullet 
points are some of the requirements for this part that will be useful when analyzing the code. 
	
	- This script will have at least three functions, one of those being the main() function. The other two will 
	caluclate the current turbidity of the water and calculate the minimum time required for the turbidity to fall 
	below the safe threshold.
	- This script will use the 'requests' library that will insure the transportation of the json data to this script.
	- The script contains a few constants that are used throughout the program. The decay factor is 2% (or 0.02). 
	The turbidity threshold for safe water id 1.0 NTU.
		

## Part 3:
Part 3 of this project is fulfiled by the test_analyze_water.py script. This script's main purpose of is use unit testing 
in order to test the main script in part 2. The script has two function: one will test the calculate_turbidity function 
and the second will test the function finding the minimum time for the turbidity to fall below the safe threshold. The 
values used in the test are given in the project prompt and are therefore used in this unit test script. The program uses 
'pytest'. This will ensure that all functions starting with 'test_' will be run. 






