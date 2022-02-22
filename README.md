# cs361_datetime_service

requirement
-python3
-python plugin geocoder tzwhere pytz

please do the pip install on the following (pip install [name below]) or (pip3 install [name below])
-geocoder
-tzwhere
-pytz

file detail
-mservice.py --> microservice file
-example_req.py --> demonstration file
-command_dtz.txt --> command file (the microservice will autorun if the condition in this file met)
-dtz_res.csv --> result file

how to use microservice

step1 : run mservice.py (the service will stay until you press enter to terminate the service)
step2 : run your code that can trigger mservice.py to deliver the data (such as the demonstration file)
step2.1 : to meet the autorun condition your code need to overwrite the commandfile(command_dtz.txt) by write "req" on the firstline and save it (sometimes need flush() to make it save at that time)
step3 : receive the data at result file(dtz_res.csv) the data will be in the second line (the first line is data label)
