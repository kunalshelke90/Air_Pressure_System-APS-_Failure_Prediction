from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import Sensor_Exception
import os , sys
from sensor.logger import logging
from sensor.utils2 import dump_csv_to_mongodb_collection
from sensor.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig
from fastapi import FastAPI,File,UploadFile,Response
from sensor.constant.application import APP_HOST,APP_PORT
from sensor.pipeline.training_pipeline import TrainPipeline
from starlette.responses import RedirectResponse # it will send directly to our main path where we want to go
from uvicorn import run as app_run #uvicorn is server
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping,SensorModel
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
from sensor.constant.training_pipeline import SAVED_MODEL_DIR,TARGET_COLUMN
from sensor.exception import Sensor_Exception
import pandas as pd
from sensor.utils.main_utils import load_object


app=FastAPI()

origin=["*"]
#cross origin Resource sharing (cors)
app.add_middleware(CORSMiddleware,allow_origins=origin,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])





@app.get("/",tags=["authentication"])
async def index(): #async menans consider there are 3 steps and first is not done or need to wait it will go to step 2 it will not wait for step 1 till end
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():
    try: 
        training_pipeline = TrainPipeline()
        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline already running")
    
        training_pipeline.run_pipeline()
        return Response("Traning Successfully Completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")



@app.get("/predict")
async def predic():
    try:
        # get data and from the csv file 
        # covert it into dataframe 
        file_path="train1.csv"   
        df =pd.read_csv(file_path)

        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = Model_resolver.get_best_model_path()
        model= load_object(file_path=best_model_path)
        y_pred=model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping,inplace=True)


        # get the prediction output as you wnat 

        csv_data = df.to_csv(index=False)
        return Response(content=csv_data, media_type="text/csv")
    
    
    except Exception as e:
        raise Sensor_Exception(e, sys)
        

    
if __name__=="__main__":


    app_run(app,host=APP_HOST,port=APP_PORT)
    
    
#def main():
#     try: 
#         training_pipeline = TrainPipeline()
#         training_pipeline.run_pipeline()
#     except Exception as e:
#         raise Sensor_Exception(e,sys)
#         logging.exception(e) 
    
    
    
    
  # file_path="/Users/myhome/Downloads/sensorlive/aps_failure_training_set1.csv"
    # database_name="ineuron"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)  
    
    
    
    
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)


# from sensor.configuration.mongo_db_connection import MongoDBClient
# from sensor.exception import Sensor_Exception
# import os , sys
# from sensor.logger import logging
# #from  sensor.utils import dump_csv_file_to_mongodb_collecton
# #from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

# from sensor.pipeline.training_pipeline import TrainPipeline

# # def test_exception():
# #     try:
# #         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
# #         a=1/0
# #     except Exception as e:
# #        raise SensorException(e,sys) 



# if __name__ == "__main__":

#     # file_path="/Users/myhome/Downloads/sensorlive/aps_failure_training_set1.csv"
#     # database_name="ineuron"
#     # collection_name ="sensor"
#     # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

#     training_pipeline = TrainPipeline()
#     training_pipeline.run_pipeline()
