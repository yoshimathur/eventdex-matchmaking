import openai

# OpenAI_Client class to create an easily accessible access point to OpenAI API 
# helps easily utilize 

class OpenAI_Client(): 

    api_key = "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"

    def __init__(self):
        self.client = openai.OpenAI(api_key=self.api_key)