import math
import datetime
def calculate_sunrise( latitude, longitude, date):

    time_offset = (longitude / 15.0)
    solar_time = datetime.datetime.combine(date, datetime.time(12)) - datetime.timedelta(hours=time_offset)
    hour_angle = math.degrees(math.acos(
    (math.sin(math.radians(-0.83)) - math.sin(math.radians(latitude)) * math.sin(math.radians(23.44))) / (math.cos(math.radians(latitude)) * math.cos(math.radians(23.44)))))
    sunrise = solar_time + datetime.timedelta(minutes=hour_angle * 4)
    return sunrise
