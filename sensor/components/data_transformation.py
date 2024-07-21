#in this file you need to do chanegs a lot according to eda of your project
from sensor.exception import Sensor_Exception
from sensor.entity.artifact_entity import DataTransformationArtifact,DataValidationArtifact
from sensor.constant.training_pipeline import TARGET_COLUMN
from sensor.entity.config_entity import DataTransformationConfig
from sensor.logger import logging
from sensor.ml.model.estimator import TargetValueMapping
from sensor.utils.main_utils import save_numpy_array_data,save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from imblearn.combine import SMOTETomek
import pandas as pd
import numpy as np
import sys

class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,data_transformation_config:DataTransformationConfig):
        #:param data_validation_artifact:output reference of ingestion artifact stage 
        #:param data_transformation_config:output configuration for data transformation
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config
        except Exception as e:
            raise Sensor_Exception(e,sys)
        
    
    @staticmethod
    def read_file(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise Sensor_Exception (e,sys)
    
    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            robust_scaler=RobustScaler()#keep every feature in same range and handle outliers
            simple_imputer=SimpleImputer()#replace missing values as with zero
            preprocessor=Pipeline(steps=[("Imputer",simple_imputer),("Robust_scaler",robust_scaler)])
            return preprocessor
        except Exception as e:
            raise Sensor_Exception(e,sys) from e
        
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            train_df=DataTransformation.read_file(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_file(self.data_validation_artifact.valid_test_file_path)
            preprocessor=self.get_data_transformer_object()
            
            #training dataframe
            
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]
            
            target_feature_train_df=target_feature_train_df.replace(TargetValueMapping().to_dict())
            
            # testing dataframe 
            
            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(TargetValueMapping().to_dict())
            
            preprocessor_object=preprocessor.fit(input_feature_train_df)
            
            transformed_input_train_feature=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature=preprocessor_object.transform(input_feature_test_df)
            
            smt=SMOTETomek(sampling_strategy="minority")
            #concate /combine
            input_feature_train_final,target_feature_train_final=smt.fit_resample(transformed_input_train_feature,target_feature_train_df)
            input_feature_test_final,target_feature_test_final=smt.fit_resample(transformed_input_test_feature,target_feature_test_df)            
            
            train_arr=np.c_[input_feature_train_final,np.array(target_feature_train_final)]
            test_arr=np.c_[input_feature_test_final,np.array(target_feature_test_final)]
            
            # save numpy array data
            
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object)
            
            # preparing artifact
            
            data_transformation_artifact=DataTransformationArtifact(transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                                                                    transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                                                                    transformed_test_file_path=self.data_transformation_config.transformed_test_file_path)
            
            logging.info(f"Data transformation Artifact:{data_transformation_artifact}")
            return data_transformation_artifact
            
        except Exception as e:
            raise Sensor_Exception (e,sys)from e
        
                                               