# this is exercise 2 for homework 1
# Daniela L Sanchez dls4848

import names 

for i in range(5):
    name = names.get_first_name()
    name.strip()

    while( len(name) != 9):
        name =  names.get_full_name()
        name.strip()
    print(name)













