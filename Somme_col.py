# Ecrit la somme des valeurs de certaines colonnes dans un fichier indique par l'utilisateur

import pandas as pd

infile = input("Nom du fichier d'entree :")
print ('\n')
if infile == '':
   infile = 'tsv_simple.tsv'
outfile = 'Promesse_somme.tsv'
nb_lignes_a_sauter = 0 #23277

i_col_titre = 0 #1
i_first_col = 0 #4
i_last_col = 2 #49
               
fout = open(outfile, "w+")
fin = pd.read_csv(infile, sep = '\t', header = 0, skiprows = nb_lignes_a_sauter )

               
for i_row in range(1, fin.shape[0] - 1):
    print('i_row = ' + str(i_row) + '\n')
    if fin.iloc[i_row][i_col_titre] == fin.iloc[i_row + 1][i_col_titre] :
        for i_col in range(i_first_col, i_last_col):
            print('i_row = ' + str(i_row) + '\n')
            print ('Ancienne valeur de la col#' + str(i_col+1) + ' : ' + str(fin.iloc[i_col + 1]) )
            fin.iloc[i_col + 1] += fin.iloc[i_col]
            print ('Nouvelle valeur de la col#' + str(i_col+1) + ' : ' + str(fin.iloc[i_col + 1]) )
    else:
        print('pas de modif pour cette ligne')
        line = pd.DataFrame.to_csv(fin.iloc[:i_row], sep = '\t')
        fout.write(line)
    
fout.close()
