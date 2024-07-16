from dataclasses import dataclass
import os , pymongo

@dataclass

class EnvironmenVariable:
    mongo_db_url:str=os.getenv("MONGODB_URL_KEY")
    
    

env_var=EnvironmenVariable()
mongo_client=pymongo.MongoClient(env_var.mongo_db_url)