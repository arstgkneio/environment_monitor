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
path = module_dir + "/environment_data"
file_prefix = 'environment_data'


# Function to retrieve the last line from a file
def get_last_line():
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
    raw_data_line = get_last_line().rstrip()
    aqi_2_5 = raw_data_line.split(',')[2]
    aqi_10 = raw_data_line.split(',')[4]

    #check if aqi_2_5/10 is a number before executing code below


    aqi_color = 'black'
    aqi_color_2_5 = 'black'
    aqi_color_10 = 'black'

    try:
        aqi_2_5_num = float(aqi_2_5)
    except:
        print("aqi_2_5 not a number") 

    else:
        if aqi_2_5_num >= 200:
            aqi_color_2_5 = 'maroon'
        elif aqi_2_5_num >= 150:
            aqi_color_2_5 = 'red'
        elif aqi_2_5_num >= 100:
            aqi_color_2_5 = 'orange'
        elif aqi_2_5_num >= 50:
            aqi_color_2_5 = 'yellow'
        elif aqi_2_5_num >= 0:
            aqi_color_2_5 = 'green'
        else:
            aqi_color_2_5 = 'black'

    try:
        aqi_10_num = float(aqi_10)
    except: 
        print("aqi_10 not a number") 
    else:    

        if aqi_10_num >= 200:
            aqi_color_10 = 'maroon'
        elif aqi_10_num >= 150:
            aqi_color_10 = 'red'
        elif aqi_10_num >= 100:
            aqi_color_10 = 'orange'
        elif aqi_10_num >= 50:
            aqi_color_10 = 'yellow'
        elif aqi_10_num >= 0:
            aqi_color_10 = 'green'
        else:
            aqi_color_10 = 'black'
            
    #print(aqi_color)
    if PM_type == '2_5':
        return(aqi_color_2_5)
    elif PM_type == '10':
        return(aqi_color_10)
    else:
        return(aqi_color)
'''
#background color set based on higher of the two aqi values
    if float(aqi_2_5) >= 200 or float(aqi_10) >= 200:
        aqi_color = 'maroon'
    elif float(aqi_2_5) >= 150 or float(aqi_10) >= 150:
        aqi_color = 'red'
    elif float(aqi_2_5) >= 100 or float(aqi_10) >= 100:
        aqi_color = 'orange'
    elif float(aqi_2_5) >= 50 or float(aqi_10) >= 50:
        aqi_color = 'yellow'
    elif float(aqi_2_5) >= 0 or float(aqi_10) >= 0:
        aqi_color = 'green'
    else:
        aqi_color = 'black'
'''



# Function which updates background of static labels
#def update_bg_of_static_label(label_name):
#    label_name['bg'] = update_bg_color()
#   
#    label_name.after(5000, update_bg_of_static_label)

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

def update_press_title_label():
    press_title_label['bg'] = update_bg_color('0')
    
    press_title_label.after(5000, update_press_title_label)

def update_press_unit_label():
    press_unit_label['bg'] = update_bg_color('0')
    
    press_unit_label.after(5000, update_press_unit_label)

def update_humid_title_label():
    humid_title_label['bg'] = update_bg_color('0')
    
    humid_title_label.after(5000, update_humid_title_label)

def update_humid_unit_label():
    humid_unit_label['bg'] = update_bg_color('0')
    
    humid_unit_label.after(5000, update_humid_unit_label)

def update_aqi_2_5_title_label():
    aqi_2_5_title_label['bg'] = update_bg_color('2_5')
    
    aqi_2_5_title_label.after(5000, update_aqi_2_5_title_label)

def update_aqi_10_title_label():
    aqi_10_title_label['bg'] = update_bg_color('10')
    
    aqi_10_title_label.after(5000, update_aqi_10_title_label)

# Function to update temp_data_label with latest reading from a file
def update_temp_data_label():
    raw_data_line = get_last_line().rstrip()
    temperature = raw_data_line.split(',')[5]
    temp_data_label['text'] = "{:6.1f}".format(float(temperature))

    temp_data_label['bg'] = update_bg_color('0')
    
    temp_data_label.after(5000, update_temp_data_label)

# Function to update press_data_label with latest reading from a file
def update_press_data_label():
    raw_data_line = get_last_line().rstrip()
    pressure = raw_data_line.split(',')[8]
    press_data_label['text'] = "{:6.1f}".format(float(pressure))

    press_data_label['bg'] = update_bg_color('0')
    
    press_data_label.after(5000, update_press_data_label)

