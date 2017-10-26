#Question 1 for tutorial exercise 08

#Open files to read and write
vcffile=open("Cflorida.vcf","r")
outfile=open("CfloridaCounts.txt","w")

import re
texasfind=re.search("[cC][fF](0-7)?\.[Aa](2)?\.d{3}",vcffile)

#Loop through open file
for Line in vcffile:
    #Remove end of line character
    Line = Line.strip()
    #Operate only on lines that do not include >, skips header lines
    if ">" not in Line:
        #Find the ORF in each sequence line
        texasfind=re.search(r"[cC][fF](0-7)?\.[Aa](2)?\.d{3}",Line)
        #Print the ORF to standard out, note that group(0) is the full match
        print(texasfind.group(0))
    elif : #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        re.sub()
        #write new version of line to file
        outfile.write(string + "\n")
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file

vcffile.close()

# need to add the loop after checking that the regex code above works for the file
#other possible REGEX pattern 
import re
texas=re.search(r"[cC][fF]([0-9]{2})?\.[Aa]([0-9])?\.[X]{3}",vcffile)


