#Exercise 8, Python question 1
#10/13/17, MMD
import vcf
import re
#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

lineNumber=0
#loop over file
for line in vcffile:#look at old code to see how you looped over a file
    #strip end of line
    line=line.strip()
    if lineNumber==0: #how can you tell if this is the header line?
        outfile.write(line+"\n")
        #write unchanged header line to file
    elif lineNumber==1: #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        re.sub(((CF|cf){1}.?{4}\.,(Cf.Sfa.),line) ###Having trouble gettig re.sub to work, syntax not working. Trying to replace CF and then any 4 characters leading to a period
        re.sub(((CF|cf){1}.?{4}\.,(Cf.Gai.),line)
        #write new version of line to file
        outfile.write(line+"\n")
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files


