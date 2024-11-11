import os, sys
objects_path = "/".join(os.path.abspath(__file__).split("/")[:-2]) + "/objects"
sys.path.insert(0, objects_path)

from objects.data_center import Data_Center
from objects.client import OpenAI_Client
from objects.schema import Prompt, Entity

# Matcher script to serve as function to be called by Chat
# variable length parameters to be determined by Chat 
# features and queries to be extracted from prompt in 1:1 

df = Data_Center("./data/Test MM  Seller data from wbenc.csv")
print(df.head())

def find_matches(features, queries): 

    if len(features) != len(queries): 
        # fatal error return 
        pass

    for i, ft in enumerate(features): 
        pass