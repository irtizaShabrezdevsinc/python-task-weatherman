# date
# 0
# maxTemperatureC
# 1
# meanTemperatureC
# 2
# minTemperatureC
# 3
# DewPointC
# 4
# meanDewPointC
# 5
# minDewpointC
# 6
# maxhumidity
# 7
# meanhumidity
# 8
# minhumidity
# 9
# maxeaevel
# 10
# PressurehPa
# 11
# meansealevelPressurehPa,
# 12
# minsealevelPressurehPa
# 13
# max_visibilityKm
# 14
# mean_visibilityKm
# 15
# min_visibilitykm
# 16
# max_wind speedKm/h
# 17
# mean_wind speedKm/h,
# 18
# max_gust speedKm/h
# 19
# Precipitation
# 20
# CloudCover
# 21
# Events
# 22
import read_file
import sys
import check_path
import task

check = check_path.verify_path(sys.argv)
if check in (1, 2, 3):
    data = read_file.path(sys.argv[3], sys.argv[2], check)
    task.process(data, sys.argv[2], check)

else:
    print("You enter the wrong command line")
    print("Enter command for example python3 weatherman.py -e 2002 /path/to/filesFolder")
