#########exercise 8#############################


#####Question 1
import sys
import re
vcf = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")
search_tex = r'(CF.A.|CF.A2.|CF07.A.|cf.a.)([0-9]{3})'
replace_tex = r'Cf.Sfa.\2'
search_fl = r'(CF.G2.|CF.GAI.|cf.gai.)([0-9]{3})'
replace_fl = r'Cf.Gai.\2'

search_allel = r'[01.]/[01.]:([0-9.]+,?[0-9.]*):[0-9:.,]*'
replace_allel = r'\1'


search_match = r'\.'
replace_match = r'NA'



for line in vcf:
    line = line.strip()
    if "##" in line:
        outfile.write (line + "\n")
    elif "#" in line:
        line = re.sub(search_tex, replace_tex, line)
        line = re.sub(search_fl, replace_fl, line)
        outfile.write(line + "\n")
    else:
        line = re.sub(search_allel, replace_allel, line)
        line = re.sub(search_match, replace_match, line)
        outfile.write(line + "\n")

outfile.close()
vcf.close()











#####Question 2
