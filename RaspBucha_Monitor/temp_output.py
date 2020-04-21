##### LIBRARIES #####
import time
from datetime import datetime
import os
import os.path
import glob
import inspect 

### SETTINGS ###

SLEEP_DURATION = 5 #seconds
log_name_prefix = "bucha_log"
module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))
data_log_dir = module_dir + "/bucha_logs"



os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
    lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def create_header(fn):
    if os.path.exists(fn):
        header = ""
    else:
        header = "date & time, temperature\n"
  
    return header 

def log_buch_temp():
    now = datetime.now()
    date_stamp = now.strftime("%Y%m%d")
    
    log_filename = log_name_prefix + "_" + date_stamp + ".csv"
    log_file = data_log_dir + "/" + log_filename
    
    log_header = create_header(log_file)
    
    with open(log_file, "a") as log:
        log.write(log_header)
        dt = datetime.now()
        log.write("{},{}\n".format(dt, bucha_temp))
    log.close()
	
##### MAIN PROGRAM #####
while True:
    bucha_temp = read_temp()
    log_buch_temp()  
    time.sleep(SLEEP_DURATION)

