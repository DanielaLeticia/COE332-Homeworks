# Homework07: In The Kubernetes

This homework is an extension of the previous homework06. While we are still utilizing the same API, Dockerfile, and 
docker-compose, we have added a few more YAML files that will deploy this program to Kubernetes. In the follwing README, you will
find a description of each of the .yml files as well as how to deploy the files to kubernetes and subsequently run the gene API.
Please note that in depth descriptions of the gene_api.py, Dockerfile, and docker-compose.yml will not be included in this 
README but if you want to learn a bit more about them, you can find the descriptions in the README for homework06 or 
follow the link: [homework06](https://github.com/DanielaLeticia/COE332-Homeworks/tree/main/homework06)

---

## Preface:
This homework is an extension of homework06 meaning that our gene_api should already be built and pushed onto DockerHub.
This homework picks up from there. 
Instructions on how to do this are in the README in homework06. Please follow the link above to view more detailed instructions on
how to create the gene_api image and push it to DockerHub.

## YAML Files
There are a total of five .yml files that are needed to deploy to Kubernetes. Since we are using both redis and Flask for this
program, we will have both a service and deployment file for each and well as an additional redis pvc file. Below are brief
descriptions of each of the .yml files

	Redis:
		`danisan-test-redis-pvc.yml` : This is a Persistant Volume Claim (PVC) file that stores our program/image
			independantly from any pods or containers. This insures that there is always be persistent storage for
			the user to claim/access.
		`danisan-test-redis-deployment.yml` : This is a deployment file that will 
		`danisan-test-redis-service.yml` : This is a service file that will make sure that the IP address that 'talks' to
			redis stays the same, even when there may be multiple due to there being multiple redis pods. 

	Flask:
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



 
