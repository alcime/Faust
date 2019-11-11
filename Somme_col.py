# Ecrit la somme des valeurs de certaines colonnes dans un fichier indique par l'utilisateur

import pandas as pd

# Demande le nom du fichier
input_file_name = input("Nom du fichier d'entree :")
print ('\n')
if input_file_name == '':
   input_file_name = 'tsv_simple.tsv'

# Parametres
ouput_file_name = 'Promesse_somme.tsv'
nb_lignes_a_sauter = 0 #23277
i_col_titre = 0 #1
i_first_col = 1 #4
i_last_col = 2 #49
output_to_console = True
output_to_file = True

# Read input file contents to df
df = pd.read_csv(input_file_name, sep = '\t', header = 0, skiprows = nb_lignes_a_sauter )
row_count = df.shape[0]
col_count = df.shape[1]



# Define function to print df
def print_df(df):
   print('Data found in ' + input_file_name)
   for i_row in range(0, row_count):
      for i_col in range(0, col_count) :
         cell_contents = str(df.iloc[i_row][i_col])
         if (i_col >= i_first_col) & (i_col <= i_last_col) :
            print(' *' + cell_contents, end = '')
         else :
            print('  ' + cell_contents, end = '')
      print('')
   print('\n')

# Print df
print_df(df)

# Sommation des colonnes
output_file = open(ouput_file_name, "w")
for i_row in range(0, row_count - 1):
   print('i_row = ' + str(i_row) + '\n')

   if i_row == row_count - 1 :
      if output_to_console :
         print('pas de modif pour cette ligne \n')
      if output_to_file :
         line = pd.DataFrame.to_csv(df.iloc[i_row:], sep = '\t')
         output_file.write(line)

   elif df.iloc[i_row, i_col_titre] == df.iloc[i_row + 1, i_col_titre] :
      for i_col in range(i_first_col, i_last_col) :
         if output_to_console :
            print ('Ancienne valeur de la col#' + str(i_col+1) + ' : \n' + str(df.iloc[i_row+1][i_col + 1]) )
         df.iloc[i_row + 1, i_col] += df.iloc[i_row, i_col]
         if output_to_console :
            print ('Nouvelle valeur de la col#' + str(i_col+1) + ' : \n' + str(df.iloc[i_row + 1][i_col + 1]) )
   
   else :
      if output_to_console :
         print('pas de modif pour cette ligne \n')
      if output_to_file :
         line = pd.DataFrame.to_csv(df.iloc[i_row:], sep = '\t')
         output_file.write(line)

# print result
print_df(df)

output_file.close()
