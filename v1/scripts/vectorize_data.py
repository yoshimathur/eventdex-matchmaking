import spacy
import pandas as pd
import numpy as np

nlp = spacy.load("en_core_web_lg")
df = pd.read_csv('data/Cleaned Seller data.csv', index_col=0)
ignore_cols = ['Primary Email', 'Secondary Email']
vector_df = pd.DataFrame()

for column in df.columns:
    vector_column = list()
    if df[column].dtype == object and column not in ignore_cols:
        for index, item in df[column].items(): 
            doc = nlp(item)
            vectors = [token.vector for token in doc if not token.is_stop and not token.is_punct and token.has_vector]
            if vectors:
                vector_column = list(np.mean(vectors, axis=0)) 
            else:
                vector_column = list(np.zeros(nlp.vocab.vectors_length))
    if vector_column and np.mean(vector_column) != 0: 
        vector_df[column] = vector_column
        print(column)

vector_df.to_csv('data/Vectorized Seller data.csv') 