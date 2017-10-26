#Question 1 for tutorial exercise 08

#Open files to read and write
vcffile=open("Cflorida.vcf","r")
outfile=open("CfloridaCounts.txt","w")

import re
texasfind="[cC][fF](0-9){,2}\.[Aa](0-9){,1}\."
floridafind="[cC][fF]\.[gG](0-9){,1}[aA]{,1}[iI]{,1}\."

#Loop through open file
for line in vcffile:
    #Remove end of line character
    line = line.strip()
    if "##" in line:
        outfile.write(line + "\n")
    elif "#CHROM" in line: #how can you tell if this is the line with the column headings?
        line=re.sub(texasfind,r"Cf.Sfa.",line)
        line=re.sub(floridafind,r"Cf.Gai.",line) #standardize (replace) sample names with TX and FL regexes
        outfile.write(line + "\n")#write new version of line to file
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
vcffile.close()
outfile.close()

# need to add the loop after checking that the regex code above works for the file
#other possible REGEX pattern 
#import re
#texas=re.search(r"[cC][fF]([0-9]{2})?\.[Aa]([0-9])?\.[X]{3}",vcffile)


