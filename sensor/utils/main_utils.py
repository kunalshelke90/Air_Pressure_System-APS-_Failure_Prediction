from sensor.exception import Sensor_Exception
from sensor.logger import logging
import pandas as pd
import numpy as np
import yaml,os,dill,sys

# this file is created to read and write schema.yaml file
# with this file you use any yaml file now
#utils folder is created which are not about sepecific components and we can use it in any  component if we want 
# it is created to use multiple times anywhere

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

def save_numpy_array_data(file_path:str,array:np.array):
    #save numpy array data to file, file path :str Location of file ,  array:np.array  data to save 
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb")as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise Sensor_Exception(e,sys)
    
def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise Sensor_Exception (e,sys) from e

def save_object(file_path:str,obj:object)->None:
    try:
        logging.info(f"Entered the save_object method of Mainutils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info(f"Exited the save_object method of Mainutils class")
    except Exception as e:
        raise Sensor_Exception (e,sys)

    
def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception (f"The file {file_path} is not exits")
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise Sensor_Exception(e,sys)


        