#Exercise 8, Python, Question 2
#10/16/17, YYC
import re as re
import pandas as pd
#Open files to read and write
vcffile1 = open("indivIDs.txt","r")
vcffile2 = open("seqFastq.fq","r")
outfile= open("IDseq.txt","w")

#Initialize empty dictionary and lists
dictionary={}
var_good=[] # for histogram
var_bad=[]
#Make dictionary of IDs
for line in vcffile1: #look at old code to see how you looped over a file
    #strip end of line
    line=line.strip()
    #split line on whitespace
    cols=line.split()
    if cols[0] in dictionary: #is the item in the DNA barcode column a key in the dictionary?
        print('error') 
        break #break and print error message if so, this should not happen...
    else: #this means DNA barcode is not yet a key
        #assign sample ID as value and DNA barcode as key
        dictionary[cols[0]]=cols[1]
#Close ID file
vcffile1.close()
# Convert the ID file to data frame
df=pd.DataFrame({'Barcode' : dictionary.keys() , 'ID' : dictionary.values() })

#assign regex to variable name, or compile to variable name
reg1=re.compile('([AGCT]{8})(AATTC)([AGCT]+)')
#A while loop will allow us to skip operating on fastq lines we don't care about
#it also allows us to read huge files line by line, without storing them in memory
#read and strip the first line in the file

# I didn't use while loop and I think for loop is more straightforward

for line in vcffile2: 
    if line.startswith('@'): #is the current line a header line?
        #read and strip the next line, now the sequence line
        line=vcffile2.next().strip()
        if re.search(reg1,line): #is your regex in the sequence
            #store your regex matches
            temp=re.search(reg1,line)  
            # store the full match
            temp1=temp.group(0)   
            # store the barcode
            temp2=temp.group(1)
            # store the AATTC+remaining sequence 
            temp3=temp.group(2)+temp.group(3)
            # store the start position of AATTC
            temp4=temp.start(2)            
            if df['Barcode'].str.contains(temp2).sum() !=0: #is your DNA barcode in the ID data frame?
            ##append the start position of the AATTC to your vector
                var_good.append(temp4)
            #write the fasta header to your file by getting the correct ID from the data frame
                temp5=df[df['Barcode'].str.contains(temp2)==True]['ID'].values[0]              
                outfile.write(temp5+'\n')
            #write the sequence remaining to the right of the AATTC cut site to your file
                outfile.write(temp3+'\n')               
            else:
                #Optional: append location of AATTC to "bad" vector (pattern found but no barcode match) as above
                var_bad.append(temp4)
        #read and strip the next 3 lines, skips over + and quality scores lines, to get to the next header
                line=vcffile2.next()
                line=vcffile2.next()
                line=vcffile2.next()
    #else:
         #it's a good idea to break loop and print error message if you end up here
        #this means you've read the wrong number of lines or the input file isn't in the right format (it is!)
        #print('error')
        #break
        
        
#Close files
outfile.close()
vcffile2.close()
#Graph histograms of good and bad start positions
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,4))
fig.suptitle('Histogram for start position of AATTC')
ax1 = fig.add_subplot(121)
ax1=plt.hist(var_good)
plt.title('Good')
plt.xlabel('Start position')
plt.ylabel('Counts')
ax2 = fig.add_subplot(122)
ax2=plt.hist(var_bad)
plt.title('Bad')
plt.xlabel('Start position')
plt.ylabel('Counts')