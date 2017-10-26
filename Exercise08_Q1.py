import re

#Open files for input and output
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable(might need 3: one for texas, one for florida and one for SNPs)
TX_reg=r"[Cc].{1,3}\.[a|A][0-9]?\.([0-9]{3})"
FL_reg=r"[Cc].{1,3}\.[g|G].{1,2}\.([0-9]{3})"
SNP_reg=r"[0|1]\/[0|1]\:([0-9]{1,3}\,[0-9]{1,3})\:[0-9]{1,3}\:[0-9]{1,3}\:[0-9]{1,3}\,[0-9]{1,3}\,[0-9]{1,3}"
Fin_reg=r"\.\/\.\:\.\:\.\:\.\:\."

#loop(following similar format to pseudo code)
for Line in vcffile:
    Line = Line.strip() #strip end of line
    if '##' in Line: 
        outfile.write(Line + "\n") 
        # write header(unchanged) line to file
    elif '#' in Line: 
        #replace sample names with TX and FL regexes
        Line_2=re.sub(TX_reg, "Cf.Sfa.\g<1>", Line)
        Line_3=re.sub(FL_reg, "Cf.Gai.\g<1>", Line_2)
        #write new line version to file
        outfile.write(Line_3 + "\n") 
    else: #now you're in the data
        Line_2=re.sub(SNP_reg, "\g<1>", Line)
        #replaces full SNP info with allele counts
        #replace missing data with NA
        Line_3=re.sub(Fin_reg, "NA", Line_2)
        #write new line version to file
        outfile.write(Line_3 + "\n")
#Close files
outfile.close() 
vcf.close()
