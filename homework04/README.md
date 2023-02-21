
# __Homework04: Tracking the ISS__

The main objectove of this homework is to import and read an xml data set containing data reguarding the location of the 
International Space Station and then apply our knowledge of Flask and its features to print specific data based on user input. 
The following homework requires some downloding or extra steps by the user in order for this script to work properly. I have tried my
best to write specific and easy-to-follow instructions for executing this project.

---

## __Part01:__

Part one of this project is getting the data and familiarizing yourself with the data given. The data can be found using
the following link: [ISS Trajectory Data](https://spotthestation.nasa.gov/trajectory_data.cfm) . This link will take you to a 
nasa.gov webiste where you will have an option to view the data in two formats; .XML and .TXT. For this project, I will utilize
the .XML format as it is easier for importing and manipulating data as opposed to a text file. Please note that you will need to
copy and paste your own link into the script. This is explained in more depth in the second part of this file. Please download 
this data set into the same folder as this project so the script will run smoothly.

One of the more important things about this data set is that it is updated live. The means that the data may be different
deppending on when you download this data from the nasa website. The state vectors conatined in the data set (which are used to 
calculate the speed and position of the ISS) are in a range of about 15 days. This is why the range may be different deppending on
when the data was downloaded. These state vectors contain Cartesiean vectors for positon (x,y,z), velocity (x_dot, y_dot, z_dot),
and a time stamp (epoch). All of the these variables are used in the script so it is important to know not only what they mean but
how they are used. It will help in the overall understanding of the project.


## __Part02:__

The second part of this homwork/project is the script itself. As states earlier, this program impliments Flask and its 
features in order to print data specific to a user's input. In this case, the user will type `curl localhost: 500` followed 
by a dash '/' and/or some key and the program will proceed to print the specific data that the user requested. For this project, the user can type/select four keys and print different info each time. These also correspond with each function that is used in 
this script. The options for user input are as follows:

		1. '/' : simply typing a back slash will print the entire data set
		2. '/epochs' : this will print all of the epochs in the data set
		3. '/epochs/<epoch>' : the user will input a number after the second back slash and it will print a specific 
				epoch data value
		4. '/epochs/<epoch>/speed' : this will print the calculated speed for the specific epoch value 
		
It is important to know how to be able to print this data. Please follow the steps below in order to succesfully 
run this program.
	
		1. log into a virtual machine or simply use command line/linux
		2. download both the script and data set. It is recommended to have both of files in the same folder. 
		3. open the python script by typing 'vim iss_tracker.py' and type in the url of the data set. This place should 
			be one of these first few lines of code and marked with a comment. 
		4. lastly, run the pogram! To to this, type into the command line the following command:
			'curl localhost: 5000'. From here you can add a back slash to access the entire data set or
			add any of the commands above and now you are able to print specifc data. 


## A note on the Flask app:
If you would like to see what is happening behind the scenes with the Flask app, open a new window in
command line and, in the same directory as the xml file and script, type the following 
commandd: `flask --app iss_tracker.py --debug run` This should open the Flask app and allow to see the operations
of the script after it has been run. If you do not have the Flask app installed in your command line, use the 
following command to instal Flask: `pip3 instal --user flask`.








   