# Function to update humid_data_label with latest reading from a file
def update_humid_data_label():
    raw_data_line = get_last_line().rstrip()
    humidity = raw_data_line.split(',')[7]
    humid_data_label['text'] = "{:6.1f}".format(float(humidity))

    humid_data_label['bg'] = update_bg_color('0')
    
    humid_data_label.after(5000, update_humid_data_label)

# Function to update aqi_2_5_data_label with latest reading from a file
def update_aqi_2_5_data_label():
    raw_data_line = get_last_line().rstrip()
    aqi_2_5 = raw_data_line.split(',')[2]
    try:
        aqi_2_5_num = float(aqi_2_5)
    except:
        aqi_2_5_data_label['text'] = "{:6s}".format(aqi_2_5)
    else:
        aqi_2_5_data_label['text'] = "{:6.1f}".format(aqi_2_5_num)
    
    aqi_2_5_data_label['bg'] = update_bg_color('2_5')
    

   # aqi_2_5_data_label.configure(bg=aqi_color) #updates background color in a different way
    
    aqi_2_5_data_label.after(5000, update_aqi_2_5_data_label)
    
# Function to update aqi_10_data_label with latest reading from a file
def update_aqi_10_data_label():
    raw_data_line = get_last_line().rstrip()
    aqi_10 = raw_data_line.split(',')[4]

    try:
        aqi_10_num = float(aqi_10)
    except:
        aqi_10_data_label['text'] = "{:6s}".format(aqi_10)
    else:
        aqi_10_data_label['text'] = "{:6.1f}".format(aqi_10_num)
    
    aqi_10_data_label['bg'] = update_bg_color('10')

    #aqi_10_data_label.configure(bg=aqi_color)

    aqi_10_data_label.after(5000, update_aqi_10_data_label)

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
my_window.title('Environment Data')
#my_window.configure(bg='black')
my_window['bg']=update_bg_color('0') # has same effect as the line above
#update_my_window_label()

my_window.geometry(monitor_resolution)
#my_window.overrideredirect(True)
my_window.wm_attributes('-fullscreen',fullscreen_boolean)
#my_window.wm_attributes('-topmost','true')

# Create the title_label widget
title_label = tk.Label(my_window, text='En-pi-ronment Monitor', font='ariel 70', fg='white')
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

# Create the press_title_label widget
press_title_label = tk.Label(my_window, text='Pressure'.ljust(23,padding_char), font='courier 45', fg='gray')
press_title_label.grid(row=2, column=0, sticky='W')
update_press_title_label()

# Create the pressure_data_label widget
press_data_label = tk.Label(my_window, font='courier 45 bold', fg='gray')
press_data_label.grid(row=2, column=1)
update_press_data_label()

# Create the press_unit_label widget
press_unit_label = tk.Label(my_window, text='hPa', font='courier 45', fg='gray')
press_unit_label.grid(row=2, column=2, sticky='W')
update_press_unit_label()

# Create the humid_title_label widget
humid_title_label = tk.Label(my_window, text='Humidity'.ljust(23,padding_char), font='courier 45', fg='gray')
humid_title_label.grid(row=3, column=0, sticky='W')
update_humid_title_label()


# Create the humid_data_label widget
humid_data_label = tk.Label(my_window, font='courier 45 bold', fg='gray')
humid_data_label.grid(row=3, column=1)
update_humid_data_label()


# Create the humid_unit_label widget
humid_unit_label = tk.Label(my_window, text='%', font='courier 45', fg='gray')
humid_unit_label.grid(row=3, column=2, sticky='W')
update_humid_unit_label()


# Create the aqi_2_5_title_label widget
aqi_2_5_title_label = tk.Label(my_window, text='AQI Index(2.5μm)'.ljust(23,padding_char), font='courier 45', fg='gray')
aqi_2_5_title_label.grid(row=4, column=0, sticky='W')
update_aqi_2_5_title_label()

# Create the aqi_2_5_data_label widget
aqi_2_5_data_label = tk.Label(my_window, font='courier 45 bold', fg='gray')
aqi_2_5_data_label.grid(row=4, column=1)
update_aqi_2_5_data_label()


# Create the aqi_10_label widget
aqi_10_title_label = tk.Label(my_window, text='AQI Index(10μm)'.ljust(23,padding_char), font='courier 45', fg='gray')
aqi_10_title_label.grid(row=5, column=0, sticky='W')
update_aqi_10_title_label()

# Create the aqi_10_data_label widget
aqi_10_data_label = tk.Label(my_window, font='courier 45 bold', fg='gray')
aqi_10_data_label.grid(row=5, column=1)
update_aqi_10_data_label()

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

