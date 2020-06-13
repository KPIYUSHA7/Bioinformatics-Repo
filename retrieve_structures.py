import pubchempy as pcp
import pandas as pd
from collections import deque

list_compounds = pd.read_csv("final.csv", header=None)  #Data file containing names of required compounds

data = list(list_compounds[0])
len(data)

Compounds = {}
for i in data:
        a = pcp.get_compounds(i, 'name') #Retrieve the PUBCHEM ID of the compounds 
        Compounds[i] = a
len(Compounds)

no_result = [] 
for i in (Compounds):
    if (Compounds[i] == []):
        no_result.append(i)   #List of compounds for whom PUBCHEM IDs were not found
    
len(no_result)

for i in deque(Compounds.keys()):  #Deque helps to remove elements from any part of the dictionary; remove the no_result IDs from original dictionary
    for j in no_result:
        if i == j:
            del Compounds[i]

len(Compounds)

for i in Compounds:
    try:
        pcp.download('SDF', f'{i}.sdf', i, 'name', record_type = '3d' ) #Download the .sdf format of the compounds for whom 3D structure is available
    except:
        print(i)


no_result  #Print out the compouds for which there was no result from pubchempy search





