#Question 1 for tutorial exercise 08

#Open files to read and write
vcffile=open("Cflorida.vcf","r")
outfile=open("CfloridaCounts.txt","w")

import re
texasfind=re.compile("[cC][fF](0-9)?\.[Aa](0-9)?\.(0-9){3}")

#Loop through open file
for line in vcffile:
    #Remove end of line character
    line = line.strip()
    if "##" in line:
        outfile.write(line + "\n")
    elif "#" in line: #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        #write new version of line to file
vcffile.close()
outfile.close()

# need to add the loop after checking that the regex code above works for the file
#other possible REGEX pattern 
#import re
#texas=re.search(r"[cC][fF]([0-9]{2})?\.[Aa]([0-9])?\.[X]{3}",vcffile)


