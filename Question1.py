#Ex 8

#Open files to read and write

import re
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable names

TXnames=r"[Cc][Ff](07)?\.[Aa](2)?"
FLnames=r"[Cc][Ff]\.[Gg][Aa2](Ii)?"
ACR=r"[01.]/[01.]:([0-9,.]+):[0-9.]+:[0-9.]+:[0-9,.]+"

#loop over file
for Line in vcffile:
    #strip end of line
    Line = Line.strip()
    
    #ID header line
    if "##" in Line: 
    #write unchanged header line to file
        outfile.write(Line + "\n")
    #ID second line
    elif "#" in Line:
        #sub sample names with TX and FL regexes
        newnamesTX = re.sub(TXnames,"Cf.Sfa",Line)
        newnamesALL = re.sub(FLnames,"Cf.Gai",newnamesTX)
        #write new version of line to file
        outfile.write(newnamesALL + "\n")
    
    else:
        #replace full SNP info with allele counts only
        AC=re.sub(ACR,r"\1",Line)
        #replace missing data with NA
        ACNA=re.sub(r"\.","NA",AC)
        #write new version of line to new file
        outfile.write(ACNA + "\n")

#Close files
vcffile.close()
outfile.close()

