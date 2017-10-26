#Exercise 8, Python question 1
#10/16/17, YYC
import re as re 

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

reg1=re.compile('((CF)|(CF07)|(cf))\.[Aa]{1}[2]?')
reg2=re.compile('((CF)|(cf))\.((G2)|(gai)|(GAI))')
reg3=re.compile('([0-9]\/[0-9]\:)(([1-9][0-9]{0,1}|0)\,[0-9])(\:([1-9][0-9]{0,2}|0)\:([1-9][0-9]{0,2}|0)\:([1-9][0-9]{0,2}|0)\,([1-9][0-9]{0,2}|0)\,([1-9][0-9]{0,2}|0))')
reg4=re.compile('\.\/\.\:\.\:\.\:\.\:\.')
#loop over file
for line in vcffile:#look at old code to see how you looped over a file
    #strip end of line
    line = line.strip()
    if line.startswith('##'): #how can you tell if this is the header line?
                       outfile.write(line + "\n")
        #write unchanged header line to file
    elif line.startswith('#CHROM'): #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        line1=re.sub(reg1,'Cf.Sfa',line)
        line2=re.sub(reg2,'Cf.Gai',line1)
        #write new version of line to file
        outfile.write(line2 + "\n")
    else: #now you're in the data
        #replace full SNP info with allele counts only
        line3=re.sub(reg3,r'\2',line)
        #replace missing data with NA
        line4=re.sub(reg4,'NA',line3)
        #write new version of line to new file
        outfile.write(line4 + "\n")
#Close files
vcffile.close()
outfile.close()
                   
