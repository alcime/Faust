import re

infile = input('Chemin du fichier :')
outfile = 'promesse_ng.tsv'

fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    line = re.sub('\"', '',line)
    fout.write(line)
fin.close()
fout.close()
