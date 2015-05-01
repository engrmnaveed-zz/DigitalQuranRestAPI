__author__ = 'Naveed'




from time import mktime
from datetime import datetime
from datetime import date
import re

def server_time():
    return int(mktime((datetime.now()).timetuple()))

def server_date():
    return int(mktime((datetime.now().date()).timetuple()))

def to_epoch(value):
    if isinstance(value, datetime):
        return (mktime(value.utctimetuple()) * 1000) + get_milliseconds_part_of_datetime(value)
    if isinstance(value, date):
        return value.strftime('%Y-%m-%d')
    return 0


def to_epoch_micro(value):
    """
    This is a view method to return the data in milli-seconds.

        :param value: Instance of `datetime.datetime`.
        :returns: `float` as the number of seconds since unix epoch.
    """
    return (mktime(value.utctimetuple()) * 1000000) + get_microseconds_part_of_datetime(value)


def from_epoch(value):
    """
        :param value:
            Instance of `float` as the number of seconds since unix epoch.
        :returns:
            Instance of `datetime.datetime`.
    """
    return datetime.utcfromtimestamp(value / 1000)

def from_epoch_micro(value):
    """
        :param value:
            Instance of `float` as the number of seconds since unix epoch.
        :returns:
            Instance of `datetime.datetime`.
    """
    return datetime.utcfromtimestamp(value / 1000000)

def clean_dict(data):
    if not isinstance(data, dict): return data
    for key in data.keys():
        value = data[key]
        if isinstance(value, dict): clean_dict(value)
        if isinstance(value, (list, dict)) and not value:
            del data[key]
        elif value is None:
            del data[key]
    return data

def hour_to_seconds(hours=0):
    return int(hours * 60 * 60)

def get_milliseconds_part_of_datetime(value):
    try:
        date = str(value)
        milliseconds = int(date[len(date)-6:len(date)-3])
        return milliseconds
    except:
        return 0

def get_microseconds_part_of_datetime(value):
    try:
        date = str(value)
        milliseconds = int(date[len(date)-6:len(date)])
        return milliseconds
    except:
        return 0


def timeField_to_seconds(value):
    str_time = str(value)
    times = map(int, re.split(r"[:,]", str_time))
    return times[0]*3600+times[1]*60+times[2]


