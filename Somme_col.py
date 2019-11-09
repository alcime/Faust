import pandas as pd

infile = input("Nom du fichier :")
outfile = 'Promesse_somme.tsv'

fout = open(outfile, "w+")
fin = pd.read_csv(infile, sep = '\t', header = 'infer', skiprows = 23277 )

for row in fin:
    n=1
    if fin.iloc[n][1] == fin.iloc[n+1][1] :
        for i in range(4,49):
            fin.iloc[i+1] += fin.iloc[i]
        else:
              line = pd.DataFrame.to_csv(fin.iloc[:n], sep = '\t')
              fout.write(line)
        n += 1
    
fin.close()
fout.close()
