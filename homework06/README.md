
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
chack what route was specified by the user. This makes the program faster and more concise. 

** insert table with routes here **

## Docker:

This prgram utilizes Docker in additon to a docker compose file to containerize the program. The docker file is relativly simple as
the program is only running one file. 

## Using Redis:

## Running the Program:

