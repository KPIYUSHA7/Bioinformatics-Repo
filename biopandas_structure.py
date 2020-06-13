#!/usr/bin/env python
# coding: utf-8

# In[10]:


import biopandas as bpd
import matplotlib.pyplot as plt
from biopandas.pdb import PandasPdb


# In[4]:


#6LZG - Structure of novel coronavirus spike receptor-binding domain complexed with its receptor ACE2

ppdb = PandasPdb().fetch_pdb('6lzg')


# In[30]:


ppdb.df['ATOM'].columns


# In[23]:


ppdb.df['ATOM']['b_factor'].plot(kind = 'line', color = 'green')
plt.title('Distribution of B-Factors')
plt.xlabel('B-factor')
plt.ylabel('count')
plt.figure(figsize = (25,15))
plt.show()


# In[26]:


atoms_present = list(ppdb.df['ATOM']['atom_name'].unique())


# In[29]:


(atoms_present)


# In[31]:


amino_acid_residues = list(ppdb.df['ATOM']['residue_name'].unique())


# In[33]:


len(amino_acid_residues)


# In[ ]:




