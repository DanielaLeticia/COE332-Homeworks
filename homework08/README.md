# Homework08: Holidapp

This homework is an extension of the previous homework06 and homework07. While we are still utilizing the same API, Dockerfile, and 
docker-compose, and YAML files, the purpose of this homework is to build out what we already have. In the follwing README, you will
find a description of each of the .yml files that have been modified. To find more descriptions of the YAML files, please see 
the homework07 README: [homework07](https://github.com/DanielaLeticia/COE332-Homeworks/tree/main/homework07)
Please note that in depth descriptions of the gene_api.py, Dockerfile, and docker-compose.yml will not be included in this 
README but if you want to learn a bit more about them, you can find the descriptions in the README for homework06 or 
follow the link: [homework06](https://github.com/DanielaLeticia/COE332-Homeworks/tree/main/homework06)
This project will also include a description of the changes made to the gene_api.py file as I have added a feature that will 
allow the user to use `matplotlib` to plot the gene data.

---

## Preface:
This homework is an extension of homework06 and homework07 meaning that our program should sucessfully be deployed to Kubernetes
and be able to run before this should take place.This homework picks up from the previous. 
Instructions on how to do this are in the README in homework06 and homework07. Please follow the link above to view more 
detailed instructions on how to create the gene_api image and push it to DockerHub and deploy it to Kubernetes.

## YAML Files
There are a total of five .yml files that are needed to deploy to Kubernetes. Since we are using both redis and Flask for this
program, we will have both a service and deployment file for each and well as an additional redis pvc file. Below are brief
descriptions of each of the .yml files

### Redis:
	`danisan-test-redis-pvc.yml` : This is a Persistant Volume Claim (PVC) file that stores our program/image
		independantly from any pods or containers. This insures that there is always be persistent storage for
		the user to claim/access.
	`danisan-test-redis-deployment.yml` : This is a deployment file that will 
	`danisan-test-redis-service.yml` : This is a service file that will make sure that the IP address that 'talks' to
		redis stays the same, even when there may be multiple due to there being multiple redis pods. 

### Flask:
	`danisan-test-flask-deployment.yml` : This is a deployment file that will
	`danisan-test-flask-service.yml` : This is a service file that is quite similar to the redis service file. It will
		create a persistent IP that will be used to talk to the flask API. 

## Deploying to Kubernetes
Please note that it is important that you have your files together in a single folder. This will make the process a lot smoother to
have everything in one place. It should also be in a terminal where you have access to a kubernetes cluster and where you are able
to perform the `kubectl` commands. Below are the steps needed to take in order to deploy the API.

1. type the following command: `kubectl apply -f <file_name.yml>` . This command will run the containers/deployments/ser-
	vices needed. Enter the .yml file you wish to run in the carrot brackets. Please note you must run these files
	in order since a file needs the previous to run. The order of the files is the same order they are in above in the
	YAML Files section.
 
2. Once you have applied all of the files, you should be able to see if these files are running successfully by using the
	command: `kubectl get <service/deployment/pvc>` (only one should be selected at a time). Running this command, 
	you should be able to see the that it is "RUNNING" and how much time it has been running. In the services section
	there should also be an IP address that will become important later.

3. Running these programs, the gene_api image should already been pulled from DockerHub and it should be ready for
	users to interact with.

4. type the following command: `kube get pods`. This should yield a list of available pods. Right now, you should have two
	available pods named "danisan-test-development" and "danisan-test-label". We will exec into the test-development
	pod and this should allow us to use curl commands on the API. Use the following command to exec into the 
	danisan-test-development pod: `kubectl exec -it <pod_name> --/bin/bash`. It is easier to copy and paste the exact
	pod name because there may be a unique number attached to it.
 
5. YOU'RE IN!!! Now, you are in the kubernetes pod that will allow you to interact with the gene API. You may now use
	the various curl commands that are outlined in the homework06 README to interact with the API. 

## Changes Made for Homework08
While this homework will be deployed just the same as the last homework, as previously stated, there have been a few changes made 
to a few of the scripts in order to add features and make it more efficient. One of the most interesting features that I have added
is the ability to turn some of the gene data into a plot image. I am using the library 'matplotlib' which has to be pip installed
into the command line you are using. Use the following command to make sure it is installed: `pip install matplotlib` . The 
following is a list of the few changes that were made to the scrips and thier purpose. 

1. The `gene_api.py` file had the most changes so we will begin with that one. First, we needed to add a second redis client. This
	is like adding a second tab to an excel spread sheet, where each excel spread sheet is a different environment where you
	can do different things. In this case, the 'first' excel spread sheet (first redis client) will pull and give the user 
	specific information about the gene data. In the second redis client, we are able to use matplotlib in order to plot 
	some of the data. This is a small change in the code that includes adding a new function that gets a redis client. This
	code can be found at the top of the script. The second change made to this script is a new route! This route will utilize
	the second redis client and be able to create the plot, display/save the plot, and delete the plot. The new route can be 
	accessed by using the following command: `curl localhost:5000/image`

2. There was a small but very significant change in the `docker-compose.yml` file. I have simply added an environment variable to 
	the sccript. This environment variable houses the "REDIS_IP". This is a special IP address that I got from using the 
	command `kubectl get services` and taking the IP for the redis service. This is a small change but one that will ensure
	that all of the components are able to 'communicate' with each other and will have access to the proper redis clients 
	needed for this homework.

3. The final script that had minor changes was the `danisan-test-flask-deployment.yml` file. This YAML file, as the name of it
	suggests, will ensure that the flask app is deployed will all of the proper intructions. The change for this file
	is that I added an environment variable as well. Like the previous bullet point stated, it is important that all of the 
	files are able to 'talk' to each other. Creating a program and deploying it to Kubernetes involves a lot of moving peices
	and is often diffucult to keep track of. Some of these files do that for you. The environment variable for this script
	is defined by the same REDIS_IP that was used in the previous changed script. 

 
