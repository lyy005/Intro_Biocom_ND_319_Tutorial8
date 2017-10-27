#Exercise 8, Question 1
#10/13/17
import re

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#regex variables
TXsamples = "([Cc][Ff](\d{2})?\.[Aa]\d?)"
FLsamples = "([Cc][Ff]\.[Gg](2|AI|ai))"
allelect = r"\d/\d:(\d,\d):\d:\d+:\d+,\d+,\d+"
missing = "\./\.:\.:\.:\.:\."

for Line in vcffile:
    Line=Line.strip()
    if '##' in Line:
        #print('found first line')
        outfile.write(Line + "\n") #write unchanged header line to file
    elif '#' in Line: #how can you tell if this is the line with the column headings?
        #print('found second line')
        TXreplaced = re.sub(TXsamples,"Cf.Sfa",Line)
        FLreplaced = re.sub(FLsamples,"Cf.Gai",TXreplaced) #standardize (replace) sample names with TX and FL regexes
        outfile.write(FLreplaced + "\n") #write new version of line to file
    else: #now you're in the data
        selAllele = re.sub(allelect, r"\1", Line) #replace full SNP info with allele counts only
        #print(selAllele)
        missingData = re.sub(missing, "N/A", selAllele) #replace missing data with NA
        #print(missingData)
        outfile.write(missingData +"\n") #write new version of line to new file
        
vcffile.close()
outfile.close()