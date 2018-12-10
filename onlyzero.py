with open("sample.txt", 'r') as f:
    lines=f.readlines()
    endNum = raw_input("Enter the end number of a line you'd like to see: ")
    for line in f:
        if line.rstrip().rsplit(" ",1)[1] == endNum:
            print line
	    lines=line

with open('zero.txt', 'w') as f:
	f.writelines(lines)

f.close()
