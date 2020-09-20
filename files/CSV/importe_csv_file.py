from csv import*
#from Notes_Eleves.csv import*
with open('Notes_Eleves.csv', newline='') as csvfile:
     spamreader = reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))
#cr = csv.reader("Notes_Eleves.csv",dialect='excel')
#for row in cr: print(row)
#print(cr)
#f=open("ffff.txt", "a")
#s=f.write(soolutions)
#f.close()
