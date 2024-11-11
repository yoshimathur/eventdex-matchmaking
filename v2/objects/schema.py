from pydantic import BaseModel

class Prompt(BaseModel): 
    features: list[str]
    queries: list[str]

class Entity(BaseModel): 
    features: list[str]
    data: list[str]

class Matcher_Output(BaseModel): 
    entities: list[Entity]