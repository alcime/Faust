import re

input_file_relative_pathname = input('Chemin du fichier :')
output_file_relative_pathname = 'promesse_ng.tsv'

input_file = open(input_file_relative_pathname)
output_file = open(output_file_relative_pathname, "w+")

for line in input_file:
    line = re.sub('\"', '',line)
    output_file.write(line)

input_file.close()
output_file.close()
