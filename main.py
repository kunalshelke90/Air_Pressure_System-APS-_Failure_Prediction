from sensor.exception import Sensor_Exception
import os,sys
from sensor.logger import logging
def test_exception():
    try:
        logging.info("getting zero division error")
        a=1/0
    except Exception as e:
        raise Sensor_Exception(e,sys)
    
    
if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)