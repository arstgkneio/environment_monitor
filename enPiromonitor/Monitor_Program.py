##### LIBRARIES #####
import time
from datetime import datetime
import os.path
import psutil
from sds011 import *
import aqi
from sense_hat import SenseHat
import inspect

##### LOGGING SETTINGS #####
module_path = inspect.getfile(inspect.currentframe())

print(module_path)

module_dir = os.path.realpath(os.path.dirname(module_path))

print(module_dir)

data_log_dir = module_dir + "/environment_data"

print(data_log_dir)

log_name_prefix = "environment_data"
SLEEP_DURATION = 60 #in seconds
my_colour = [255, 255, 255] #sense hat color 

##### FUNCTIONS #####
sense = SenseHat()
sense.clear()
sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)

def get_data(n=3):
        sensor.sleep(sleep=False)
        pmt_2_5 = 0
        pmt_10 = 0
        time.sleep(10)
        for i in range (n):
            x = sensor.query()
            pmt_2_5 = pmt_2_5 + x[0]
            pmt_10 = pmt_10 + x[1]
            time.sleep(2)
        pmt_2_5 = round(pmt_2_5/n, 1)
        pmt_10 = round(pmt_10/n, 1)
        sensor.sleep(sleep=True)
        time.sleep(2)
        return pmt_2_5, pmt_10
    

def conv_aqi(pmt_2_5, pmt_10):
    aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pmt_2_5))
    aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pmt_10))
    return aqi_2_5, aqi_10


def save_log():        
    now = datetime.now()
    date_stamp = now.strftime("%Y%m%d")
    
    log_filename = log_name_prefix + "_" + date_stamp + ".csv"
    log_file = data_log_dir + "/" + log_filename
    
    log_header = create_header(log_file)
    
    with open(log_file, "a") as log:
        log.write(log_header)
        dt = datetime.now()
        log.write("{},{},{},{},{},{},{},{},{}\n".format(dt, pmt_2_5, aqi_2_5, pmt_10, aqi_10, temp_from_humidity, temp_from_pressure, humidity, pressure))
    log.close()
    
    
def get_sense_data():
    temp_from_h = sense.get_temperature_from_humidity()
    temp_from_p = sense.get_temperature_from_pressure()
    hum = sense.get_humidity()
    pres = sense.get_pressure()
    
    return temp_from_h, temp_from_p, hum, pres

def create_header(fn):
    if os.path.exists(fn):
        header = ""
    else:
        header = "date & time,pmt_2_5,aqi_2_5,pmt_10,aqi_10,temp_from_humidity,temp_from_pressure,humidity,pressure\n"
  
    return header 


##### MAIN PROGRAM #####
while True:
    pmt_2_5, pmt_10 = get_data()
    aqi_2_5, aqi_10 = conv_aqi(pmt_2_5, pmt_10)
    temp_from_humidity, temp_from_pressure, humidity, pressure = get_sense_data()
     
    save_log()
        
    print("Writing to file...")
    time.sleep(SLEEP_DURATION)

            
      

