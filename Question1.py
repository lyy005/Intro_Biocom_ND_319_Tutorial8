#Question 1 for tutorial exercise 08



#possible REGEX pattern 
import re
re.sub([cC][fF]([0-9]{2})?\.[Aa]([0-9])?\.XXX,Cf.Sfa.XXX,vcffile)

# need to add the loop after checking that the regex code above works for the file


#pseudo code from the github repo
#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

#loop over file
for :#look at old code to see how you looped over a file
    #strip end of line
    if : #how can you tell if this is the header line?
        #write unchanged header line to file
    elif : #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        #write new version of line to file
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files

