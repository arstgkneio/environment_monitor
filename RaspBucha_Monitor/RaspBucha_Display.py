import tkinter as tk
import time as tm
import datetime
import os
import glob
import inspect

 
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
    
while True:
    print(read_temp())  
    time.sleep(1)
    

# Display Settings
monitor_resolution = '1024x600'
fullscreen_boolean = False

# Gets the canonical path, eliminating any symbolic links
module_path = inspect.getfile(inspect.currentframe())

# Builds working directory using canonical path
module_dir = os.path.realpath(os.path.dirname(module_path))

# Folder containing .csv files
path = module_dir + "/bucha_logs"
file_prefix = 'bucha_log'



# Create time_last_measurement_label widget
time_last_measurement_label = tk.Label(my_window, text = 'last update:', font = 'courier 25', fg='gray')
time_last_measurement_label.grid(row=101, column=1)
update_time_last_measurement_label()

# Create time_last_measurement_data_label widget
time_last_measurement_data_label = tk.Label(my_window, font = 'courier 25 bold', fg ='gray')
time_last_measurement_data_label.grid(row=101, column=2, columnspan=2)
update_time_last_measurement_data_label()



# Initiate the window's main loop that waits for user's actions
my_window.mainloop()

