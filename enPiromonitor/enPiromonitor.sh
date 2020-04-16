# This bash script script runs both the enPiromonitor program and the display program simultaneously

# Assigns environment variable necessary for display program 
export DISPLAY=:0.0 

python3 /<PATH_GOES_HERE>/Monitor_Program.py &



python3 /<PATH_GOES_HERE>/Display_Program.py &
