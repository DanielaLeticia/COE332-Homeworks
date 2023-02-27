# __Homework05: Undone (The Sweater Container)__

This is a continuation of homework04. This is a new and improved version of the iss tracker that was built in homework04. There
have been a couple of new routes added which will be discussed in detail in this README and it also impliments docker which is used
to containerize this project and ship it anywhere and on any device. 

---

## Part01: Imporved Script

This script is a newer and updated version of the iss_tracker script that was built in homework04. The main difference between these
two scripts is some of the new routes added which make this application more advanced and overall more useful to the user.
The following are the new routes implimented and thier purpose:
	
	1. '/epochs?limit=int&offset=int' : This command will return a modified list of epochs with the specified parameters
	2. '/help' : This will return to the user a list of all of the routes available and a brief description of thier purpose.
	3. '/delete-data' : This will delete ALL of the data in the data set.
	4. '/post-data' : This will reload and update the data set with data from the web.

## Part02: Dockerfile

The Dockerfile is the main focus of this homework. The point of a Dockerfile is to able to containerize and ship your program. 
In other words, it puts all of the nessessary commands and scripts together so that the entire program can be shared and used by 
others. This is particulary useful because not everyone is running the same versions of software and such. Containerizing a 
program allows other to easily access your program. While there are many ways to containerize a project, we choose Docker to do this.
The file called 'Dockerfile' in this folder is what containerized this project and will be the file that is run by the user in 
order to run the iss tracker program/script. 

## Part03: Running the Data & Dockerfile


