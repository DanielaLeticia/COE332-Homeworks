# this is the iss tacker script for homework05
# Daniela Sanchez, dls4848

import requests
import math
import xmltodict

from flask import Flask

app = Flask(__name__)

# this is where my issue is: how to access/download data here!!!!!
def get_data() -> dict:
    '''
    This function will return the entire data set

    Args:
        This fuction does not take any arguments.

    Returns:
        data : This is the variable for the entire data set that will be returned when this function is executed.
    '''
    data_url = "https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml"
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
    This function will print a list of all of the epochs in the data set when the user types '/epochs' and will return a modified
    version of the list if the user uses query parameters.

    Args:
        This function does not take any arguments.

    Returns:
        list_of_epochs (list): This is the list of all of the epochs in the data set
    '''
    maximum = len(data) #getting the length of the data
    list_of_epochs = []
    lim = request.args.get('limit', maximum)
    if lim:
        try:
            lim = int(lim)
        except ValueError:
            return "Invalid limit paramter", 400

    offset = request.args.get('offset', 0)
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            return "invalid offset parameter", 400

    count = lim
    for i in range(maximum):
        if len(list_of_epochs) == lim:
            break
        if i >= offset:
            list_of_epochs.append(data[i]['EPOCH'])
    return list_of_epochs


#@app.route('/epochs?limit=int&offset=int', methods=['GET'])
#def get_limit_epoch():



#    return 



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
    return ( 'speed: {str(speed)} {units}')


@app.route('/help', methods=['GET'])
def help_message():
    '''
    This function will return a help menu with all available user options and small descriptions.

    Args:
        This function does not take any arguments.

    Returns:
        This function will return a help menu in string form.
    '''
    help_string = " Help Menu: Below are all of the possible commands and thier descriptions:"
    string1 = ("'/' : returns entire data set;\n")
    string2 = ("'/epochs' : returns list of ALL epochs in data set;\n")
    string3 = ("'/epochs?limit=int&offset=int' : returns list of epochs with user specified parameters;\n")
    string4 = ("'/epochs/<epoch>' : returns user specified epoch;\n")
    string5 = ("'/epcohs/<epochs>/speed' : returns speed of user specified epoch;\n")
    string7 = ("'/help' : returns help menu;\n")
    string8 = ("'/delete-data' : will delete entire data set;\n") 
    string9 = ("'/post-data : will reload the dictionary object with data from the web;\n")

    return help_string + string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8 + string9

@app.route('/delete-data', methods=['DELETE'])
def delete_all_data(data):
    try: 
        if data.first() is not None:
            data.delete()
            delete_message = 'ALL data has been succesfully deleted'
        else:
            print ('Invalid Input: data could not be deleted.')
            delete_message = 'Data could NOT be deleted!'
    except HTTPException as error:
        return error
    return delete_message

@app.route('/post-data', methods=['POST'])
def post_data():
    '''
    This function will reload the dictionary with data from the web

    Args:
        This function takes not arguments.

    Returns:
        data (dict): this is the entire updated data set
    '''
    global data
    data = information['ndm']['oem']['body']['segment']['data']['stateVector']
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


