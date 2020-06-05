# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 03:22:17 2020

@author: Matthew Davids
"""
import importlib

mName = input('DNA input:')
importlib.import_module(mName)

inputfile = "DNA.txt"
with open(inputfile,mode='r') as f: # using this way allows me not to worry about closing the file and also reseting its cursor eveytime we read line 
    cont = f.read()                 # the as f, the f is useed as a variable that holds the text file
                                    # And lastly the mode is set to r meaning readonly this makes that the file not be overwritten here unless mode w, a r+ or w+ is used
    cont = cont.replace('\n','')    # the replaced method is replacing the space or next line so all the items in the file will be align next to each other.
    cont = cont.replace('\r','')

def translate(cont):                                # Defining a function translate(cont)
    amino_table = {'ATT':'I','ATC':'I','ATA':'I', # the keys inside this dictionary are the DNA codons and they holding the value SLC code for Amino acid
                   'CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L',
                   'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
                   'TTT':'F','TTC':'F',
                   'ATG':'M'}
    protein =''
    if len(cont) % 3 == 0:                  # This line here says that if the length of count which was assign to DNA.txt a text file if the 
        for n in range(0,len(cont),3):      # 3 can evenly go into the length of count then it will return zero because there is no remainder so it will be  divisible by 3 if not then it is not divisible by three
            codon = cont[n:n + 3]
            protein = protein + animo_table[codon]
    return protein        

def mutate(inputfile):
    with open(inputfile,mode='r') as f:   #
        cont = f.read()
        
    first_occur = cont[0]
    if first_occur in 'a':
        cont
        
 
prt = mutate('NormalDNA.txt')
dna = mutate('MutatedDNA.txt')

if 'a' in prt:
    f.read()

p == translate(dna[20:935])
dna == prt
