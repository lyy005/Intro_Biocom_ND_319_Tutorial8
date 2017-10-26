import re

#Open files for input and output
vcf = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable(might need 3: one for texas, one for florida and one for SNPs)
TX_reg=re.compile(input regex) #tx and fl should be the same (format re.compile(r''))
FL_reg=re.compile(input regex)
SNP_reg=re.compile(r'^.+?/.+?:(.+?,.+?):.+?,.+?,.+?$') #not 100% sure it's correct
#re.sub(r"[Cc][Ff][0-9]+\.[Aa][0-9]{1}\.[0-9]{3}","Cf.Sfa.[0-9]{3}",test)>test1 #in case this is helpful for searches
#loop(following similar format to pseudo code)
for line in vcf:
  line=line.strip()
  #split lines int columns separated by whitespace
  col=line.split()
  if 
  elif
  else
  outfile.write( + "\n")
