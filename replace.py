# first get all lines from file
with open('samplec.txt', 'r') as f:
    lines = f.readlines()

#add space at end of each line

lines = [line.replace("\n"," \n") for line in lines]


#remove the space
lines = [line.replace(" \n","\n") for line in lines]


# remove spaces
lines = [line.replace(' ', ',') for line in lines]



# finally, write lines in the file
with open('samplec.txt', 'w') as f:
    f.writelines(lines)
