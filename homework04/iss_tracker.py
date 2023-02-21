# Daniela Sanchez, dls4848

import requets
import math
import xmltodict

from flask import Flask

app = Flask(__name__)

def get_data() -> dict:
    '''
    This function will return the entire data set

    Args:
        This fuction does not take any arguments.

    Returns:
        data : This is the variable for the entire data set that will be returned when this function is executed.
    '''
    data_url = "https://..." # enter url link here
    response = requests.get(data_url)
    information = xmltodict.parse(response.text)
    data = information['ndm']['oem']['body']['segment']['data']['stateVector']
    return data

@app.route('/', methods=['GET'])
def get_entire_data_set():
    '''
    This function will print the entire data set when the user simply uses a back slash '/'

    Args:
        This function does not take any arguments.

    Returns:
        data (dict): This is the entire data set
    '''
    data = get_data()
    return data


@app.route('/epochs', methods=['GET'])
def get_all_epochs():
    '''
    This function will print a list of all of the epochs in the data set when the user types '/epochs'

    Args:
        This function does not take any arguments.

    Returns:
        list_of_epochs (list): This is the list of all of the epochs in the data set
    '''
    data = get_data()
    list_of_epochs = []
    list_length = len(data)
    for i in range(list_length):
        list_of_epochs.append(data[i]['EPOCH'])
    return list_of_epochs


@app.route('/epochs/<int:epoch>', methods=['GET']) # the 'epoch' is typed as an int as the arguments only takes strings
def get_specif_epoch(epoch):
    '''
    This function will print a specified epoch value. Specfied by the user

    Args: 
        epoch (int): This is an input value that is entered by the user. Will go after a back slash

    Returns:
        epoch[data]: This is the specific epoch value in the data set.
    '''
    data = get_data()
    if epoch>=len(data):
        return "Error: epoch value not in data set", 400 # error message if input is not in data set and error code
    return epoch[data]


@app.route('/epochs/<int:epoch>/speed', methods=['GET'])
def get_speed_for_specif_epoch(epoch):
    '''
    This function will print the speed for the specific epoch specified. The units for the speed are calculated and printed as
    well. The formula to caluclate was provided by COE332 professors.

    Args:
        epoch(int): This is the specific epoch from the data set that will be used in this function

    Returns:
        speed: This is the speed for the specific enoch.
    '''
    data = get_data()
    if epoch>=len(data):
        return "Error: epoch value not in data set", 400

    # initializing _dot values
    x_dot = data[epoch]['X_DOT']['#text']
    y_dot = data[epoch]['Y_DOT']['#text']
    z_dot = data[epoch]['Z_DOT']['#text']

    # type casting the values into floats
    x_dot = float(x_dot)
    y_dot = float(y_dot)
    z_dot = float(z_dot)

    # using formula provided to calculate speed
    calculate = (x_dot*x_dot)+(y_dot*y_dot)+(z_dot*z_dot)
    speed = math.sqrt(calculate)
    units = data[epoch]['X_DOT']['@units']
    return (f 'speed: {str(speed)} {units}')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')









