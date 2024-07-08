import spacy
import pandas as pd 
import numpy as np 

nlp = spacy.load("en_core_web_lg")
stop_words = []

df = pd.read_csv('data/Cleaned Seller data.csv')

for column in df.columns: 
    if df[column].dtype == object: 
        doc_series = df[column].apply(nlp)
        df[column] = doc_series.apply(lambda doc: np.mean([token.vector for token in doc if not token in stop_words]))

df.to_csv('data/Vectorized Seller data.csv')