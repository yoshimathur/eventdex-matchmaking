from data_center import Data_Center
from client import OpenAI_Client
from schema import Prompt, Entity

# Matcher class to serve as function to be called by Chat
# variable length parameters to be determined by Chat 
# features and queries to be extracted from prompt in 1:1 

class Matcher(): 

    data = Data_Center('')

    def __init__(self):
        pass

    def find_matches(features, queries): 

        if len(features) != len(queries): 
            # fatal error return 
            pass

        for i, ft in enumerate(features): 
            pass