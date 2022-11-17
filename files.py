#This line opens the files 
#in this case, the file name to be opened is "files.csv"
with open ("files.csv") as file: 
# the for loop loops through the file "files.csv" and reads all the strings present
    for line in file:
        #this line removes the csv delimiter 
        row= line.rstrip().split(", ")
        #this line prints strings in "files.csv" file
        print(f"{row[0]} is file {row[3]}")

