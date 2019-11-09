import pandas as pd

infile = input("Nom du fichier :")
outfile = 'Promesse_somme.tsv'

fout = open(outfile, "w+")
fin = pd.read_csv(infile, sep = '\t', header = 'infer', skiprows = 23277 )

for row in fin:
    if fin['Titre'][row] == fin ['Titre'][row + 1] :
        for i in range(4,49):
            fin[i+1] += fin[i]
        else:
                fout.write (fin[row]) 
    
fin.close()
fout.close()
