import pandas
import numpy
import re

sequenceID = open("indivIDs.txt", "r") #Open sequence ID file

barcodes={} #Define empty dictionary for barcodes associated with sequence IDs

for line in sequenceID: #Loop through sequence ID file line-by-line
    line=line.strip() #Strip whitespace from beginning and end of line
    cols=line.split() #Return the first value and the second value as unique objects in a list
    if cols[0] in barcodes: #Check if the first value in the line (the barcode) is already in the dictionary
        print "Duplicate:" + cols[1] #Print error message
    else:
        barcodes[cols[0]] = cols[1] #If barcode is not yet present, add it as a key, and associate it with
                                    #the second value in the line (the sequence ID)

file.close(sequenceID) #Close the file
