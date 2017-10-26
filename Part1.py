vcffile=open("Cflorida.vcf","r")
outfile=open("CfloridaCounts.txt","w")
import re
test1=[]
test="GF.GAI.027"
re.sub(r"[Cc][Ff][0-9]+\.[Aa][0-9]{1}\.[0-9]{3}","Cf.Sfa.[0-9]{3}",test)>test1
print(test1)
