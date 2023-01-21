#this is exercise 3 for homework 1
#Daniela L Sanchez dls4848

import names

def name_length(name):
    name = name.replace(" ", "")
    return (len(name))

name_list = []

for i in range(5):
    name_list.append(names.get_full_name())

for x in name_list:
    print(x + "has a length of" + " " + str(name_length(x)) + " " + "characters.")



