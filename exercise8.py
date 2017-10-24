#########exercise 8#############################


#####Question 1

import re
vcf = open("Cflorida.vcf","r")

SearchStr =r'>[cf]'
ReplaceStr =r'fuuuck'

for line in vcf:
    line = line.strip()
    if "#" in line:
        newLine = re.sub(SearchStr, ReplaceStr, line)
        print newLine
    else: print line

vcf.close()











#####Question 2
