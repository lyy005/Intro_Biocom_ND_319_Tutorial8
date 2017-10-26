import re

inputFile = open("Cflorida.vcf","r")
outputFile = open("CfloridaCounts.txt","w")

regexTX = re.compile(r"(CF|cf)\w*.[Aa]\w*.")
regexFL = re.compile(r"(CF|cf).[Gg]\w*.")
delete1 = re.compile("0/0:")
delete2 = re.compile(":\d[\d:,]*")
delete3 = re.compile("./.:.:.:.:.")

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
        ln = re.sub(delete1, "", ln)
        ln = re.sub(delete2, "", ln)
        ln = re.sub(delete3, "NA", ln)
        outputFile.write(ln + "\n")
        
inputFile.close()
outputFile.close()
        
