# Importing the library
import psutil

# Calling psutil.cpu_precent() for 4 seconds
while (True):
    try:
        cpu_usage = psutil.cpu_percent(5)
        if (cpu_usage > 80):
            print("Alert! CPU usage exceeds threshold:", cpu_usage)
    except Exception as error:
        print("An exception occured", error)
