import tkinter as tk
import time as tm
import datetime
import os
import glob
import inspect

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


# Function to retrieve the last line from a file
def get_last_line():
    print('the path is:' + path)
    file_list = glob.glob(path + '/' + file_prefix + '*.csv')
    file_list.sort()
    datafile = file_list[-1] #most recent data file
    
    with open(datafile, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = (f.readline().decode())
        return(last_line)
    
# Padding character
padding_char = '_'

# Function to update background color variable based on air quality index
def update_bg_color(PM_type):
            
    aqi_color = 'black'

    return(aqi_color)


def update_my_window_label():
    my_window['bg'] = update_bg_color('0')
    
    my_window.after(5000, update_my_window_label)

def update_title_label():
    title_label['bg'] = update_bg_color('0')
    
    title_label.after(5000, update_title_label)

def update_clock_label():
    clock_label['bg'] = update_bg_color('0')
    
    clock_label.after(5000, update_clock_label)

def update_temp_title_label():
    temp_title_label['bg'] = update_bg_color('0')
    
    temp_title_label.after(5000, update_temp_title_label)

def update_temp_unit_label():
    temp_unit_label['bg'] = update_bg_color('0')
    
    temp_unit_label.after(5000, update_temp_unit_label)


# Function to update temp_data_label with latest reading from a file
def update_temp_data_label():
    raw_data_line = get_last_line().rstrip()
    temperature = raw_data_line.split(',')[1 ]
    temp_data_label['text'] = "{:6.1f}".format(float(temperature))

    temp_data_label['bg'] = update_bg_color('0')
    
    temp_data_label.after(5000, update_temp_data_label)


# Function to update clock_label widget with system clock reading
def display_time():
    current_time = tm.strftime('%I:%M:%S %p')
    clock_label['text'] = current_time
    clock_label.after(200, display_time)

# Function to update time_last_measurement widget
# based on dt value from latest recording
def update_time_last_measurement_data_label():
    #current_time = tm.strftime('%I:%M:%S %p')
    raw_data_line = get_last_line().rstrip()
    dt_latest = raw_data_line.split(',')[0]
    dt_latest_obj = datetime.datetime.strptime(dt_latest, "%Y-%m-%d %H:%M:%S.%f")
    time_last_measurement = dt_latest_obj.strftime("%I:%M:%S")
    time_last_measurement_data_label['text'] = time_last_measurement

    time_last_measurement_data_label['bg'] = update_bg_color('0')

    time_last_measurement_data_label.after(5000, update_time_last_measurement_data_label)

def update_time_last_measurement_label():
    time_last_measurement_label['bg'] = update_bg_color('0')
    
    time_last_measurement_label.after(5000, update_title_label)



#update_bg_color()
# Create the main window with and set its attributes
my_window = tk.Tk()
my_window.title('Kombucha Temperature')
#my_window.configure(bg='black')
my_window['bg']=update_bg_color('0') # has same effect as the line above
#update_my_window_label()

my_window.geometry(monitor_resolution)
#my_window.overrideredirect(True)
my_window.wm_attributes('-fullscreen',fullscreen_boolean)
#my_window.wm_attributes('-topmost','true')

# Create the title_label widget
title_label = tk.Label(my_window, text='Kombucha Monitor', font='ariel 70', fg='white')
title_label.grid(row=0, column=0, columnspan=2)
update_title_label()

# Create the clock_label widget
clock_label = tk.Label(my_window, font='ariel 70', fg='gray')
clock_label.grid(row=100, column=0, columnspan=3)
display_time()
update_clock_label()

# Create the temp_title_label widget
temp_title_label = tk.Label(my_window, text='Temperature'.ljust(23,padding_char), font='courier 45', fg='gray')
temp_title_label.grid(row=1, column=0, sticky='W')
update_temp_title_label()

# Create the temp_data_label widget
temp_data_label = tk.Label(my_window, font='courier 45 bold', fg='gray')
temp_data_label.grid(row=1, column=1)
update_temp_data_label()

# Create the temp_unit_label widget
degree_sign = u'\N{DEGREE SIGN}' #unicode
temp_unit_label = tk.Label(my_window, text=degree_sign+'C', font='courier 45', fg='gray')
temp_unit_label.grid(row=1, column=2, sticky='W')
update_temp_unit_label()


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

