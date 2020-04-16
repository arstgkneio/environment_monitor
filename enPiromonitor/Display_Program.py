import tkinter as tk
import time as tm
import os
import glob

# Settings
monitor_resolution = '1024x600'

# Retrieve the latest data file
path = '/home/pi/Desktop/Air_Quality_Monitor_Code'
file_prefix = 'environment_data'

# Function to retrieve the last line from a file
def get_last_line():
    file_list = glob.glob(path + '/' + file_prefix + '*.csv')
    file_list.sort()
    datafile = file_list[-1]
    
    with open(datafile, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = (f.readline().decode())
        return(last_line)
    
# Padding character
padding_char = '_'

# Function to update temp_data_label with latest reading from a file
def update_temp_data_label():
    raw_data_line = get_last_line().rstrip()
    temperature = raw_data_line.split(',')[5]
    temp_data_label['text'] = "{:6.1f}".format(float(temperature))
    
    temp_data_label.after(5000, update_temp_data_label)

# Function to update press_data_label with latest reading from a file
def update_press_data_label():
    raw_data_line = get_last_line().rstrip()
    pressure = raw_data_line.split(',')[8]
    press_data_label['text'] = "{:6.1f}".format(float(pressure))
    
    press_data_label.after(5000, update_press_data_label)

# Function to update humid_data_label with latest reading from a file
def update_humid_data_label():
    raw_data_line = get_last_line().rstrip()
    humidity = raw_data_line.split(',')[7]
    humid_data_label['text'] = "{:6.1f}".format(float(humidity))
    
    humid_data_label.after(5000, update_humid_data_label)
    

# Function to update aqi_2_5_data_label with latest reading from a file
def update_aqi_2_5_data_label():
    raw_data_line = get_last_line().rstrip()
    aqi_2_5 = raw_data_line.split(',')[2]
    aqi_2_5_data_label['text'] = "{:6.1f}".format(float(aqi_2_5))
    
    aqi_2_5_data_label.after(5000, update_aqi_2_5_data_label)
    
# Function to update aqi_10_data_label with latest reading from a file
def update_aqi_10_data_label():
    raw_data_line = get_last_line().rstrip()
    aqi_10 = raw_data_line.split(',')[4]
    aqi_10_data_label['text'] = "{:6.1f}".format(float(aqi_10))
    
    aqi_10_data_label.after(5000, update_aqi_10_data_label)

# Function to update clock_label widget with system clock reading
def display_time():
    current_time = tm.strftime('%I:%M:%S %p')
    clock_label['text'] = current_time
    clock_label.after(200, display_time)

# Create the main window with and set its atributes
my_window = tk.Tk()
my_window.title('Environment Data')
#my_window.configure(bg='black')
my_window['bg']='black' # has same effect as the line above

my_window.geometry(monitor_resolution)
#my_window.overrideredirect(True)
#my_window.wm_attributes('-fullscreen','true')
#my_window.wm_attributes('-topmost','true')

# Create the title_label widget
clock_label = tk.Label(my_window, text='EnPIronment Monitor', font='ariel 70', bg='black', fg='white')
clock_label.grid(row=0, column=0, columnspan=2)


# Create the clock_label widget
clock_label = tk.Label(my_window, font='ariel 70', bg='black', fg='gray')
clock_label.grid(row=100, column=0, columnspan=3)
display_time()


# Create the temp_title_label widget
temp_title_label = tk.Label(my_window, text='Temperature'.ljust(23,padding_char), font='courier 45', bg='black', fg='gray')
temp_title_label.grid(row=1, column=0, sticky='W')


# Create the temp_data_label widget
temp_data_label = tk.Label(my_window, font='courier 45 bold', bg='black', fg='gray')
temp_data_label.grid(row=1, column=1)
update_temp_data_label()

# Create the temp_unit_label widget
degree_sign = u'\N{DEGREE SIGN}' #unicode
temp_unit_label = tk.Label(my_window, text=degree_sign+'C', font='courier 45', bg='black', fg='gray')
temp_unit_label.grid(row=1, column=2, sticky='W')

# Create the press_title_label widget
press_title_label = tk.Label(my_window, text='Pressure'.ljust(23,padding_char), font='courier 45', bg='black', fg='gray')
press_title_label.grid(row=2, column=0, sticky='W')


# Create the pressure_data_label widget
press_data_label = tk.Label(my_window, font='courier 45 bold', bg='black', fg='gray')
press_data_label.grid(row=2, column=1)
update_press_data_label()

# Create the press_unit_label widget
press_unit_label = tk.Label(my_window, text='hPa', font='courier 45', bg='black', fg='gray')
press_unit_label.grid(row=2, column=2, sticky='W')

# Create the humid_title_label widget
humid_title_label = tk.Label(my_window, text='Humidity'.ljust(23,padding_char), font='courier 45', bg='black', fg='gray')
humid_title_label.grid(row=3, column=0, sticky='W')


# Create the humid_data_label widget
humid_data_label = tk.Label(my_window, font='courier 45 bold', bg='black', fg='gray')
humid_data_label.grid(row=3, column=1)
update_humid_data_label()


# Create the humid_unit_label widget
humid_unit_label = tk.Label(my_window, text='%', font='courier 45', bg='black', fg='gray')
humid_unit_label.grid(row=3, column=2, sticky='W')


# Create the aqi_2_5_title_label widget
aqi_2_5_title_label = tk.Label(my_window, text='AQI Index(2.5μm)'.ljust(23,padding_char), font='courier 45', bg='black', fg='gray')
aqi_2_5_title_label.grid(row=4, column=0, sticky='W')


# Create the aqi_2_5_data_label widget
aqi_2_5_data_label = tk.Label(my_window, font='courier 45 bold', bg='black', fg='gray')
aqi_2_5_data_label.grid(row=4, column=1)
update_aqi_2_5_data_label()


# Create the aqi_10_label widget
aqi_10_title_label = tk.Label(my_window, text='AQI Index(10μm)'.ljust(23,padding_char), font='courier 45', bg='black', fg='gray')
aqi_10_title_label.grid(row=5, column=0, sticky='W')


# Create the aqi_10_data_label widget
aqi_10_data_label = tk.Label(my_window, font='courier 45 bold', bg='black', fg='gray')
aqi_10_data_label.grid(row=5, column=1)
update_aqi_10_data_label()



# Initiate the window's main loop that waits for user's actions
my_window.mainloop()
