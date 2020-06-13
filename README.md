# Bioinformatics-Repo

## Contains the codes performing bioinformatics tasks

### 1) biopandas_structure.py

"BIOPANDAS" python library allows bioinformaticians to work with PDB and MOL2 molecular structures in Pandas dataframes. A reliable and efficient source depicting the usage is Biopandas official documentation : http://rasbt.github.io/biopandas/

The structure of novel coronavirus spike receptor-binding domain complexed with its receptor ACE2 was analyzed using Biopandas library in Python

### 2) final_sentiment_analysis.py

Parsing Nature.com article to learn attributes of the article and perform Sentiment analysis using TextBlob, NLTK, Newspaper3k Libraries

The inspiration for this program was from this tutorial. Do give this a read : https://levelup.gitconnected.com/sentiment-analysis-using-machine-learning-python-9122e03f8f7b

The input to the Python program is the link of the article you want to parse. Eg: https://www.nature.com/articles/d41586-020-01315-7 . An output text file is written with the following details about the article of you interest:

Author Of the Article
Image in the article
Entire text of the article
Keywords in the article
Rough Summary Of the article
Sentiment Polarity Value and analysis of sentiment (positive, negative or neutral) The TextBlob's sentiment property returns a Sentiment object. The polarity indicates sentiment with a value from -1.0 (negative) to 1.0 (positive) with 0.0 being neutral. The subjectivity is a value from 0.0 (objective) to 1.0 (subjective). (Source: https://www.pythonprogramming.in/sentiment-analysis-using-textblob.html)

### 3) retrieve_structures.py 
    Retrieves structures from PUBCHEM database using python

