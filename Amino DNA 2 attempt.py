def translate(cont): # The function translate being defined
     amino_table = {'ATT':'I','ATC':'I','ATA':'I', # the keys inside this dictionary are the DNA codons and they holding the value SLC code for Amino acid
                   'CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L',
                   'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
                   'TTT':'F','TTC':'F',
                   'ATG':'M'}
     
mName = input('Enter DNA:')
with open('C:\\Users\\Matthew Davids\\Documents\\Sprint\\DNA.txt',mode='r') as f:
    cont = f.read()
    cont = cont.replace('\n','')
    cont = cont.replace('\r','')
    print(mName)
    
    if len(cont) % 3 == 0:
        print(animo_table['ATT']+animo_table['CTT']+animo_table['GTT']+animo_table['TTT']+animo_table['ATG'])
    else:
        print('X')
        
def mutate(dna):
    with open('DNA.txt',mode='r') as r:
        dna = r.read()
        dna = dna.replace('\n', '')
        
        letter = dna[0]
        if letter == 'a':
            print('True)
        else:
            print('False')

with open('NormalDNA.txt',mode='r') as n:
    rep = n.read()
    rep = rep.replace('A','a')

Mfile = open('MutatedDNA.txt')
d = Mfile.read()
d = d.replace('a', 'T')  

          
            