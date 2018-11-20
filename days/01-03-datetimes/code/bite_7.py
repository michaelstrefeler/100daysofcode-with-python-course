# bite_7.py
# Parsing dates from logs
'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = 'logfile.txt'
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    p = r"(\d{4}).(\d{2}).(\d{2})(\w)(\d{2}).(\d{2}).(\d{2})"
    match = re.findall(p, line)
    groups = list(match[0])
    date = [int(group) for group in groups if group.isnumeric()]
    return datetime(date[0], date[1], date[2], date[3], date[4], date[5])


def time_between_shutdowns(loglines):
    shutdown_times = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            shutdown_times.append(convert_to_datetime(line))
    return max(shutdown_times) - min(shutdown_times)
