# This is excerise 1 for homwork 1
# Daniela L Sanchez dls4848

words = []

with open('words', 'r') as f:
    words = f.read().splitlines()


words.sort(key=len, reverse=True)

for x in range(5):
    print(words[x])




