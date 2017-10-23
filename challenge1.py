import re

inputFile = open("Cflorida.vcf","r")
outputFile = open("CfloridaCounts.txt","w")

regexTX = re.compile(r"(CF|cf)\w*.[Aa]\w*.")
regexFL = re.compile(r"(CF|cf).[Gg]\w*.")

for ln in inputFile:
    ln.strip()
    if ln.startswith("##"):
        outputFile.write(ln + "\n")
        continue
    if ln.startswith("#"):
        ln = re.sub(regexFL,"Cf.Gai.",ln)
        ln = re.sub(regexTX,"Cf.Sfa.",ln)
        outputFile.write(ln + "\n")
    else:
        outputFile.write(ln + "\n")
        
inputFile.close()
outputFile.close()
        