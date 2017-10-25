#########exercise 8#############################


#####Question 1

import re
vcf = open("Cflorida.vcf","r")

search_tex =r'(CF.A.|CF.A2.|CF07.A.|cf.a.)([0-9]{3})'
replace_tex =r'Cf.Sfa.\2'

for line in vcf:
    line = line.strip()
    if "#" in line:
        texas = re.sub(search_tex, replace_tex, line)
        print texas

vcf.close()











#####Question 2
