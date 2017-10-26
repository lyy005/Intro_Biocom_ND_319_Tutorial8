import re

IDFile = open("indivIDs.txt","r")
IDs = {}

for ln in IDFile:
    ln = ln.strip()
    fields = ln.split()
    if fields[0] in IDs:
        print("Duplicate: " + fields[0])
        continue
    else:
        IDs[fields[0]] = fields[1]
        
IDFile.close()

sequenceFile = open("seqFastq.fq","r")
outputFile = open("IDseq.fasta","w")

cutSites = []

regex = re.compile(r"([ATCG]{8})AATTC") #gets the group of 8 bases just before the restriction site in a  group
sequenceReg = re.compile(r"[A-Z]{10}")  #matches uppercase strings. I saw some had an N to begin with. I chose 10 because it is unlikely that the quality line has 10 uppercase in a row

for ln in sequenceFile:
    if re.match(sequenceReg, ln):
        match = re.search(regex, ln)
        if not match:
            #print("No match on the restriction site in sequence: " + ln)
            continue
        if match.group(1) in IDs:
            cutSites.append(match.start(1) + 8)
            ln = ln[:match.start(1)] + ln[match.end(1):] #cuts out the part matched by regex from string
            
            outputFile.write('>' + IDs[match.group(1)] + "\n")
            outputFile.write(ln)
        #else:
            #print("no match found on : " + match.group(1))
            #outputFile.write("> No match on: " + match.group(1) + '\n')
            #outputFile.write(ln)
            
import pandas
from plotnine import *
data=pandas.DataFrame({"Cut Site": cutSites})

cutHG=ggplot(data,aes(x="Cut Site"))
cutHG+geom_histogram()+theme_classic()
