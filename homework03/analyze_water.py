# Daniela Sanchez, dls4848

import requests
import json


def calculate_turbidity(data:float) -> float:
    """
    This function will calculate current turbidity by taking the average of the most recent entires in the json data set.

    Args:
        data(float): this is data that will be imported into this script from the turbidity_data json data set

    Returns: 
        current_turbidity(float): this is the current turbidity that will be used later on in the script.
    """
    current_turbidity = 0
    for i in range(5):
        current_turbidity += data[i]['sample_volume'] * data[i]['calibration_constant']

    current_turbidity /= 5
    return current_turbidity


def calculate_minimum_time(current_turbidity:float, safe_thresh:float, decay_factor:float) -> float:
    """
    This function will take the current turbidity and determine whether or not it is within the safe threshold or not.
    If not, it will calculate the minimum time required for the turbidity to fall below the safe threshold.
    
    Args: 
        current_turbidity(float) : this value is taken from the previous function 'current_turbidity'
        safe_thresh(float) : this is a given constant which is 1.0
        decay_factor(float) : this is a given constant which is 2% or 0.02 which is how it is used in this script

    Returns: 
        0(int): this means that the current turbidity is below the safe threshold and will not go through the rest of the
                function to calculate the min time
        hours(float) : this is the minimum amount of time it will take for the water's turbidity to fall below the 
                    safe threshold. This value is typed as a float but will give the result in hours. 
    """
    if current_turbidity <= safe_thresh:
        return 0
    else:
        hours = 0
        while current_turbidity > safe_thresh:
            hours += 1
            current_turbidity *= (1 - decay_factor)
        return hours


def main():
    response = requests.get("https://turbidity_data.json") #import water turbidity data set
    data = json.loads(response.text)['turbidity_data']

    # constants given
    safe_thresh = 1.0
    decay_factor = 0.02

    # calculate current water turbidity using function
    current_turbidity = calculate_turbidity(data)
    below_safe_thresh = current_turbidity <= safe_thresh

    # calculate minimum time to fall below safe thresh
    minimum_time = calculate_minimum_time(current_turbidity, safe_thresh, decay_factor)

    # print results
    print("Current water turbidity:" , current turbidity)
    print("Below safe threshold:" , below_safe_thresh)
    print("Minimum time required to fall below safe threshold:" , minimum_time, "hours")


if __name__ == "__main__":
    main()








