f = open("sample.txt","r")
lines = f.readlines()
f.close()

f = open("nonzero.txt","w")
endNum = raw_input("Enter the end number of a line you'd not want to see: ")
for line in lines:
  	if line.rstrip().rsplit(" ",1)[1] != endNum:
	 print(line)
    	 f.write(line)
