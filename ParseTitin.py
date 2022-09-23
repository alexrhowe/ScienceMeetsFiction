from manim import *
import numpy as np
import csv

peptides = {'A':'alanyl', 'C':'cysteinyl', 'D':'aspartyl', 'E':'glutamyl', 'F':'phenylalanyl', 
            'G':'glycyl', 'H':'histidyl', 'I':'isoleucyl', 'K':'lysyl', 'L':'leucyl', 
            'M':'methionyl', 'N':'asparaginyl', 'P':'prolyl', 'Q':'glutaminyl', 'R':'arginyl', 
            'S':'seryl', 'T':'threonyl', 'V':'valyl', 'W':'tryptophyl', 'Y':'tyrosyl'}

acyls = {'Ala':'alanyl', 'Cys':'cysteinyl', 'Asp':'aspartyl', 'Glu':'glutamyl', 'Phe':'phenylalanyl', 
         'Gly':'glycyl', 'His':'histidyl', 'Ile':'isoleucyl', 'Lys':'lysyl', 'Leu':'leucyl', 
         'Met':'methionyl', 'Asn':'asparaginyl', 'Pro':'prolyl', 'Gln':'glutaminyl', 'Arg':'arginyl', 
         'Ser':'seryl', 'Thr':'threonyl', 'Val':'valyl', 'Trp':'tryptophyl', 'Tyr':'tyrosyl'}
         
acylnames = ['alanyl', 'cysteinyl', 'aspartyl', 'glutamyl', 'phenylalanyl', 
         'glycyl', 'histidyl', 'isoleucyl', 'lysyl', 'leucyl', 
         'methionyl', 'asparaginyl', 'prolyl', 'glutaminyl', 'arginyl', 
         'seryl', 'threonyl', 'valyl', 'tryptophyl', 'tyrosyl']
        
fin = open('titin12.txt','r')
        
bigname = ''
bigseq = ''
        
for i in range(0,600):
    sequence = fin.readline()[0:60]
    if i==599: sequence = sequence[0:len(sequence)-1]
    for l in sequence:
        bigname = bigname + peptides[l]
        bigseq = bigseq + l
        
bigname = bigname + 'isoleucine'
bigseq = bigseq + 'I'

print('Titin, isoform 12')
print(len(bigseq),' Amino Acids')
print(len(bigname),' Letters')

fout = open('titin-name.txt','w')
rows = int(np.floor(len(bigname)/72.))
for i in range(0,rows):
    fout.write('{0:s}\n'.format(bigname[i*72:(i+1)*72]))
fout.write(bigname[rows*72:])