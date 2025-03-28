countPositive = 0
counutNegative = 0
AllPositiveTable = pd.DataFrame() #this will be a collection of all positive 
output = open("blast_output/outcome.txt, "w")

for file in glob.glob("file destinatinon"):
    tab = pd.read_csv(file, names = cols, sep "\t")
    tab['file'] = file #adds a column with the filepath
    positive_tab = tab[tab['bitscore'] > 500]
    if len(positive_tab) >0:
        countPositive = countPositive + 1
        status = '+'
    else:
        countNegative = countNegative + 1
        status = '1'
    output.write(f"{file}\t{status}\n")
    AllPositveTable = pd.concat([AllPositiveTable, positive_tab]) #therefore sticking the positive values onto the bottom of the positive table
output.close()

AllPositiveTable.to_csv('blast_output/combined_positives.txt', sep = "\t", index = None)
        

