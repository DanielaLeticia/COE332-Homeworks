
# Homework06: Say It Ain't Genes

This homework is mostly a continuation and additional practice for the topics associated with the previous homeworks.
This program uses a Flask application to get, delete, and post data. The data set used in this program is taken from the Human
Genome Organization (HUGO) which is a non-profit that oversees the HUGO Gene Nomenclature Committee (HGNC). The HGNC is 
repsonsible for uniquly naming every human gene. This data set contains indentifying information for every gene that has been 
named by HGNC.

---

## Routes:

This application has mulyiple routes that will help the user get the information from the data set easier. All of the available
routes and a brief description of them in is the table below. Some of the routes are a bit more basic, simply getting data from the 
data set based on parameters. The POST, DELETE, and GET routes are special in this program, as they all can run within a single 
route in the program. Taking a deeper look into the code iteself, we can see that it utilizes if and elese if statements to 
check what route was specified by the user. This makes the program faster and more concise. 

| Route | Method | Description |
| ----- | ----- | ----- |
| `/data` | POST | put all data into redis |
| `/data` | GET | returning all data from redis |
| `/data` | DELETE | delete all data from redis |
| `/genes` | GET | return a json formatted list of all hgnc_id |
| `/genes/<hgnc_id>` | GET | return all data associated with a specified hgnc_id |

## Docker:

This prgram utilizes Docker in additon to a docker compose file to containerize the program. The docker file is relativly simple as
the program is only running one file. This dockerfile is used in conjuction to the docker-compose file whose purpose is to
'automate' the containerization process.

## Using Redis:

This program uses redis to run. Redis is used to create a much simpler coding environment. It is mainly used with programs with 
complex data which is why it is appropirate to use it with this project and data set as it is longer and more complex than the
previous data sets we have worked with. 

## Running the Program:

First and formost, it is important that the user has all of the required files in one folder or repository in the command line of 
their choosing. Since we implimented Docker into this program, running it is fairly simple. To run the docker-compose file and the 
container, type and execute the following command: `docker-compose up -d`. This will create a redis-flask app. You can then use
the command `docker ps -a` to get a list of all of the containers running. Here you should find the container that we just 
launched. Running the commands is similar to what we have done so far with curl. The command is as follows: `curl localhost:5000`
This is the basic command. You can add a route that was mentioned above to interact with the data. An example of this is:
`curl localhost:5000/genes`. This command will return a list of all the genes in the data set. You can repeat this command with the 
routes in the table.  

