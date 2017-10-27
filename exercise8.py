import os
import pandas
import numpy

vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")


for line in vcffile:
    
    line = line.rstrip() 

    var=re.match('[CFcf]\.[Aa]*?\.', line)
    var.replace('var','Cf.Sfa') 
    outfile.write(var)
    var2=re.match('[CFcf]\.[Gg][Aa]?[Ii]?\.', line)
    var2.replace('var2','Cf.Sfa') 
    outfile.write(var2)
    
    var3=re.match([0-9],[0-9],line)
    outfile.write(var3)
   



