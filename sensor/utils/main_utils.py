from sensor.exception import Sensor_Exception
import pandas as pd
import numpy as np
import yaml,os,dill,sys

# this file is created to read and write schema.yaml file
# with this file you use any yaml file now
#utils folder is created which are not about sepecific components and we can use it in any  component if we want 

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise Sensor_Exception(e,sys)


def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as file:
            yaml.dump(content,file)
    except Exception as e:
        raise Sensor_Exception (e,sys)
