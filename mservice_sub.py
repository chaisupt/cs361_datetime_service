
# # note
# please do pip/pip3 install the following
# geocoder
# pytz
# tzwhere

# from geopy.geocoders import Nominatim
import geocoder
from datetime import datetime
import pytz
from tzwhere import tzwhere
import string
import os
import time
import sys
import select
import keyboard

def curr_time_service() :
    # get current longitude latitude
    g = geocoder.ip('me')
    # print(g.latlng)
    the_set=g.latlng

    #initial tzwhere
    # global tzwhere
    t_tz= tzwhere.tzwhere()
    #find the timezone from current latitude / longitude
    timezone_str = t_tz.tzNameAt(the_set[0], the_set[1]) # Seville coordinates
    #set the timezone into appropriate format
    timezone = pytz.timezone(timezone_str)
    #show the timezone
    # print(datetime.now(timezone))
    dict_result={}
    dict_result['date']=str(datetime.now(timezone).date())
    dump=str(datetime.now(timezone).time())
    dict_result['time']=dump[:8]
    dict_result['timezone']=str(datetime.now(timezone).tzname())
    # print(dict_result)
    return dict_result

def doit():
    #setup output
    firstline="date,time,time_zone\n"
    ddict=curr_time_service()
    secondline=ddict["date"] + ","+ ddict["time"] + "," + ddict["timezone"]
    # print(secondline)
    rs_file=open("dtz_res.csv","w")
    rs_file.write(firstline)
    rs_file.write(secondline)
    rs_file.flush()
    rs_file.close()

def check_commandfile():
    command_file=open("command_dtz.txt","r")
    commander=command_file.readline()
    commander=commander.replace("\n","")
    command_file.close()
    if(commander=="req"):
        command_file=open("command_dtz.txt","w")
        command_file.write(" ")
        command_file.flush()
        command_file.close()
        doit()


print("service is running please press control+c to quit system")
while True:
    try:
        check_commandfile()
    except KeyboardInterrupt:
        print(" \nthe service was closed thank you for using time service")
        break
