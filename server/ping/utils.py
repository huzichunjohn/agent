import datetime
import time


def get_timestamp_by_string(date_str, format):
    try:
	date = datetime.datetime.strptime(date_str, format)
	return int(time.mktime(date.timetuple()))
    except ValueError as e:
	return ''	

def get_string_by_timestamp(timestamp, output_format):
    return datetime.datetime.fromtimestamp(timestamp).strftime(output_format)

print get_timestamp_by_string("2016-06-30 12:00:11", "%Y-%m-%d %H:%M:%S")
print get_string_by_timestamp(get_timestamp_by_string("2016-06-30 12:00:11", "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")


print get_timestamp_by_string("2016-06-30 12:00:11", "%Y-%m-%d")

