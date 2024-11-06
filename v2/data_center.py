import pandas as pd

# DataCenter class to convert csv file to pandas dataframe 
# all matcher scripts utilize dataframes adapt DataCenter to convert needed data to dataframe

class Data_Center(): 

    def __init__(self, url) -> pd.DataFrame:
        self.data_url = url
        return pd.read_csv(url)